from kafka import KafkaProducer
import json
from json import dumps

p = KafkaProducer(bootstrap_servers = ['broker:29092'], value_serializer = lambda x:dumps(x).encode('utf-8'))

with open('data/0.json', 'r') as file:
    data = json.load(file)

p.send('Data.data', value = data)

p.flush()