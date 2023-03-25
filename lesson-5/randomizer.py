import tkinter as tk
import random


def getRandomInt(min, max):
    return random.randint(min, max)

def getRandomFloat(min, max):
    return float('{:3f}'.format(random.uniform(min, max)))


def updateNumber():
    min = int(minNum.get())
    max = int(maxNum.get())
    if min >= max: 
        randNumLabel["text"] = "Помилка!"
    else: 
        randNumLabel["text"] = getRandomInt(min, max)


window = tk.Tk()

window.title("Згенеруй випадкове число!")

window.geometry("400x250+500+250")

window.resizable(0, 0)

window.configure(bg="#05C3DD")

randNumLabel = tk.Label(text="Ваше число", bg="#05C3DD",
                        fg="yellow", font="Verdana 50 bold")
randNumLabel.pack()

minNum = tk.StringVar()
maxNum = tk.StringVar()

entryMin = tk.Entry(textvariable=minNum)
entryMax = tk.Entry(textvariable=maxNum)

entryMin.insert(0, "Мінімальне число")
entryMax.insert(0, "Максимальне число")

entryMin.pack(pady=10)
entryMax.pack()


button = tk.Button(text="Згенерувати число", bg="#05C3DD",
                   font="Verdana 20", bd="0", padx="10", pady="8", command=updateNumber)
button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

window.mainloop()
