from tkinter import *
from tkinter import ttk

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


def start_pub():
    print('Start pub')
    pub_prog.start(20)
    status_text.set('Started..')


def stop_pub():
    print('Stop pub')
    pub_prog.stop()
    status_text.set('Stopped..')


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
