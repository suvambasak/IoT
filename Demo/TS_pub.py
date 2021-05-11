from __future__ import print_function
import paho.mqtt.publish as publish
import psutil
import string
import random
import serial

import random
import time

# The ThingSpeak Channel ID.
# Replace <YOUR-CHANNEL-ID> with your channel ID.
channelID = "1385093"

# The write API key for the channel.
# Replace <YOUR-CHANNEL-WRITEAPIKEY> with your write API key.
writeAPIKey = "ZGEK3NL0UVWPK3D6"

# The hostname of the ThingSpeak MQTT broker.
mqttHost = "mqtt.thingspeak.com"

# You can use any username.
mqttUsername = "mwa0000022490756"

# Your MQTT API key from Account > My Profile.
mqttAPIKey = "8HQRSH6RX3BHT23Z"

tTransport = "websockets"
tPort = 80

# Create the topic string.
topic = "channels/" + channelID + "/publish/" + writeAPIKey

# ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
# ser.flush()
counter = 100
while(1):

    line = random.randint(0, 50)
    counter = random.randint(0, 50)

    # line = ser.readline().decode('utf-8').rstrip()
    print(line,counter)
    # build the payload string.
    payload = "field1=" + str(line)+"&field2="+str(counter)

    # attempt to publish this data to the topic.
    try:
        publish.single(topic, payload, hostname=mqttHost, transport=tTransport, port=tPort, auth={
                       'username': mqttUsername, 'password': mqttAPIKey})
        time.sleep(5)
    except (KeyboardInterrupt):
        break

    except:
        print("There was an error while publishing the data.")
