from tkinter import *
from tkinter import ttk
import pymysql


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


gui = GUI()
