from tkinter import *
from tkinter import ttk
import pymysql
import threading
import time
# import Adafruit_DHT


class Database:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'admin'
        self.password = 'admin'
        self.dbname = '20mcmb08'
        try:
            self.db = pymysql.connect(
                self.host, self.user, self.password, self.dbname)
            print("[*] Database Connected.")
        except Exception as e:
            print("\n\n[**] Exception :: __init__ :: " + str(e))
            print('\n\n')
        self.db.autocommit(True)
        self.cursor = self.db.cursor()

    def fetch_all(self):
        SQL = "SELECT * FROM `dht`"
        try:
            self.cursor.execute(SQL)
            result = self.cursor.fetchall()
            print ('fetch_all: ',result)
            return result
        except Exception as e:
            print('\n[**] Database :: fetch_all :: ' + str(e))
            return None

    def add_new(self, temperature, humidity):
        SQL = "INSERT INTO `dht` (`id`, `time`, `temperature`, `humidity`) VALUES (NULL, NULL, '%s', '%s')"%(temperature,humidity)
        try:
            self.cursor.execute(SQL)
            print('add_new:',temperature,humidity)
        except Exception as e:
            print('\n[**] Exception :: add_new :: ' + str(e))


class Sensor:
    def __init__(self):
        self.control = None
        self.sensor_threat = None

        # Set sensor type : Options are DHT11,DHT22 or AM2302
        # self.sensor = Adafruit_DHT.DHT11
        
        # Set GPIO sensor is connected to
        self.gpio = 4

        self.db = Database()

    def sense(self):
        # TEST
        humidity=0
        temperature=0

        while self.control:
            try:
                time.sleep(1)

                # Use read_retry method. This will retry up to 15 times to
                # get a sensor reading (waiting 2 seconds between each retry).
                # humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.gpio)


                # TEST
                humidity+=0.7
                temperature+=0.7

                if humidity is not None and temperature is not None:
                    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
                else:
                    print('Failed to get reading. Try again!')

            except Exception as e:
                print ('Sense:',str(e))

    def start(self):
        self.control=True
        self.sensor_threat = threading.Thread(target=self.sense)
        self.sensor_threat.start()

    def stop(self):
        self.control=False
        self.sensor_threat.join()



s = Sensor()
s.start()
time.sleep(10)
s.stop()

class GUI:
    def __init__(self):
        # self.publisher = Publish()

        self.root = Tk()
        self.root.title('Problem 2')

        # create frame for start publishing
        self.pub_frame = LabelFrame(
            self.root, text='DB Store', padx=50, pady=50)
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
        # self.publisher.start()
        self.pub_prog.start(20)
        self.status_text.set('Started..')

    def stop_pub(self):
        print('Stop pub')
        # self.publisher.stop()
        self.pub_prog.stop()
        self.status_text.set('Stopped..')


# gui = GUI()
