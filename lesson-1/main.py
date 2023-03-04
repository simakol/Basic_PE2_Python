# print("Hello world! 111")

'''
number = 10

print(number)

number = 5

print(number)

MAIN_NUMBER = 1

print(MAIN_NUMBER)

MAIN_NUMBER = 15

print(MAIN_NUMBER)
'''

'''
num_1 = 10
num_2 = 5

print(num_1 + num_2)
print(num_1 * num_2)
print(num_1 - num_2)
print(num_1 / num_2)
print(num_2 ** 5)
print(10 % 3) # 9 / 3 = 3 -> 10 - 9 = 1
print(15 % 4) # 12 / 4 = 3 -> 15 - 12 = 3

print(15 > 2) # True
print(15 < 2) # False
print(10 >= 10) # True 
print(10 > 10) # False
print(10 <= 10) # True
print(10 == 10) # True
print(9 == 10) # False

'''

user_age = 28  # Integer (int) - цілочисельний тип даних
user_height = 1.90  # Float - тип даних чисел з плаваючою точкою(дробові числа)
user_name = "Oleg"  # String - строковий тип даних

# print(2 * user_name)

# Boolean (Bool) - логічний тип даних, зберігає тільки два значення: True(правда) або False(неправда)
is_user_play_games = True
# is_user_play_games = False

user_city = None  # NoneType - означає нічого

# type() - перевіряє тип даних змінної або значення

'''
   str() - змінює тип даних на строку | type conversion function to string(type str)
   float() - змінює тип даних на число з плаваючою крапкою
   int() - змінює тип даних на ціле число
    bool() - змінює тип даних на логічний тип
'''

# print(user_age)
# print(type(user_age))

# user_age = float(user_age)

# print(user_age)
# print(type(user_age))

# num = "10"

# print(type(num))
# num = int(num)
# print(type(num))

# print(num + 5)

# print(bool(None))

'''
    True: будь-яке число(і додатні і відʼємні), крім 0 | будь-яка строка, крім пустої
    False: пуста строка | 0 | None
'''

user_name = input("Напиши своє імʼя: ")
user_age = input("Напиши свій вік: ")
user_city = input("Напиши своє місто: ")
is_user_play_games = bool(
    int(input("Чи граєш ти в ігри? (1 - граю, 0 - не граю): ")))

# "1" -> True | bool("1") -> true | int("1") -> 1 -> bool(1) -> True
# "0" -> False | bool("0") -> true | int("0") -> 0 -> bool(0) -> False


print("========================================")

print("Привіт, " + user_name + "! Раді вас вітати!")
print("Тобі " + user_age + " років!")
print("Твій рік народження: ", 2023 - int(user_age))
print("Ти живеш у місті " + user_city)
print("Статус гравця: ", is_user_play_games)
