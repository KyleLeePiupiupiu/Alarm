from tkinter import *
import datetime
import time
import winsound

def alarm(setTimer):
    while True:
        time.sleep(1)
        nowTime = datetime.datetime.now()
        now = nowTime.strftime('%H:%M:%S')
        date = nowTime.strftime("%d/%m/%Y")
        print('The Set Date is:', date)
        print(now)

        if now == setTimer:
            print("It's time")


        winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
        break

def actualTime():
    setTimer = f"{hour}:{min}:{sec}"
    alarm(setTimer=setTimer)

        

if __name__ == '__main__':

    clock = Tk()
    clock.title('Alarm Clock')
    clock.geometry('400x100')
    timeFormat = Label(clock, text='Hour   Min   Sec', font=60).place(x=200)
    addTime = Label(clock, text='When to wake up', fg='blue', relief='solid').place(x=0, y=29)

    # variable for setting alarm
    hour = StringVar()
    min = StringVar()
    sec = StringVar()

    # set alarm time
    hour = Entry(clock, textvariable=hour, bg='pink', width=15).place(x = 200, y = 20)
    min = Entry(clock, textvariable=min, bg = 'pink', width=15).place(x = 240, y = 20)
    sec = Entry(clock, textvariable=sec, bg='pink', width=15).place(x=280, y=20)

    # take the time input 
    submit = Button(clock, text='set alarm', fg='red', width=10, command=actualTime).place(x = 200, y = 70)


    clock.mainloop()

