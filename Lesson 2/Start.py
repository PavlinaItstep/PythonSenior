# 1) Перший код.
from this import d


print('Hello World!')

first = 23
print(first)

second = "Number"
print(second)
# --------------
print(first,second)

# 2) Як проводити операції над числами.

a = 10 + 5
b = a + 20
c = ( a + b ) * 2
print(a,b,c)

# 3) Робота з рядками.

# 1. Імя змінної не може містити в собі пробіли.
# 2. Імя змінної не може починатися з числа.
# 3. Регістр для змінних важливий, тобто є ріниця між var i Var.

first_string = "Hello World!"
second_string = 'Hello World!'
third_string = """Hello World!"""

# 4) Під час створення Рядка, враховуються тільки перші лапки.

name = input('Ваше Імя?')
# greeting = переводиться як привітання.
# Для того щоб поєднати дві змінні в одну ( Одного типу ) використовуємо +
greeting = "Привіт, " + name

print(greeting)

# 5) Для того щоб вивести довжину слова використовуємо len(назва змінної)

string = input('Напишіть любий текст: ')

string_length = len(string)

print(string_length)

# 6) Типи данних. Перетворення типів.

result = 10 + 15

text = "1) Результат = " + str(result)
print(text)

# Для того щоб конвертувати любе значення в текст пишемо str(назва змінної)

result_2 = "10" + "15"
text_2 =  "2) Результат = " + result_2
print(text_2)

# Для того щоб конвертувати значення в число пишемо int(назва змінної)

a_2 = input("Перше число: ")
b_2 = input("Друге число: ")

result_3 = int(a_2) + int(b_2)

text_3 =  "4) Результат = " + str(result_3)
print(text_3)

# Логічна перевірка if + elif + else 

first_number = input("Перше число")
if int(first_number) == 0:
    print("Ділення на 0 не можливе.")
else:
    print("Ділення можливе.")

