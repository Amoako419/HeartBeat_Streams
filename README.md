# Real-Time Customer Heartbeat Data Pipeline

## Project Description
This project simulates real-time monitoring of customers' heart beat rates using synthetic data. The data is produced to a Kafka topic and consumed by a Kafka consumer that writes into a PostgreSQL database.

## How It Works
1. Synthetic data generator (`producer.py`) sends random heartbeat data to Kafka.
2. Kafka broker manages the streaming.
3. Consumer (`consumer.py`) listens to Kafka and inserts data into PostgreSQL.

## Project Structure
```
heartbeat-project/
├── docker-compose.yml
├── producer.py
├── consumer.py
├── scripts/
│   ├── consumer.py
│   └── producer.py
└── README.md
```

## Database Schema
```sql
CREATE TABLE heartbeats (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    heartbeat INTEGER NOT NULL,
    timestamp TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
```

## How to Run
1. Create a virtual environment: `python -m venv venv`
2. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Start services: `docker-compose up -d`
5. Create Kafka topic: `kafka-topics --create --topic heartbeat-data --bootstrap-server localhost:9092`
6. Run `producer.py`: `python producer.py`
7. Run `consumer.py`: `python consumer.py`
8. Verify data in PostgreSQL.

Enjoy building your real-time data pipeline!
