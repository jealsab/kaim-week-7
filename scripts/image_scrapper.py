import os
import json
import logging
from telethon.sync import TelegramClient
from telethon.tl.types import MessageMediaPhoto
from dotenv import load_dotenv

# Load environment variables
load_dotenv('../.env')  # Adjust the path to your .env file

# Replace these with your credentials from the .env file
api_id = os.getenv('TG_API_ID')
api_hash = os.getenv('TG_API_HASH')

# Channels to scrape
CHANNELS = ["https://t.me/lobelia4cosmetics", "https://t.me/chemed_channel"]

# Directory to save images
SAVE_DIR = "images"
os.makedirs(SAVE_DIR, exist_ok=True)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("scraping_log.txt"),  # Store logs in this file
        logging.StreamHandler()  # Also output to console
    ]
)

# Temporary storage for raw metadata (if needed)
RAW_METADATA_FILE = "raw_metadata.json"

def store_raw_metadata(metadata):
    """ Store raw metadata in a JSON file """
    if os.path.exists(RAW_METADATA_FILE):
        with open(RAW_METADATA_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(metadata)
    with open(RAW_METADATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Initialize client with session name, api_id, and api_hash
with TelegramClient('telegram_scraper', api_id, api_hash) as client:
    for channel in CHANNELS:
        logging.info(f"Scraping {channel}...")  # Log channel being scraped
        for message in client.iter_messages(channel, limit=100):  # Adjust the limit as needed
            if isinstance(message.media, MessageMediaPhoto):
                try:
                    # Download the image
                    file_path = client.download_media(message.media, SAVE_DIR)
                    logging.info(f"Downloaded: {file_path}")  # Log successful download

                    # Store raw metadata (e.g., message ID, image URL)
                    metadata = {
                        "message_id": message.id,
                        "file_path": file_path,
                        "channel": channel,
                        "date": str(message.date)
                    }
                    store_raw_metadata(metadata)  # Store raw data in a JSON file

                except Exception as e:
                    logging.error(f"Failed to download media for message ID {message.id}: {e}")  # Log errors
