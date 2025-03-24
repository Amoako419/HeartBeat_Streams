import json
import time
import random
from kafka import KafkaProducer

# Connect to Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_heartbeat_data():
    return {
        "customer_id": random.randint(1, 100),
        "heartbeat": random.randint(60, 100),  # Normal resting heart rate range
        "timestamp": time.time()
    }

if __name__ == "__main__":
    while True:
        data = generate_heartbeat_data()
        producer.send('heartbeat-data', data)
        print(f"Produced: {data}")
        time.sleep(3)  # Adjust the frequency as needed
