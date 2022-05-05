# Винятки. Генерація Винятків. Попередження.
# Except - Виняток, Помилка.
# Вся структура називається Капсула.
try: # Виконує Код.
    try:
        print("Start Code")
    except SyntaxError: # Виводить текст помилки.
        print("We have SyntaxError")
except NameError as error: # Виводить помилку.
    print(error)
else: # Якщо немає помилок.
    print("No problems")
finally: # Виконується на кінці 
    print("Finally Code")
# Кожну капсулу " Структуру " можна огорнути ще додатковую капсулою.

# Генерація винятків.
# raise яка примусова генерує виняток.
def checker(a):
    if type(a) != str:
        raise TypeError(f"Sorry, i can't work with {type(a)} , i need class str")
    else:
        print("Good")


b = 10
checker(b)

# Попередження - warnings
# Генерувати сповіщення можна за допомогою функції warn()
import warnings


warnings.simplefilter("ignore",SyntaxWarning)
warnings.simplefilter("error",ImportWarning)

warnings.warn("Warning, no code here", SyntaxWarning)



try:
    warnings.warn("Warning, library not import", ImportWarning)
except:
    print("Warning process!")