# firstNum = float(input("Введіть перше число: "))
# operation = input("Введіть операцію(+, -, * /): ")
# secondNum = float(input("Введіть друге число: "))

# print("Результат: ")

# if operation == "+":
#     print(firstNum + secondNum)
# elif operation == "-":
#     print(firstNum - secondNum)
# elif operation == "*":
#     print(firstNum * secondNum)
# elif operation == "/":
#     print(firstNum / secondNum)
# else:
#     print("Некоректна операція")

#! ================================================

# firstNum = float(input("Введіть перше число: "))
# operation = input("Введіть операцію(+, -, * /): ")
# secondNum = float(input("Введіть друге число: "))

# match operation:
#     case "+":
#         print(firstNum + secondNum)
#     case "-":
#         print(firstNum - secondNum)
#     case "*":
#         print(firstNum * secondNum)
#     case "/":
#         print(firstNum / secondNum)
#     case _:
#         print("Некоректна операція")

#! ================================================

# counter = 1

# print("До циклу")

# while counter <= 5:
#     print(counter)
#     # counter = counter + 1
#     counter += 1

# print("Після циклу")


'''
1. 
while 1 <= 5: true
    print(1)
    counter = 1 + 1 = 2
2. 
while 2 <= 5: true
    print(2)
    counter = 2 + 1 = 3
3. 
while 3 <= 5: true
    print(3)
    counter = 3 + 1 = 4
4. 
while 4 <= 5: true
    print(4)
    counter = 4 + 1 = 5
5. 
while 5 <= 5: true
    print(5)
    counter = 5 + 1 = 6
6. 
while 6 <= 5: false
   -----------

'''

#! ================================================

# userAge = int(input("Введіть свій вік: "))

# while userAge < 18:
#     userAge = int(input("Введіть свій вік більше 18: "))

# print("Ваш вік", userAge)

#! ================================================

# ADMIN_LOGIN = "admin"
# ADMIN_PASSWORD = "qwerty"

# login = input("Введіть ваш логін: ")

# if login == ADMIN_LOGIN:
#     password = input("Вітаю, введіть пароль адміну: ")
#     while password != ADMIN_PASSWORD:
#         password = input("Невірний пароль! Спробуйте ще раз: ")
#     print("Вітаю, адмін!")
# else:
#     print("Вітаю,", login)

#! ================================================

# while True:
#     print("hello")

#! ================================================

# word = "hello"

# for letter in word:
#     print(letter)

'''
1. for letter = "h" in word = "hello":
    print("h")
2. for letter = "e" in word = "hello":
    print("e")
3. for letter = "l" in word = "hello":
    print("l")
4. for letter = "l" in word = "hello":
    print("l")
5. for letter = "o" in word = "hello":
    print("o")

'''

#! ================================================

# for index in range(1, 11):
#     print(index)

'''
1. for index = 1 in range(1, 11):
    print(1)
2. for index = 2 in range(1, 11):
    print(2)
3. for index = 3 in range(1, 11):
    print(3)
.....
10. for index = 10 in range(1, 11):
    print(10)

'''

#! ================================================

# for index in range(1, 11, 3):
#     print(index)


'''
1. for index = 1 in range(1, 11, 3):
    print(1)

2. for index = 1 + 3 = 4 in range(1, 11, 3):
    print(4)

3. for index = 4 + 3 = 7 in range(1, 11, 3):
    print(7)

4. for index = 7 + 3 = 10 in range(1, 11, 3):
    print(10)

'''


#! ================================================

# for number in range(2, 15, 2):
#     if number % 4 != 0:
#         print(number)


# for number in range(2, 15, 2):
#     if number % 4 == 0:
#         continue
#     print(number)

'''
1. for number = 2 in range(2, 15, 2):
    if 2 % 4 == 0: false
        continue ---
    print(2)

2. for number = 4 in range(2, 15, 2):
    if 4 % 4 == 0: true
        continue 
        
3. for number = 6 in range(2, 15, 2):
    if 6 % 4 == 0: false
        continue ----
    print(6)
    


'''

#! ================================================

# sentence = "5i 5l5o5v5e5 5p5yt5ho5n5"
# correctSentence = ""

# for char in sentence:
#     if char == "5":
#         continue
#     correctSentence += char

# print(correctSentence)

#! ================================================

# sentence = "1i 4l5o2v0e6 8p7yt51ho28n9"
# correctSentence = ""

# for char in sentence:
#     if not char.isdigit():
#         correctSentence += char

# print(correctSentence)

#! ================================================

# print("До циклу")

# for number in range(1, 11):
#     if number == 0:
#         break
#     print(number)
# else:
#     print("У цьому діапазоні не має цифри 0!")

# print("Після циклу")

#! ================================================

'''
1. запитати у користувача 2 числа - 1 це початок діапазону циклу і 2 - це кінець діапазону
2. якщо користувач ввів 1 число більше ніж 2, то потрібно запитувати у нього 2ге число до тих пір, поки він не введе правильно(щоб 1 число було менше за 2)
3. запитати у користувача 3 число, яке ми шукаємо у діапазоні
4. запускаємо цикл і в кінці виводмо повідомлення чи є число 3 у діапазоні, чи його там немає
'''

# fromNumber = int(input("Введіть ліву сторону діапазону: "))
# toNumber = int(input("Введіть праву сторону діапазону: ")) + 1

# while fromNumber >= toNumber:
#     toNumber = int(
#         input("Невірно! Права сторона не може бути менша за ліву, спробуйте ще раз: ")) + 1

# searchNumber = int(input("Введіть число, яке ви хочете перевірити: "))

# for number in range(fromNumber, toNumber):
#     if searchNumber == number:
#         print("Число", searchNumber, "є у діапазоні")
#         break
# else:
#     print("Числа", searchNumber, "немає діапазоні")


#! ================================================

# ADMIN_LOGIN = "admin"
# ADMIN_PASSWORD = "qwerty"

# login = input("Введіть ваш логін: ")

# if login == ADMIN_LOGIN:
#     password = input("Вітаю, введіть пароль адміну: ")
#     for i in range(1, 4):
#         if password == ADMIN_PASSWORD:
#             print("Вітаю, адмін!")
#             break
#         attempt = 4 - i
#         print("Невірний пароль! Спробуйте ще раз(кількість спроб", attempt, "): ")
#         password = input()
#     else:
#         print("Ви ввели пароль неправильно 4 рази. Ваш акаунт заблоковано!")

# else:
#     print("Вітаю,", login)

#! ================================================

'''
1. користувач вводить якесь слово
2. користувач вводить букву, яку ми будемо шукати у слові
3. перевірити чи є буква у слові(якщо є, кажемо, так, якщо немає, кажемо ні)

'''

# word = input("Введіть слово: ")
# letter = input("Введіть букву, яку хочете перевірити: ")

# for char in word:
#     if letter == char:
#         print("Буква", letter, "є у слові", word)
#         break
# else:
#     print("Букви", letter, "у слові", word, "немає")

# ====

# if letter in word:
#     print("Буква", letter, "є у слові", word)
# else:
#     print("Букви", letter, "у слові", word, "немає")

#! ================================================

# вивести перші 200 непарних чисел у консоль
# не виводити числа, які кратні 5

# counter = 0

# for number in range(1, 200 * 2 + 100, 2):
#     if number % 5 == 0:
#         continue
#     print(number)
#     counter +=1

# print("Ось ваші перші", counter, "непарні числа, які не кратні 5")

'''
1. 1
2. 3
3. 5
4. 7
5. 9
6. 11
7. 13
8. 15
9. 17
10. 19
'''
