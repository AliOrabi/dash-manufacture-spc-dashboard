from multiprocessing.connection import Client
import paho.mqtt.client as mqtt

from mqtt_subscriber import MQTT_PATH, on_connect, on_message 
MQTT_SERVER = "localhost"


# Callbacks
def on_connect (client, userdata, flags, rc):
    print ('Connected with code :' + str(rc))
    # Subscrib Topic
    client.subscribe("Test/#1", "Test/#2")

def on_message(client, userdata, msg):
    print (str(msg.payload))




client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect('14a46948bb724f76b8bdc68c3aab3870.s1.eu.hivemq.cloud', 8883, 60)
client.loop_forever()