import psycopg2
import pandas as pd
import json
import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv('../.env')
# Setup logging configuration
logging.basicConfig(
    filename='pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Log start of the process
logging.info("Starting the data pipeline...")

try:
    # Get the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Build the path to the JSON file in the root directory
    json_path = os.path.join(script_dir, "../cleaned_metadata.json")

    # Log the start of data loading
    logging.info(f"Loading cleaned data from {json_path}...")

    # Load your cleaned data (assuming it's a JSON file)
    with open(json_path, "r") as file:
        cleaned_data = pd.json_normalize(json.load(file))

    logging.info(f"Data loaded successfully with {len(cleaned_data)} records.")

    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname='DB_NAME',
        user='DB_USER',
        password='DB_PASSWORD',
        host='DB_HOST',
        port='DB_PORT'
    )
    cursor = conn.cursor()

    # Log start of data insertion
    logging.info("Starting to insert cleaned data into PostgreSQL...")

    # Insert data
    for _, row in cleaned_data.iterrows():
        cursor.execute(
            """
            INSERT INTO cleaned_data (message_id, file_path, channel, date)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (message_id) DO NOTHING
            """,
            (row['message_id'], row['file_path'], row['channel'], row['date'])
        )

    # Commit changes to the database
    conn.commit()
    logging.info("Data insertion completed successfully.")

    # Close the connection
    cursor.close()
    conn.close()

except Exception as e:
    logging.error(f"Error encountered: {str(e)}")

