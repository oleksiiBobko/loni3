from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers="c515bvsddmq01.int.thomsonreuters.com:9092")
# producer = KafkaProducer(bootstrap_servers="localhost:9092")


my_file = open("mrsp_events_rics.txt.big", "r")
rics = my_file.readlines()
rics = [ric.rstrip() for ric in rics]
for i in range(5):
    for r in rics:
        msg = "{\"tag\":\"1\",\"permId\":\"123\",\"ric\":\"" + r + "\",\"tradeDate\":\"2021-10-04\",\"changeTime\":\"2021-10-04T12:54:47Z\",\"transCode\":\"I\",\"pubStatus\":\"U\",\"tradeIndicator\":\"H\",\"data\":[]}"
        producer.send(topic = "ETSInterTSHistoryChanges", value = bytes(msg, "utf8"))
    producer.flush()