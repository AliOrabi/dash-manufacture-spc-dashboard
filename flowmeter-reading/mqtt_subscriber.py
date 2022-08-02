import paho.mqtt.client as mqtt
import time
import datetime
import pandas as pd 
from pandas import json_normalize
import numpy as np
import json
import csv

t = datetime.datetime.now()
datetime = t.strftime("%D %H:%M")
MQTT_SERVER = "192.168.10.5" #M2M Sim ip
# MQTT_SERVER = "10.0.0.11"   #M2M ROuter IP
# MQTT_SERVER = "192.168.43.106" localnetwork ip
MQTT_PATH = "meter_01" 



# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH) 



# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg): 
    print(msg.topic + " , " + t.strftime("%D %H:%M") +  " , " + str(msg.payload.decode("utf-8").split(',')))
    # more callbacks, etc
    #print ('msg:', msg.payload.decode("utf-8"))
    
    flow = msg.payload.decode("utf-8")
    
    data = [{
        "datetime": t.strftime("%D %H:%M"), 
        "flow(puls)": flow
        }]
    df = pd.DataFrame(columns = ["datetime","flow(puls)"])
# append data to df
    df1 = [df.columns]
    for row,datetime,flow in zip(df1,df["datetime"],df["flow(puls)"]):
        
        row["datetime"] = datetime
        row["flow(puls)"] = flow
        data.append(row)
    data 
    df2 = pd.DataFrame(data).to_csv('data.csv', mode='a', index=True, header=False)
    df2

    #print(data)
    
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(MQTT_SERVER, 1883, 60)
 
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()