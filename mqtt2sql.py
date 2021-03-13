#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 21:35:34 2021

@author: kyrsjo
"""


#pip install paho-mqtt
import paho.mqtt.client as mqtt

def on_connect(client,userdata,flags,rc):
    print("Connected with result code "+str(rc))
    
    #client.subscribe("$SYS/#")
    client.subscribe("plants_kitchen/#")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

if __name__ == "__main__":
    print("In __main__, setting up MQTT connection...")
    client = mqtt.Client()
    
    client.on_connect = on_connect;
    client.on_message = on_message;
    
    client.connect("192.168.1.100")
    
    print("Looping forever!")
    client.loop_forever()