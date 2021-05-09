from __future__ import print_function
import paho.mqtt.publish as publish
import psutil
import string
import random
import serial

# The ThingSpeak Channel ID.
# Replace <YOUR-CHANNEL-ID> with your channel ID.
channelID = "1372729"

# The write API key for the channel.
# Replace <YOUR-CHANNEL-WRITEAPIKEY> with your write API key.
writeAPIKey = "SQ1W2OEJAD89C1RA"

# The hostname of the ThingSpeak MQTT broker.
mqttHost = "mqtt.thingspeak.com"

# You can use any username.
mqttUsername = "mwa0000022343692"

# Your MQTT API key from Account > My Profile.
mqttAPIKey = "RGCSPFB3RHEITJW4"

tTransport = "websockets"
tPort = 80

# Create the topic string.
topic = "channels/" + channelID + "/publish/" + writeAPIKey

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.flush()

while(1):

    line = ''

    line = ser.readline().decode('utf-8').rstrip()
    print(line)
    # build the payload string.
    payload = "field1=" + str(line)

    # attempt to publish this data to the topic.
    try:
        publish.single(topic, payload, hostname=mqttHost, transport=tTransport, port=tPort, auth={
                       'username': mqttUsername, 'password': mqttAPIKey})

    except (KeyboardInterrupt):
        break

    except:
        print("There was an error while publishing the data.")
