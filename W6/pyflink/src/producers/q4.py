import csv
import json
from kafka import KafkaProducer
from time import time

topic_name = 'green-trips'
csv_file = 'c:/Users/freil/DEZoom/W6/green_tripdata_2019-10.csv'
required_columns = [
    "lpep_pickup_datetime",
    "lpep_dropoff_datetime",
    "PULocationID",
    "DOLocationID",
    "passenger_count",
    "trip_distance",
    "tip_amount",
]

t0 = time()

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

with open(csv_file, 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for row in reader:
        # Each row will be a dictionary keyed by the CSV headers
        # Send data to Kafka topic "green-trips"
        message = {col: row[col] for col in required_columns}
        producer.send(topic_name, value=message)

# Make sure any remaining messages are delivered
producer.flush()

t1 = time()
print(f'took {(t1 - t0):.2f} seconds')