import paho.mqtt.client as mqtt
import time
message="hello"
i=0

def on_connect(mosq, obj, rc):
    mqttc.subscribe("/test/topic", 0)
    print("rc: " + str(rc))
    print "hello connect"

def on_message(mosq, obj, msg):
    global message
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    message = msg.payload
    print "hello msg"
    

def on_publish(mosq, obj, mid):
    print("mid: arya" + str(mid))
    print "hello pub"

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))
    print "hello sub"

mqttc = mqtt.Client()
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
# Connect
mqttc.username_pw_set("fcfvaydb", password="MmIWxonlCM7u")
mqttc.connect("m12.cloudmqtt.com",11523 ,60)



while True:
    #print "hello"
    #mqttc.publish("/test/topic",i)
    time.sleep(1)
    #print i
    #i=i+1
