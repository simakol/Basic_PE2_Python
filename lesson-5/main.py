import random
import tkinter as tk

# randNumber = random.randint(-10, 10)  # [-10, 10]

# print(randNumber)

# def getRandInt(min, max):
#     return random.randint(min, max)

# print(getRandInt(10, 100))
# print(getRandInt(1, 5))
# print(getRandInt(-10, 0))
# print(getRandInt(500, 1000))


def handleClick():
    label["text"] = message.get()


window = tk.Tk()  # створення головного елементу інтерфейсу - вікна програми
window.title("Заголовок програми!")  # створюємо заголовок вікна програми
# задаємо розміри і позицію вікна - 400x200 - розміри 400 - ширина, а висота - 200. 300+300 - це позиція на екрані монітору(відступи по осі x і по осі у)
window.geometry("400x200+500+300")

window.resizable(0, 0)  # забороняємо зміну розмірів вікна

window.configure(bg="black")

text = tk.Label(text="Hello world!", bg="black",
                fg="lime", font="Arial 40 bold")  # створення текстової мітки (звичайного тексту) з налаштуваннями

text.pack()  # метод для розміщення елементів на вікні

message = tk.StringVar()  # контейнер для тексту
entry = tk.Entry(textvariable=message)  # поле вводу тексту

entry.pack()
# entry.place(relx=0.7, rely=0.2, anchor=tk.CENTER) # розміщуємо елемент на вікні за координатами, x/y - від 0 до 1(0 - сама ліва або сама верхня сторона, 1 - сама права або сама нижня сторона), anchor - це точка на елементі, за якою ми будемо розміщувати

label = tk.Label(text="ваш текст тут", fg="green")
label.pack()

button = tk.Button(text="Оновити", command=handleClick)  # кнопка
button.pack()

window.mainloop()  # нескінченний цикл, який не дасть нашому вікну закритись
