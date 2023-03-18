# word = input("Введіть слово: ")
# user_letter = input("Введіть букву, яку ви хочете порахувати: ")

# counter = 0

# for letter in word:
#     if letter == user_letter:
#         counter += 1

# print("Буква", user_letter, "зустрічається", counter, "рази(-ів)")


#! ==============================================


# def print_message(msg):
#     # msg - параметр, це змінна, в яку зберігається якесь передане значення під час виклику ф-ції
#     print("Hello world!!!")
#     print(msg)


# print_message("THIS IS A STRING") # "" - аргумент ф-ції
# print_message(5 + 10)


# def some_number():
#     print("Ця функція вміє повертати цифру 5")
#     return 5


# num1 = 7
# num2 = some_number()

# print(num1 + num2)

#! ==============================================

# def count_letters(word, user_letter):
#     counter = 0

#     for letter in word:
#         if letter == user_letter:
#             counter += 1

#     print("Буква", user_letter, "зустрічається",
#           counter, "рази(-ів)", "у слові", word)

#     return counter


# smth = count_letters("hello", "l")
# print(smth)
# count_letters("laptop", "p")
# count_letters("rabbit", "d")
# count_letters("ранок", "а")
# count_letters(input(), input())


#! ==============================================

'''
1. створити 2 функції які просто повертають якесь число або цифру
2. створити 2 змінні в які зберегти результати виконання функцій
3. перемножити ці 2 змінні
'''

# def num5():
#     return 5


# def num10():
#     return 10


# x = num5()
# y = num10()

# print(x * y)

#! ==============================================

# string = "Hello world"

# print(len(string)) #length

'''
написати функцію, яка приймає строку і рахує її довжину без пробілів (вручну написати ф-цію len())
'''


# def count_str_length(string):
#     counter = 0
#     for char in string:
#         if char != " ":
#             counter += 1
#     return counter

# str1 = "Nice to meet you"
# print(count_str_length(str1))
# str2 = "    h  e  l  l  o    "
# print(count_str_length(str2))

#! ==============================================

# написати функцію, яка приймає строку, а повертає цю ж саму строку, але перевернуту
# hello -> olleh | rabbit -> tibbar

'''
1. отримати довжину строки
2. створення змінної, в яку ми будемо складувати перевернуте слово
3. запуск циклу і накопичення символів до нової змінної(задом наперед)
4. повернути нове слово
'''


# def reverse_string(string):
#     str_length = len(string) - 1
#     new_string = ""

#     for i in range(str_length + 1):
#         new_string += string[str_length - i]

#     return new_string


'''
1.  for 0 in range(5 не вкл):
        print(string[str_length - i]) -> string[4 - 0] -> string[4] -> o
2.  for 1 in range(5 не вкл):
        print(string[str_length - i]) -> string[4 - 1] -> string[3] -> l
3.  for 2 in range(5 не вкл):
        print(string[str_length - i]) -> string[4 - 2] -> string[2] -> l
4.  for 3 in range(5 не вкл):
        print(string[str_length - i]) -> string[4 - 3] -> string[1] -> e
5.  for 4 in range(5 не вкл):
        print(string[str_length - i]) -> string[4 - 4] -> string[0] -> h

'''

# print(reverse_string("hello"))
# print(reverse_string("rabbit"))
# print(reverse_string("hello world!"))

#! ==============================================

'''
напишіть функцію, яка приймає три параметри: перше число, друге число і знак("+", "-", "/", "*") і ця функція повертає результат математичної операції.

calculate(4, 3, "+") -> 7
calculate(3, 3, "*") -> 9
'''

# def calculate(num1, num2, operation):
#     result = 0

#     match operation:
#         case "+":
#             result = num1 + num2
#         case "-":
#             result = num1 - num2
#         case "*":
#             result = num1 * num2
#         case "/":
#             result = num1 / num2
    
#     return result
    

# print(calculate(4, 8, "*"))
# print(calculate(125, 53, "*"))
# print(calculate(459, 3, "/"))
# print(calculate(593, 345, "+"))

