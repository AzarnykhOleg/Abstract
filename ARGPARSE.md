---
date: 18.05.2026
tags: python
authors: AzOV
Abstract:
---
> ***<span style="color: green">argparse</span>*** — встроенный модуль Python для создания интерфейсов командной строки (CLI). Позволяет парсить аргументы, передаваемые скрипту при запуске.

# Базовый шаблон использования

1. Импортировать модуль: ***<span style="color: green">import argparse</span>***.
    
2. Создать парсер: ***<span style="color: green">parser = argparse.ArgumentParser(…)</span>***.
    
3. Добавить аргументы: ***<span style="color: green">parser.add_argument(…)</span>***.
    
4. Парсить аргументы: ***<span style="color: green">args = parser.parse_args()</span>***.
    
5. Использовать полученные значения в коде.
    

---

# Ключевые функции и методы

###  ***<span style="color: green">ArgumentParser()</span>*** — создаёт объект парсера.

_Основные параметры:_

- ***<span style="color: green">description</span>*** — краткое описание программы (выводится в справке `--help`).
    
- ***<span style="color: green">epilog</span>*** — текст, который выводится после списка аргументов (в справке).
    
```python
parser = argparse.ArgumentParser(
    description="Скрипт для обработки файлов",
    epilog="Спасибо за использование!"
)
```

### ***<span style="color: green">add_argument()</span>*** — добавляет аргумент в парсер.

_Ключевые параметры:_

- ***<span style="color: green">name</span>*** или ***<span style="color: green">flags</span>*** — имя или флаги аргумента (например, `'--input'`, `'-i'`).
    
- ***<span style="color: green">help</span>*** — описание аргумента (выводится в справке).
    
- ***<span style="color: green">type</span>*** — тип данных (например, `int`, `str`, `float`).
    
- ***<span style="color: green">default</span>*** — значение по умолчанию.
    
- ***<span style="color: green">required</span>*** — обязателен ли аргумент (`True`/`False`).
    
- ***<span style="color: green">choices</span>*** — допустимые значения (список).
    
- ***<span style="color: green">action</span>*** — действие при наличии аргумента:
	- **store (по умолчанию)** — сохраняет значение аргумента без изменения его типа. 
	- **store_const** — сохраняет значение, указанное в параметре const. По умолчанию const равен None. Часто используется с опциональными флагами.
	- **store_true** и **store_false** — специальные случаи  store_const, которые сохраняют значения True и False соответственно. По умолчанию store_true хранит False, а store_false True. Эти действия часто используются для создания булевых флагов, которые включают или выключают определённые функции программы. 
	- **append** — добавляет значение в список. Используется, когда один и тот же флаг можно использовать многократно. 
	- **count** — подсчитывает количество появлений флага. Часто применяется для реализации уровня детализации (например, -vvv). 
	- **callback** — вызывает пользовательскую функцию для сложной логики.
    
Примеры:

_Позиционный аргумент:_

```python
parser.add_argument('filename', help='Имя обрабатываемого файла')
```

_Опциональный аргумент с типом:_

```python
parser.add_argument('--count', type=int, default=1, help='Количество повторений')
```

_Булевый флаг:_

```python
parser.add_argument('--verbose', action='store_true', help='Включить подробный вывод')
```

_Аргумент с выбором значений:_

```python
parser.add_argument('--mode', choices=['fast', 'slow'], default='fast', help='Режим работы')
```

### ***<span style="color: green">parse_args()</span>*** — парсит аргументы командной строки и возвращает объект с атрибутами.

Пример:

```python
args = parser.parse_args()
print(f"Файл: {args.filename}")
print(f"Количество: {args.count}")
```

### ***<span style="color: green">add_subparsers()</span>*** — позволяет создавать подкоманды (subcommands), как в `git commit`, `git push`.

Пример:

```python
subparsers = parser.add_subparsers(dest='command', help='Доступные команды')

# Подкоманда "create"
create_parser = subparsers.add_parser('create', help='Создать файл')
create_parser.add_argument('name', help='Имя файла')

# Подкоманда "delete"
delete_parser = subparsers.add_parser('delete', help='Удалить файл')
delete_parser.add_argument('name', help='Имя файла')
```

---

# Примеры использования

**Пример 1: Простой скрипт с позиционным и опциональным аргументами**

```python
import argparse

parser = argparse.ArgumentParser(description="Простой калькулятор")
parser.add_argument('x', type=float, help='Первое число')
parser.add_argument('y', type=float, help='Второе число')
parser.add_argument('--operation', choices=['add', 'sub'], default='add', help='Операция: сложение или вычитание')

args = parser.parse_args()

if args.operation == 'add':
    result = args.x + args.y
else:
    result = args.x - args.y

print(f"Результат: {result}")
```

Запуск:

```bash
python calc.py 5 3 --operation add  # Результат: 8.0
python calc.py 5 3                   # Результат: 8.0 (по умолчанию)
```

**Пример 2: Скрипт с подкомандами**

```python
import argparse

parser = argparse.ArgumentParser(description="Менеджер файлов")
subparsers = parser.add_subparsers(dest='command', help='Команды')

# Команда "list"
list_parser = subparsers.add_parser('list', help='Показать список файлов')
list_parser.add_argument('--path', default='.', help='Путь к директории')

# Команда "copy"
copy_parser = subparsers.add_parser('copy', help='Копировать файл')
copy_parser.add_argument('source', help='Исходный файл')
copy_parser.add_argument('dest', help='Целевой файл')

args = parser.parse_args()

if args.command == 'list':
    print(f"Список файлов в {args.path}")
elif args.command == 'copy':
    print(f"Копируем {args.source} в {args.dest}")
```

Запуск:

```bash
python file_manager.py list --path /home  # Список файлов в /home
python file_manager.py copy file1.txt file2.txt  # Копируем file1.txt в file2.txt
```

---

# Полезные советы

- **Справка (`--help`)** генерируется автоматически. Всегда добавляйте понятные описания (`help`) к аргументам.
    
- Используйте `type` для автоматической конвертации типов. Это избавит от ручного преобразования строк.
    
- Для булевых флагов используйте `action='store_true'` или `action='store_false'`.
    
- Подкоманды (`subparsers`) полезны для сложных утилит с множеством функций.
    
- Если аргумент не передан, а `default` не задан, атрибут в `args` будет `None`.
    

---

# Краткий справочник

| Функция/Метод          | Назначение                    | Пример                                                       |
| ---------------------- | ----------------------------- | ------------------------------------------------------------ |
| ***<span style="color: green">ArgumentParser()</span>*** | Создаёт парсер                | `parser = argparse.ArgumentParser(description="Мой скрипт")` |
| ***<span style="color: green">add_argument()</span>***   | Добавляет аргумент            | `parser.add_argument('--name', help='Ваше имя')`             |
| ***<span style="color: green">parse_args()</span>***     | Парсит аргументы              | `args = parser.parse_args()`                                 |
| ***<span style="color: green">add_subparsers()</span>*** | Добавляет поддержку подкоманд | `subparsers = parser.add_subparsers(dest='cmd')`             |