from telethon import TelegramClient
import os
import pandas as pd
from dotenv import load_dotenv

# Load environment variables
load_dotenv('../.env')  # Adjust the path to your .env file

# Replace these with your credentials
api_id = os.getenv('TG_API_ID')
api_hash = os.getenv('TG_API_HASH')

# Initialize the client
client = TelegramClient('session_name', api_id, api_hash)

# Function to scrape a channel
async def scrape_channel(channel_url):
    print(f"Scraping data from {channel_url}")

    # Dictionary to store scraped data
    data = {'Channel': [], 'Message': []}

    # Get channel entity
    channel = await client.get_entity(channel_url)

    # Fetch messages
    async for message in client.iter_messages(channel, limit=100):  # Adjust limit as needed
        text = message.text if message.text else "Media/Non-Text Message"
        data['Channel'].append(channel.title)
        data['Message'].append(text)

    # Save data to a CSV file
    df = pd.DataFrame(data)
    output_file = f"{channel.title.replace(' ', '_')}_data.csv"
    df.to_csv(output_file, index=False)
    print(f"Scraped data saved to {output_file}")

# Main function to handle multiple channels
async def main():
    # List of channels to scrape
    channels = [
        'https://t.me/DoctorsET',
        'https://t.me/lobelia4cosmetics',
        'https://t.me/yetenaweg',
        'https://t.me/EAHCI'
    ]
    for channel in channels:
        await scrape_channel(channel)

# Run the script
with client:
    client.loop.run_until_complete(main())
