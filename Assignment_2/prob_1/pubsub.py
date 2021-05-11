from __future__ import print_function
# import paho.mqtt.publish as publish

from tkinter import *
from tkinter import ttk
from urllib.request import urlopen
import json
import time
import threading

# import Adafruit_DHT

# import psutil
import string
import random
# import serial


class Publish:
    def __init__(self):
        self.control = None
        self.publisher_threat = None

        # Set sensor type : Options are DHT11,DHT22 or AM2302
        # self.sensor = Adafruit_DHT.DHT11
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

                time.sleep(5)

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


class Subscribe:
    def __init__(self):
        # self.URL = 'https://api.thingspeak.com/channels/1385704/feeds.json?results=1'

        # Test
        self.URL = 'https://api.thingspeak.com/channels/1385093/feeds.json?results=1'

    def fetch_update(self):
        with urlopen(self.URL) as url:
            data = json.loads(url.read().decode())

            # (Date,Time,Temperature,Humidity)
            return (
                data['feeds'][-1]['created_at'].split('T')[0],
                data['feeds'][-1]['created_at'].split('T')[1][:-1],
                data['feeds'][-1]['field1'],
                data['feeds'][-1]['field2']
            )
            # print(data['feeds'][-1])
            # print('Temp: ', data['feeds'][-1]['field1'])
            # print('Hume: ', data['feeds'][-1]['field2'])
            # print('Date: ', data['feeds'][-1]['created_at'].split('T')[0])
            # print('Time: ', data['feeds'][-1]['created_at'].split('T')[1])


# s = Subscribe()
# d = s.fetch_update()
# print(d[0])


class GUI:
    def __init__(self):
        self.publisher = Publish()
        self.subscriber = Subscribe()
        self.subscriber_thread = None
        self.control = None
        self.pub_flag = True
        self.sub_flag = True

        self.root = Tk()
        self.root.title('ThingSpeak - Problem 1')

        # create frame for start publishing
        self.pub_frame = LabelFrame(
            self.root, text='Publish', padx=61, pady=61)
        # frame.pack(padx=10, pady=10)
        self.pub_frame.grid(row=0, column=0, padx=10, pady=10)

        # create frame for subscribing
        self.sub_frame = LabelFrame(
            self.root, text='Subscribe', padx=30, pady=30)
        self.sub_frame.grid(row=0, column=1, padx=10, pady=10)

        # Status View publishing
        self.status_text = StringVar()
        self.status_text.set('Current Status')
        self.status_view = Label(self.pub_frame, textvariable=self.status_text)
        self.status_view.grid(row=0, column=0)

        # Status View subscrbe
        self.date_view = Label(self.sub_frame, text='Date')
        self.date_view.grid(row=0, column=0)
        self.time_view = Label(self.sub_frame, text='Time')
        self.time_view.grid(row=1, column=0)
        self.temperature_view = Label(self.sub_frame, text='Temperature')
        self.temperature_view.grid(row=2, column=0)
        self.humidity_view = Label(self.sub_frame, text='Humidity')
        self.humidity_view.grid(row=3, column=0)

        self.subscription_status_text = StringVar()
        self.subscription_status_text.set('Unsubscribed')
        self.subscription_status = Label(
            self.sub_frame, textvariable=self.subscription_status_text, anchor=W)
        self.subscription_status.grid(row=4, column=0)

        # Data view
        self.date = Entry(self.sub_frame)
        self.date.grid(row=0, column=1)
        self.time = Entry(self.sub_frame)
        self.time.grid(row=1, column=1)
        self.temperature = Entry(self.sub_frame)
        self.temperature.grid(row=2, column=1)
        self.humidity = Entry(self.sub_frame)
        self.humidity.grid(row=3, column=1)

        self.date.insert(0, 'xxxx-xx-xx')
        self.time.insert(0, 'xx:xx:xx')
        self.temperature.insert(0, 'xx.x')
        self.humidity.insert(0, 'xx.x')

        # Progress bar publishing
        self.pub_prog = ttk.Progressbar(self.pub_frame, orient=HORIZONTAL,
                                        length=150, mode='indeterminate')
        self.pub_prog.grid(row=1, column=0, pady=20)

        # Progress bar subscribing
        self.sub_prog = ttk.Progressbar(self.sub_frame, orient=HORIZONTAL,
                                        length=150, mode='indeterminate')
        self.sub_prog.grid(row=4, column=1, pady=20, columnspan=2)

        # adding button in publishing frame.
        self.start = Button(self.pub_frame, text='Start',
                            command=self.start_pub)
        self.start.grid(row=2, column=0)
        self.stop = Button(self.pub_frame, text='Stop', command=self.stop_pub)
        self.stop.grid(row=3, column=0)

        # adding button in subscribe frame.
        self.sub = Button(self.sub_frame, text='Subscribe',
                          command=self.start_sub)
        self.sub.grid(row=5, column=0)
        self.cancel = Button(self.sub_frame, text='Unsubscribe',
                             command=self.stop_sub)
        self.cancel.grid(row=5, column=1)

        self.root.mainloop()

    def loader(self):
        while self.control:
            current_state = self.subscriber.fetch_update()
            print(current_state)

            self.date.delete(0, END)
            self.date.insert(0, current_state[0])

            self.time.delete(0, END)
            self.time.insert(0, current_state[1])

            self.temperature.delete(0, END)
            self.temperature.insert(0, current_state[2])

            self.humidity.delete(0, END)
            self.humidity.insert(0, current_state[3])

            time.sleep(3)

    def start_sub(self):
        if self.sub_flag:
            self.sub_flag = False
            print('Start sub')

            self.control = True
            self.subscriber_thread = threading.Thread(target=self.loader)
            self.subscriber_thread.start()

            self.sub_prog.start(10)
            self.subscription_status_text.set('Subscribed')

    def stop_sub(self):
        if not self.sub_flag:
            self.sub_flag = True
            print('Stop sub')

            self.control = False
            # self.subscriber_thread.join()

            self.sub_prog.stop()
            self.subscription_status_text.set('Unsubscribed')

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


GUI()
