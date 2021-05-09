from __future__ import print_function
import paho.mqtt.publish as publish

print('Fix start')


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
mqttAPIKey = "RGCSPFB3RHEITJW4"

tTransport = "websockets"
tPort = 80


# Create the topic string.
topic = "channels/" + channelID + "/publish/" + writeAPIKey
counter = 100

while True:
    counter += 10
    print(counter)

    # build the payload string.
    payload = "f1=" + str(counter)

    # attempt to publish this data to the topic.
    try:
        publish.single(topic, payload, hostname=mqttHost, transport=tTransport, port=tPort, auth={
                       'username': mqttUsername, 'password': mqttAPIKey})

    except (KeyboardInterrupt):
        break

    except:
        print("There was an error while publishing the data.")
