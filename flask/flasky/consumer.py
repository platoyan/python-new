# coding: utf-8
from kafka import KafkaConsumer
consumer = KafkaConsumer('test')
for msg in consumer:
	print((msg.value).decode('utf8'))
