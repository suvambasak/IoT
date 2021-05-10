# from __future__ import print_function
# import paho.mqtt.publish as publish
from tkinter import *
from tkinter import ttk
import time
import threading
# import psutil
# import string
# import random
# import serial

# ################# ThingSpeak Publish ################


# # The ThingSpeak Channel ID.
# # Replace <YOUR-CHANNEL-ID> with your channel ID.
# CHANNEL_ID = "1385093"

# # The write API key for the channel.
# # Replace <YOUR-CHANNEL-WRITEAPIKEY> with your write API key.
# WRITE_API_KEY = "ZGEK3NL0UVWPK3D6"

# # The hostname of the ThingSpeak MQTT broker.
# MQTT_HOST = "mqtt.thingspeak.com"

# # You can use any username.
# MQTT_USERNAME = "mwa0000022490756"

# # Your MQTT API key from Account > My Profile.
# MQTT_API_KEY = "8HQRSH6RX3BHT23Z"

# T_TRANSPORT = "websockets"
# T_PORT = 80

global control
control = True


def test():
    i = 0
    while control:
        print(i)
        i += 1
        time.sleep(2)


###################### GUI #########################
root = Tk()
root.title('Problem 1')

# create frame for start publishing
pub_frame = LabelFrame(root, text='MQTT Publish', padx=50, pady=50)
# frame.pack(padx=10, pady=10)
pub_frame.grid(row=0, column=0, padx=10, pady=10)

# Status View
status_text = StringVar()
status_text.set('Current Status')
status_view = Label(pub_frame, textvariable=status_text)
status_view.grid(row=0, column=0)

t = threading.Thread(target=test)


def start_pub():
    print('Start pub')
    pub_prog.start(20)
    status_text.set('Started..')
    global control
    control = True
    t.start()


def stop_pub():
    print('Stop pub')
    pub_prog.stop()
    status_text.set('Stopped..')
    global control
    control = False
    t.join()


# Progress bar
pub_prog = ttk.Progressbar(pub_frame, orient=HORIZONTAL,
                           length=150, mode='indeterminate')
pub_prog.grid(row=1, column=0, pady=20)

# adding button in publishing frame.
start = Button(pub_frame, text='Start', command=start_pub)
start.grid(row=2, column=0)
stop = Button(pub_frame, text='Stop', command=stop_pub)
stop.grid(row=3, column=0)


root.mainloop()
