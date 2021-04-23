import tkinter as tk
from pynput.keyboard import Controller
import time
import pyautogui


def beg():
    for char in "pls beg":
        keyboard = Controller()
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.1)


def dep():
    for char in "pls dep all":
        keyboard = Controller()
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.1)


def begRepeatFunc():
    beg()
    pyautogui.press('enter')
    time.sleep(5)
    dep()
    pyautogui.press('enter')
    time.sleep(45)


number = 0


def begRepeat():
    global number
    ammount = int(EntryBoxTwo.get())
    while True:
        if number < ammount:
            begRepeatFunc()
            number += 1
            if number == ammount:
                break


def begWithTimer():
    while True:
        global number
        timeAmmountSecs = float(EntryBox.get())
        timeAmmountMins = timeAmmountSecs * 60

        time.sleep(5)
        begRepeat()
        number = 0
        time.sleep(timeAmmountMins)


def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


def themeCheckNotice():
    fileOpen = open("LaunchType.txt", "r")

    read_file = fileOpen.read()

    fileOpen.close()

    if read_file == 'Light':
        root.config(bg='#FFFFFF')

        Label1.config(bg='#FFFFFF', fg='#000000')
        Label2.config(bg='#FFFFFF', fg='#000000')

        Button1.config(bg='#FFFFFF', fg='#000000')

    if read_file == 'Dark':
        root.config(bg='#000000')

        Label1.config(bg='#000000', fg='#FFFFFF')
        Label2.config(bg='#000000', fg='#FFFFFF')

        Button1.config(bg='#141414', fg='#FFFFFF')


def themeCheck():
    fileOpen = open("LaunchType.txt", "r")

    read_file = fileOpen.read()

    fileOpen.close()

    if read_file == 'Light':
        master.config(bg='#FFFFFF')

        topLabel.config(bg='#FFFFFF', fg='#000000')
        ammount.config(bg='#FFFFFF', fg='#000000')
        StartLabel.config(bg='#FFFFFF', fg='#000000')

        EntryBox.config(bg='#FFFFFF', fg='#000000')
        EntryBoxTwo.config(bg='#FFFFFF', fg='#000000')

        begger.config(bg='#FFFFFF', fg='#000000')
        themeButton.config(bg='#FFFFFF', fg='#000000')

    if read_file == 'Dark':
        master.config(bg='#000000')

        topLabel.config(bg='#000000', fg='#FFFFFF')
        ammount.config(bg='#000000', fg='#FFFFFF')
        StartLabel.config(bg='#000000', fg='#FFFFFF')

        EntryBox.config(bg='#141414', fg='#FFFFFF')
        EntryBoxTwo.config(bg='#141414', fg='#FFFFFF')

        begger.config(bg='#141414', fg='#FFFFFF')
        themeButton.config(bg='#141414', fg='#FFFFFF')


def themeChange():
    openFile = open("LaunchType.txt", 'r')

    readfile = openFile.read()

    openFile.close()

    if readfile == 'Dark':
        openFileNew = open('LaunchType.txt', 'w')
        openFileNew.write('Light')
        openFileNew.close()
        themeCheck()

    elif readfile == 'Light':
        openFileNewTwo = open('LaunchType.txt', 'w')
        openFileNewTwo.write('Dark')
        openFileNewTwo.close()
        themeCheck()


root = tk.Tk()
root.title(' ')
root.geometry('250x100')

Label1 = tk.Label(root, text='Notice:', font=('TkDefaultFont', 18, 'bold'))
Label1.pack()

Label2 = tk.Label(root, text='Please force quit the application when\n you want to stop the bot.')
Label2.pack()

Button1 = tk.Button(root, text='Close', command=root.destroy)
Button1.pack()

center(root)
themeCheckNotice()

root.mainloop()

master = tk.Tk()

master.title("Discord Begger v2")
master.geometry("325x215")

topLabel = tk.Label(master, text="Enter time between each period \nof bot spams. (minutes)")
topLabel.pack()

EntryBox = tk.Entry(master, highlightthickness=0)
EntryBox.pack()

ammount = tk.Label(master, text="Ammount of begs and deps")
ammount.pack()

EntryBoxTwo = tk.Entry(master, highlightthickness=0)
EntryBoxTwo.pack()

StartLabel = tk.Label(master, text="Press Start below for the bot to start.")
StartLabel.pack()

begger = tk.Button(master, text="Start", command=begWithTimer)
begger.pack()

themeButton = tk.Button(text='Swap \nTheme', command=themeChange)
themeButton.pack()

center(master)
themeCheck()

master.mainloop()
