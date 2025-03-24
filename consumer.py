import json
from kafka import KafkaConsumer
import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get database credentials from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Connect to PostgreSQL
conn = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)
cursor = conn.cursor()

# Connect to Kafka
consumer = KafkaConsumer(
    'heartbeat-data',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

def insert_heartbeat(data):
    query = "INSERT INTO heartbeats (customer_id, heartbeat, timestamp) VALUES (%s, %s, to_timestamp(%s))"
    cursor.execute(query, (data['customer_id'], data['heartbeat'], data['timestamp']))
    conn.commit()

if __name__ == "__main__":
    for message in consumer:
        data = message.value
        print(f"Consumed: {data}")
        insert_heartbeat(data)
