---
date: 
tags: 
authors: GB

Abstract:  
---
# [Модуль sys](zotero://open-pdf/library/items/NW29V7HX?page=19&annotation=7PD86A79)

модуль sys — стандартный модуль Python, предоставляющий доступ к системным параметрам и функциям, взаимодействующим с интерпретатором. Содержит переменные и функции для работы со средой выполнения, командной строкой, потоками ввода-вывода и внутренним состоянием интерпретатора.

## Аргументы командной строки

> **<span style="color: green">sys.argv</span>** — список аргументов командной строки, переданных скрипту. Первый элемент argv[0] — имя скрипта (путь к файлу). В интерактивной оболочке содержит пустую строку.

```python
import sys
# При запуске: python script.py -v file.txt
print(sys.argv)  
# ['script.py', '-v', 'file.txt']
# Пример обработки аргументов
if len(sys.argv) > 1:
    filename = sys.argv[1]
    print(f"Обрабатываем файл: {filename}")
```

## Завершение программы

> **<span style="color: green">sys.exit([arg])</span>** — выход из Python с указанием статуса завершения. Вызывает исключение SystemExit, которое можно перехватить в блоке try/except. Аргумент 0 — успешное завершение, ненулевое значение — ошибка.

```python
import sys
# Выход с кодом 0 (успех)
sys.exit(0)
# Выход с сообщением (код 1)
sys.exit("Ошибка: файл не найден")
# В блоке try/except можно перехватить
try:
    sys.exit(1)
except SystemExit as e:
    print(f"Программа завершилась с кодом {e.code}")
```

## Пути поиска модулей

> **<span style="color: green">sys.path</span>** — список строк, определяющих пути поиска модулей при импорте. Инициализируется из переменной окружения PYTHONPATH и путей по умолчанию. Можно модифицировать динамически для добавления собственных директорий.

```python
import sys
# Просмотр текущих путей
print(sys.path)
# Добавление пути для импорта
sys.path.append('/home/user/my_modules')
sys.path.insert(0, '/path/to/priority')  # в начало списка
# Проверка перед импортом
if '/custom/path' not in sys.path:
    sys.path.append('/custom/path')
```

## Информация о платформе и интерпретаторе

> **<span style="color: green">sys.platform</span>** — строка-идентификатор операционной системы (‘win32’, ‘linux’, ‘darwin’ для macOS, ‘cygwin’ и др.). Используется для платформенно-зависимого кода.
> 
> **<span style="color: green">sys.version</span>** — строка с версией интерпретатора Python и информацией о сборке.
> 
> **<span style="color: green">sys.version_info</span>** — кортеж (major, minor, micro, releaselevel, serial) для программной проверки версии.
> 
> **<span style="color: green">sys.executable</span>** — строка с абсолютным путем к исполняемому файлу интерпретатора Python.

```python
import sys
# Определение ОС
if sys.platform == "win32":
    config_file = "C:\\config.txt"
elif sys.platform.startswith("linux"):
    config_file = "/etc/config.txt"
elif sys.platform == "darwin":
    config_file = "/Users/Shared/config.txt"
# Проверка версии Python
if sys.version_info >= (3, 8):
    print("Поддерживается Python 3.8+")
else:
    print("Требуется обновление Python")
# Путь к интерпретатору
print(f"Используется: {sys.executable}")
```

## Стандартные потоки ввода-вывода

> **<span style="color: green">sys.stdin</span>** — объект файлового типа для стандартного ввода.
> 
> **<span style="color: green">sys.stdout</span>** — стандартный вывод (куда направляется print).
> 
> **<span style="color: green">sys.stderr</span>** — стандартный поток ошибок.
> 
> **<span style="color: green">sys.**stdin**<span style="color: green">**, **<span style="color: green">sys.**stdout**<span style="color: green">**, **<span style="color: green">sys.**stderr**<span style="color: green">** — исходные значения потоков до переопределения.

```python
import sys
# Перенаправление вывода в файл
with open('output.log', 'w') as f:
    old_stdout = sys.stdout
    sys.stdout = f
    print("Это попадет в файл")
    sys.stdout = old_stdout  # восстановление
# Запись ошибок отдельно
sys.stderr.write("Ошибка: что-то пошло не так\n")
# Чтение из stdin
for line in sys.stdin:
    print(f"Получено: {line.strip()}")
```

