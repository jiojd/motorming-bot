"""
Motorming Daily Stock Bot
Posts all photos in /photos folder + caption.txt to the Telegram group.
Runs automatically via GitHub Actions every day at 8:00 AM MYT.
"""

import json
import os
import sys
import time
from pathlib import Path

import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
PHOTOS_DIR = Path("photos")
CAPTION_FILE = Path("caption.txt")
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

# Telegram limits
MAX_PHOTOS_PER_ALBUM = 10
MAX_CAPTION_LENGTH = 1024
ALLOWED_EXTS = {".jpg", ".jpeg", ".png", ".webp"}


def chunk(lst, size):
    """Split a list into smaller lists of given size."""
    for i in range(0, len(lst), size):
        yield lst[i : i + size]


def send_album(photos, caption=None):
    """Send a list of up to 10 photos as a Telegram media group."""
    media = []
    files = {}

    try:
        for idx, photo_path in enumerate(photos):
            key = f"photo{idx}"
            item = {"type": "photo", "media": f"attach://{key}"}
            # Caption goes only on the first photo of the album
            if idx == 0 and caption:
                item["caption"] = caption[:MAX_CAPTION_LENGTH]
            media.append(item)
            files[key] = open(photo_path, "rb")

        data = {"chat_id": CHAT_ID, "media": json.dumps(media)}
        response = requests.post(
            f"{TELEGRAM_API}/sendMediaGroup",
            data=data,
            files=files,
            timeout=60,
        )
        if not response.ok:
            print(f"❌ Telegram API error {response.status_code}:")
            print(f"   Response: {response.text}")
            print(f"   CHAT_ID used: {CHAT_ID}")
        response.raise_for_status()
        return response.json()
    finally:
        for f in files.values():
            f.close()


def send_text(text):
    """Send a plain text message (used when no photos available)."""
    response = requests.post(
        f"{TELEGRAM_API}/sendMessage",
        data={"chat_id": CHAT_ID, "text": text},
        timeout=30,
    )
    response.raise_for_status()
    return response.json()


def main():
    # Read caption
    caption = ""
    if CAPTION_FILE.exists():
        caption = CAPTION_FILE.read_text(encoding="utf-8").strip()

    # Find all photos
    if not PHOTOS_DIR.exists():
        print(f"❌ Photos folder not found: {PHOTOS_DIR}")
        sys.exit(1)

    photos = sorted(
        p
        for p in PHOTOS_DIR.iterdir()
        if p.is_file() and p.suffix.lower() in ALLOWED_EXTS
    )

    if not photos:
        print("⚠️ No photos found. Sending text-only message.")
        if caption:
            send_text(caption)
            print("✅ Text message sent.")
        else:
            print("❌ No caption either. Nothing to send.")
            sys.exit(1)
        return

    print(f"📸 Found {len(photos)} photos.")

    albums = list(chunk(photos, MAX_PHOTOS_PER_ALBUM))
    print(f"📦 Splitting into {len(albums)} album(s).")

    for i, album_photos in enumerate(albums):
        # Caption only on the first album, first photo
        album_caption = caption if i == 0 else None
        print(f"   → Sending album {i + 1}/{len(albums)} ({len(album_photos)} photos)...")
        send_album(album_photos, caption=album_caption)
        # Small delay to avoid rate limits
        if i < len(albums) - 1:
            time.sleep(2)

    print("✅ All photos sent successfully!")


if __name__ == "__main__":
    main()
