from __future__ import print_function
import paho.mqtt.publish as publish

from tkinter import *
from tkinter import ttk
import time
import threading

import Adafruit_DHT

import psutil
import string
import random
import serial


class Publish:
    def __init__(self):
        self.control = None
        self.publisher_threat = None

        # Set sensor type : Options are DHT11,DHT22 or AM2302
        self.sensor = Adafruit_DHT.DHT11
        # Set GPIO sensor is connected to
        self.gpio = 4

        # The ThingSpeak Channel ID.
        # Replace <YOUR-CHANNEL-ID> with your channel ID.
        self.CHANNEL_ID = "1385704"

        # The write API key for the channel.
        # Replace <YOUR-CHANNEL-WRITEAPIKEY> with your write API key.
        self.WRITE_API_KEY = "JXMONKXBE6TT13RA"

        # The hostname of the ThingSpeak MQTT broker.
        self.MQTT_HOST = "mqtt.thingspeak.com"

        # You can use any username.
        self.MQTT_USERNAME = "mwa0000022490756"

        # Your MQTT API key from Account > My Profile.
        self.MQTT_API_KEY = "8HQRSH6RX3BHT23Z"

        self.T_TRANSPORT = "websockets"
        self.T_PORT = 80

        # Create the topic string.
        self.TOPIC = "channels/" + self.CHANNEL_ID + "/publish/" + self.WRITE_API_KEY

    def push_data(self):
        while self.control:
            try:
                # Use read_retry method. This will retry up to 15 times to
                # get a sensor reading (waiting 2 seconds between each retry).
                humidity, temperature = Adafruit_DHT.read_retry(
                    self.sensor, self.gpio)

                if humidity is not None and temperature is not None:
                    print(
                        'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
                else:
                    print('Failed to get reading. Try again!')
                    continue

                # build the payload string.
                payload = "field1=" + str(temperature)+"&field2="+str(humidity)

                # attempt to publish this data to the topic.
                publish.single(self.TOPIC, payload, hostname=self.MQTT_HOST, transport=self.T_TRANSPORT, port=self.T_PORT, auth={
                               'username': self.MQTT_USERNAME, 'password': self.MQTT_API_KEY})

            except Exception as e:
                print(e)

    def test(self):
        i = 0
        while self.control:
            print(i)
            i += 1
            time.sleep(0.5)

    def start(self):
        self.control = True
        # self.publisher_threat = threading.Thread(target=self.test)
        self.publisher_threat = threading.Thread(target=self.push_data)
        self.publisher_threat.start()

    def stop(self):
        self.control = False
        self.publisher_threat.join()


class GUI:
    def __init__(self):
        self.publisher = Publish()

        self.root = Tk()
        self.root.title('Problem 1')

        # create frame for start publishing
        self.pub_frame = LabelFrame(
            self.root, text='MQTT Publish', padx=50, pady=50)
        # frame.pack(padx=10, pady=10)
        self.pub_frame.grid(row=0, column=0, padx=10, pady=10)

        # Status View
        self.status_text = StringVar()
        self.status_text.set('Current Status')
        self.status_view = Label(self.pub_frame, textvariable=self.status_text)
        self.status_view.grid(row=0, column=0)

        # Progress bar
        self.pub_prog = ttk.Progressbar(self.pub_frame, orient=HORIZONTAL,
                                        length=150, mode='indeterminate')
        self.pub_prog.grid(row=1, column=0, pady=20)

        # adding button in publishing frame.
        self.start = Button(self.pub_frame, text='Start',
                            command=self.start_pub)
        self.start.grid(row=2, column=0)
        self.stop = Button(self.pub_frame, text='Stop', command=self.stop_pub)
        self.stop.grid(row=3, column=0)

        self.root.mainloop()

    def start_pub(self):
        print('Start pub')
        self.publisher.start()
        self.pub_prog.start(20)
        self.status_text.set('Started..')

    def stop_pub(self):
        print('Stop pub')
        self.publisher.stop()
        self.pub_prog.stop()
        self.status_text.set('Stopped..')


gui = GUI()
