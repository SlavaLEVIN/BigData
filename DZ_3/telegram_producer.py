import asyncio
import fcntl
import json
import os
import subprocess
import sys
from pathlib import Path

from dotenv import load_dotenv
from kafka import KafkaProducer
from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import PeerChannel


CHANNEL_IDS = [
    1050820672, 1149896996, 1101170442, 1036362176,
    1310155678, 1001872252, 1054549314, 1073571855,
]
ROOT = Path(__file__).resolve().parent


def start_producer():
    log_path = ROOT / ".venv" / "telegram_producer.log"
    with log_path.open("a") as log:
        process = subprocess.Popen(
            [sys.executable, "-u", str(ROOT / "telegram_producer.py")],
            stdin=subprocess.DEVNULL, stdout=log, stderr=subprocess.STDOUT,
            start_new_session=True,
        )
    try:
        status = process.wait(timeout=1)
    except subprocess.TimeoutExpired:
        print(f"Сборщик Telegram запущен. Лог: {log_path}")
        return
    if status != 0:
        raise RuntimeError(f"Ошибка запуска сборщика. Подробности: {log_path}")
    print("Сборщик Telegram уже работает.")


def serialize_message(message):
    return json.dumps(message, ensure_ascii=False).encode("utf-8")


async def main():
    load_dotenv(ROOT / ".env")
    api_id = os.getenv("TELEGRAM_API_ID")
    api_hash = os.getenv("TELEGRAM_API_HASH")
    if not api_id or not api_hash:
        raise SystemExit("Заполни TELEGRAM_API_ID и TELEGRAM_API_HASH в DZ_3/.env.")
    api_id = int(api_id)
    producer = KafkaProducer(
        bootstrap_servers="localhost:9092", value_serializer=serialize_message,
        acks="all", retries=3,
    )
    client = TelegramClient(str(ROOT / "telegram"), api_id, api_hash)

    try:
        await client.start()
        await client.get_dialogs()
        channels = []
        for channel_id in CHANNEL_IDS:
            try:
                channel = await client.get_entity(PeerChannel(channel_id))
            except ValueError:
                link = input(f"Ссылка или @username канала {channel_id}: ").strip()
                channel = await client.get_entity(link)
                if channel.id != channel_id:
                    raise ValueError(f"Указан другой канал, нужен ID {channel_id}")
            await client(JoinChannelRequest(channel))
            channels.append(channel)
            print(f"Подключён: {channel.title} ({channel.id})")

        @client.on(events.NewMessage(chats=channels))
        async def send_message(event):
            sender = await event.get_sender()
            username = getattr(sender, "username", None) or f"id:{event.sender_id}"
            message = {
                "username": username,
                "user_id": event.sender_id,
                "channel_id": event.chat_id,
                "message_id": event.id,
                "text": event.raw_text,
                "date": event.date.isoformat(),
            }
            delivery = producer.send("telegram_messages", message)
            await asyncio.to_thread(delivery.get, timeout=30)

        print("Получение новых сообщений. Для остановки: Ctrl+C.")
        await client.run_until_disconnected()
    finally:
        await client.disconnect()
        producer.close()


def run():
    with (ROOT / ".venv" / "telegram_producer.lock").open("a") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            return
        try:
            asyncio.run(main())
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    run()
