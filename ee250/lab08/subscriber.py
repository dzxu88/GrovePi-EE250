
import paho.mqtt.client as mqtt
import time
def on_connect(client, userdata, flags, rc):

    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to the ultrasonic ranger topic here
    client.subscribe("ultrasonic_ranger1")
    client.subscribe("ultrasonic_ranger2")
    client.message_callback_add("ultrasonic_ranger1", ranger1_callback)
    client.message_callback_add("ultrasonic_ranger2", ranger2_callback)


#Default message callback. Please use custom callbacks.

def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload))

def ranger1_callback(client, userdata, message):
    #the third argument is 'message' here unlike 'msg' in on_message 
    print("custom_callback: " + message.topic + " " + str(message.payload, "utf-8"))

def ranger2_callback(client, userdata, message):
    #the third argument is 'message' here unlike 'msg' in on_message 
    print("custom_callback: " + message.topic + " " + str(message.payload, "utf-8"))


if __name__ == '__main__':
#this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.loop_start()

    while True:

        time.sleep(1)