import datetime
import random
import time
import tkinter as tk


from tkinter import END

from keyDictionary import keyDictionary
from textList import textList


class KeyboardClass(tk.Tk):
    def __init__(self):
        self.key = tk.Tk()
        self.key.title('LightningTyper')
        self.key.iconbitmap('keyboard.ico')

        self.key.geometry('1086x253')
        self.key.maxsize(width=1086, height=253)
        self.key.minsize(width=1086, height=253)

        self.key.configure(bg='#DED9C4')
        self.wordcount = 0
        self.Dis_entry = tk.Entry(self.key, readonlybackground="#FBF3E4", fg="grey",
                                  font=("Helvetica", 15, "bold"))
        self.text = random.choice(textList)
        print(self.text)
        self.Dis_entry.insert(0, self.text)
        self.Dis_entry.configure(state='readonly')
        self.Dis_entry.grid(rowspan=1, columnspan=100, ipadx=1000, ipady=20)
        self.label = tk.Label(text=f"{self.wordcount} WPM,", bg="#FBF3E4", fg="#7FC8A9",
                              font=("Helvetica", 13, "bold"))
        self.label.grid(row=0, column=12,columnspan=1,sticky="EW")
        self.label2 = tk.Label(text=f"{self.wordcount} %", bg="#FBF3E4", fg="#7FC8A9",
                               font=("Helvetica", 13, "bold"))
        self.label2.grid(row=0,columnspan=1, column=13,sticky="EW")
        self.totalCount = 0
        self.start_time = 0.0
        self.buttonList = []
        self.firstLetter = 0
        self.createKeys()
        self.key.mainloop()

    def update(self, btn, param):
        print("update")
        btn.config(bg="#96C7C1")
        self.totalCount += 1
        if self.totalCount == 1:
            self.start_time = datetime.datetime.now()

        print(f"{param.char} pressed")
        if self.text=="":
            self.text = random.choice(textList)
            self.Dis_entry.configure(state='normal')
            self.Dis_entry.delete(0, END)  # deletes the current value
            self.Dis_entry.insert(0, self.text)
            self.Dis_entry.configure(state='readonly')
            self.label.config(text=f"0 WPM,")
            self.totalCount=0
            self.wordcount=0
            self.label2.config(text="100%")
        else:
            if param.char == self.text[0].lower():
                self.wordcount += 1
                self.text = self.text[1:]
                self.Dis_entry.configure(state='normal')
                self.Dis_entry.delete(0, END)  # deletes the current value
                self.Dis_entry.insert(0, self.text)
                self.Dis_entry.configure(state='readonly')

            end_time = datetime.datetime.now()
            time_elapsed = (end_time - self.start_time).seconds
            self.label.config(text=f"{round((self.wordcount / 5) / (time_elapsed / 60))} WPM,")

            self.label2.config(text=f"{round((self.wordcount / self.totalCount) * 100, 1)}%")

            print(time_elapsed)


    def press(self, param, btn, event=None):

        print(btn)
        btn.config(bg="grey")
        btn.after(60, self.update, btn, param)

    def createKeys(self):
        for item in keyDictionary:
            row = keyDictionary[item]["row"]
            col = keyDictionary[item]["column"]
            padx = keyDictionary[item]["ipadx"]
            pady = keyDictionary[item]["ipady"]
            sticky = keyDictionary[item]["sticky"]
            if item == "Enter" or item == "Space":
                q = tk.Button(self.key, text=f"{item}", bg="#96C7C1", fg="white", font=("Helvetica", 10, "bold"),
                              width=keyDictionary[item]["width"],
                              command=lambda: self.press('Q', q), bd=1)
                q.grid(row=row, columnspan=col, ipadx=padx, ipady=pady, sticky=sticky)
                self.key.bind(f"{keyDictionary[item]['key']}", lambda params=f"{item}", btn=q: self.press(params, btn))

                self.buttonList.append(q)
            else:
                q = tk.Button(self.key, text=f"{item}", bg="#96C7C1", fg="white", font=("Helvetica", 10, "bold"),
                              width=6,
                              command=lambda: self.press('Q', q), bd=1)
                q.grid(row=row, column=col, ipadx=padx, ipady=pady, sticky=sticky)

                self.key.bind(f"{keyDictionary[item]['key']}", lambda params=f"{item}", btn=q: self.press(params, btn))

                self.buttonList.append(q)
