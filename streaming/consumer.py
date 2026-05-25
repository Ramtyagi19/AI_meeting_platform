from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'transcript_events',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode())
)

for msg in consumer:
    print("Received:", msg.value)