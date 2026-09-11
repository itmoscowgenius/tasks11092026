from tkinter import *
from tkinter import ttk

clicks = 0

def click_button():
    global clicks
    clicks += 1
    bin["text"] = f" Clicks {clicks}"

root = Tk()
root.title("Тестовое приложение")
root.geometry("1000x500")

btn = ttk.Button(text = "Кликни", command = click_button)
btn.pack()

root.mainloop()