## Управление загруженными модулями

> **<span style="color: green">sys.modules</span>** — словарь, отображающий имена модулей в объекты модулей. Содержит все уже загруженные модули. Изменение словаря влияет на последующие импорты.
> 
> **<span style="color: green">sys.builtin_module_names</span>** — кортеж строк с именами модулей, встроенных в интерпретатор (например, ‘sys’, ‘builtins’).

```python
import sys
# Список загруженных модулей
print(list(sys.modules.keys()))
# Проверка, загружен ли модуль
if 'numpy' in sys.modules:
    print("NumPy уже импортирован")
# Принудительная перезагрузка (удаление из кэша)
if 'mymodule' in sys.modules:
    del sys.modules['mymodule']
import mymodule  # будет загружен заново
# Проверка, является ли модуль встроенным
print('os' in sys.builtin_module_names)  # False
print('sys' in sys.builtin_module_names)  # True
```

## Память и объекты

> **<span style="color: green">sys.getsizeof(object[, default])</span>** — возвращает размер объекта в байтах. Учитывает только память самого объекта, не включая объекты, на которые он ссылается (для контейнеров).
> 
> **<span style="color: green">sys.getrefcount(object)</span>** — возвращает количество ссылок на объект (с учетом временной ссылки от самого вызова функции).

```python
import sys
# Размер примитивов и контейнеров
print(sys.getsizeof(42))      # обычно 28 байт
print(sys.getsizeof([]))      # базовый размер списка
print(sys.getsizeof([1, 2, 3]))  # больше, чем пустой
# Подсчет ссылок
a = [1, 2, 3]
print(sys.getrefcount(a))  # обычно 2: одна от 'a', одна от аргумента
b = a
print(sys.getrefcount(a))  # 3
```

## Исключения и отладка

> **<span style="color: green">sys.exc_info()</span>** — возвращает кортеж (type, value, traceback) с информацией об обрабатываемом в данный момент исключении. Если исключения нет — (None, None, None).
> 
> **<span style="color: green">sys.last_type</span>**, **<span style="color: green">sys.last_value</span>**, **<span style="color: green">sys.last_traceback</span>** — информация о последнем необработанном исключении (только в интерактивном режиме).
> 
> **<span style="color: green">sys.tracebacklimit</span>** — максимальное количество уровней трассировки, выводимых при необработанном исключении (по умолчанию 1000).

```python
import sys
import traceback
# Получение информации об исключении
try:
    1 / 0
except:
    exc_type, exc_value, exc_tb = sys.exc_info()
    print(f"Тип: {exc_type}")
    print(f"Значение: {exc_value}")
    traceback.print_tb(exc_tb)
# Ограничение глубины стека
sys.tracebacklimit = 2
```

## Рекурсия и лимиты

> **<span style="color: green">sys.getrecursionlimit()</span>** — возвращает максимальную глубину рекурсии (по умолчанию 1000).
> 
> **<span style="color: green">sys.setrecursionlimit(limit)</span>** — устанавливает новый лимит рекурсии. Позволяет увеличить глубину для глубоко рекурсивных алгоритмов.

```python
import sys
# Текущий лимит
print(sys.getrecursionlimit())  # 1000
# Увеличение лимита (осторожно!)
sys.setrecursionlimit(2000)
# Пример глубокой рекурсии
def deep_count(n):
    if n <= 0:
        return 0
    return 1 + deep_count(n - 1)
# Теперь можно вызывать с большими n
print(deep_count(1500))
```

## Флаги и кодировки

> **<span style="color: green">sys.flags</span>** — именованный кортеж с флагами командной строки, с которыми был запущен Python (-O оптимизация, -v подробный режим и т.д.).

> **<span style="color: green">sys.getdefaultencoding()</span>** - функция в модуле sys в Python, которая возвращает название кодировки, используемой по умолчанию для преобразования строк (например, при работе с Unicode). По умолчанию это 'utf-8'.
