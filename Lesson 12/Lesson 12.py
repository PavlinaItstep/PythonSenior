# Логування. Ковігурування логування. Тести.

import logging

# 1. DEBUG - найнижчий рівень налаштування. Найчастіше використовується розробниками бібліотек.
# 2. INFO - рівень інформування. Він створенний для надання повідомлень про коректну роботу компонентів програми.
# 3. WARNING - рівень застережень, які повідомляють користувачу про можливу неправильну -
# роботу програми або надають важливу інформацію.
# 4. ERROR - рівень, помилок, які сповіщають про неправильну роботу функції або якогось кусочка коду.
# 5. CRITICAL - рівень критичних помилок, що інформує про серйозний -
# збій роботи програми, через який її виконання зупинене.

# Налаштування конфігурації потрібно робити на початку програми.
# filename - рядок з шляхом до файлу. Логі заведено зберігати в спеціальний текстовий файл .log
# filemode - режим відкриття файлу. "a" - режим на дозаписування тексту. "w" - режим на перезапис тексту.
# format - відповідає за форматування запису в файлик.
logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="w",format="We have next logging message:%(asctime)s:%(levelname)s-%(message)s")
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")

try:
    print(10/0)
except Exception:
    logging.exception("Exception")

assert 2+2 == 5, "wrong assert"

# Доктести

"""
>>> 2+2
5
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()