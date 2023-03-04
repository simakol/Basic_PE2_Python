# int - ціле число 69 42
# boolean - true/false
# none - нічого не означає
# string - строки "string"
# float - числа з плаваючою крапкою 1.5 44.59

# num1 = 4
# num2 = 15

# result = num1 < num2

# result = bool(-15)
# print(result)
# print(type(result))

'''
    True: будь-яке число(і додатні і відʼємні), крім 0 | будь-яка строка, крім пустої
    False: пуста строка | 0 | None
'''

# name = input("Введи своє імʼя: ")
# print("Привіт, ", name)

#! ================================================

# userNumber = float(input("Введи будь-яке число: "))

# '''
# if умова:
#     тіло моєї умови, якщо умова істинна, виконується тіло, якщо хибна, тіло не виконується
# '''

# if userNumber > 10:
#     print("Ваше число більше за 10")
# elif userNumber < 10:
#     print("Ваше число менше за 10")
# else:
#     print("Ваше число дорівнює 10")
# # elif userNumber == 10:
# #     print("Ваше число дорівнює 10")

# print("Ваше число: ", userNumber)

#! ================================================

# userNumber = int(input("Введіть число: "))
# remainder = userNumber % 2

# if userNumber == 0:
#     print("Ви ввели 0")
# elif remainder == 0:
#     print("Число", userNumber, "є парним")
# else:
#     print("Число", userNumber, "не є парним")

#! ================================================

'''
logical operators
- Логічне І - and - повертає перший false, якщо оператор не знайшов false, то він повертає останній елемент
- Логічне АБО - or - повертає перший true, якщо оператор не знайшов true, то він повертає останній елемент
- Логічне НІ - not - змінює логічний тип на зворотній, тобто, якщо був true, він зробить його false і навпаки
'''

# print(55 and 1 and None and "hello")
# print(0 or "" or False or "Hi there" or None)
# print(not not None)
# print(bool(None))

# print(0 or 1 and None)
# print("" or 0 and "hello" or 56 and 42)
'''
1. 0 and "hello" -> 0 -> "" or 0 or 56 and 42
2. 56 and 42 -> 42 -> "" or 0 or 42
3. "" or 0 or 42 -> 42
'''

# print("Hello world" and "I love python" or None and "Hi there")
'''
1. "Hello world" and "I love python" -> "I love python" -> "I love python" or None and "Hi there"
2. None and "Hi there" -> None -> "I love python" or None
3. "I love python" or None -> "I love python"
'''


#! ================================================

# print("Введи три числа: ")
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())

# '''
# 1. якщо num1 > num2 і num1 > num3 -> це значить, що num1 найбільше
# 2. якщо num2 > num1 і num2 > num3 -> це значить, що num2 найбільше
# 3. якщо num3 > num1 і num3 > num2 -> це значить, що num3 найбільше
# '''

# biggestNum = num1
# flag = True

# if num1 > num2 and num1 > num3:
#     biggestNum = num1
# elif num2 > num1 and num2 > num3:
#     biggestNum = num2
# elif num3 > num1 and num3 > num2:
#     biggestNum = num3
# else:
#     print("Неможливо визначити")
#     flag = False


# if flag:
#     print("Число", biggestNum, "є найбільшим")

#! ================================================

# print("Введи три числа: ")
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())

# numOrder1 = num1
# numOrder2 = num2
# numOrder3 = num3

# numberOfBiggest = "1"
# numberOfAvarage = "2"

# # це перевірка на найбільше число
# if num1 > num2 and num1 > num3:
#     numOrder1 = num1
#     numberOfBiggest = "1"
# elif num2 > num1 and num2 > num3:
#     numOrder1 = num2
#     numberOfBiggest = "2"
# elif num3 > num1 and num3 > num2:
#     numOrder1 = num3
#     numberOfBiggest = "3"

# # це перевірка на середнє число

# if numberOfBiggest == "1":
#     if num2 > num3:
#         numOrder2 = num2
#         numberOfAvarage = "2"
#     elif num3 > num2:
#         numOrder2 = num3
#         numberOfAvarage = "3"
# elif numberOfBiggest == "2":
#     if num1 > num3:
#         numOrder2 = num1
#         numberOfAvarage = "1"
#     elif num3 > num1:
#         numOrder2 = num3
#         numberOfAvarage = "3"
# elif numberOfBiggest == "3":
#     if num1 > num2:
#         numOrder2 = num1
#         numberOfAvarage = "1"
#     elif num2 > num1:
#         numOrder2 = num2
#         numberOfAvarage = "2"

# # це перевірка на останнє число
# if num1 < num2 and num1 < num3:
#     numOrder3 = num1
# elif num2 < num1 and num2 < num3:
#     numOrder3 = num2
# elif num3 < num1 and num3 < num2:
#     numOrder3 = num3


# print("Ось числа у порадку зростання:", numOrder3, numOrder2, numOrder1)

#! ================================================

cash = int(input("Внесіть кошти: "))
print("Виберіть напій: \n 1 - Лате (25 грн) \n 2 - Флет-вайт (50 грн) \n 3 - Китайський чай (10 грн)")
drink = int(input())
change = cash
sugarPrice = 2
flag = True

if drink == 1 and cash >= 25:
    change = cash - 25
    print("Насолоджуйтесь вашим лате, ось ваша решта -", change, "грн.")
elif drink == 2 and cash >= 50:
    change = cash - 50
    print("Насолоджуйтесь вашим флет-вайт, ось ваша решта -", change, "грн.")
elif drink == 3 and cash >= 10:
    change = cash - 10
    print("Насолоджуйтесь вашим китайським чаєм, ось ваша решта -", change, "грн.")
else:
    print("Недостаньо коштів, ось ваша решта -", change, "грн.")
    flag = False

if flag:
    sugarStatus = int(
        input("Чи бажаєте ви додати цукор? \n 1 - так \n 2 - ні \n"))
    if sugarStatus == 1:
        sugarAmount = int(
            input("Скільки цукру вам покласти? (1 кубік - 2 грн.)\n"))
        totalSugarPrice = sugarPrice * sugarAmount
        print("Ціна за", sugarAmount, "цукру =", totalSugarPrice, "грн.")
        if change < totalSugarPrice:
            change += int(input("Внесіть кошти: "))
            if change >= totalSugarPrice:
                change -= totalSugarPrice
                print("Дякуємо! Ми додали у ваш напій",
                      sugarAmount, "цукру. Ваша решта -", change, "грн.")
            else:
                print("Недостаньо коштів! Ваша решта -", change, "грн.")
        else:
            change -= totalSugarPrice
            print("Дякуємо! Ми додали у ваш напій",
                  sugarAmount, "цукру. Ваша решта - ", change)
    else:
        print("На все добре!")
