from kafka import KafkaConsumer

consumer = KafkaConsumer('foobar')

for msg in consumer:
	print (msg)