from kafka import KafkaProducer

producer = KafkaProducer()#bootstrap_servers='localhost:9092')

for i in range(5):
	producer.send('foobar', b'Hello World')
	producer.flush()
	#producer.send('foobar', b'Hello World').get(timeout=30)