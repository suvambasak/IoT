from tkinter import *
from tkinter import ttk
import time
import threading


class Publish:
    def __init__(self):
        self.control = None
        self.t = None

    def test(self):
        i = 0
        while self.control:
            print(i)
            i += 1
            time.sleep(0.5)

    def start(self):
        self.control = True
        self.t = threading.Thread(target=self.test)
        self.t.start()

    def stop(self):
        self.control = False
        self.t.join()


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
