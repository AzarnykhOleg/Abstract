---
date: 18.05.2026
tags: python
authors: AzOV
Abstract:
---
> **argparse** — встроенный модуль Python для создания интерфейсов командной строки (CLI). Позволяет парсить аргументы, передаваемые скрипту при запуске.

# Базовый шаблон использования

1. Импортировать модуль: `import argparse`.
    
2. Создать парсер: `parser = argparse.ArgumentParser(…)`.
    
3. Добавить аргументы: `parser.add_argument(…)`.
    
4. Парсить аргументы: `args = parser.parse_args()`.
    
5. Использовать полученные значения в коде.
    

---

# Ключевые функции и методы

**1. `ArgumentParser()`** — создаёт объект парсера.

_Основные параметры:_

- `description` — краткое описание программы (выводится в справке `--help`).
    
- `epilog` — текст, который выводится после списка аргументов (в справке).
    
```python
parser = argparse.ArgumentParser(
    description="Скрипт для обработки файлов",
    epilog="Спасибо за использование!"
)
```

**2. `add_argument()`** — добавляет аргумент в парсер.

_Ключевые параметры:_

- `name` или `flags` — имя или флаги аргумента (например, `'--input'`, `'-i'`).
    
- `help` — описание аргумента (выводится в справке).
    
- `type` — тип данных (например, `int`, `str`, `float`).
    
- `default` — значение по умолчанию.
    
- `required` — обязателен ли аргумент (`True`/`False`).
    
- `choices` — допустимые значения (список).
    
- `action` — действие при наличии аргумента (например, `'store_true'`, `'count'`).
    

Примеры:

_Позиционный аргумент:_

python

```python
parser.add_argument('filename', help='Имя обрабатываемого файла')
```

_Опциональный аргумент с типом:_

python

```python
parser.add_argument('--count', type=int, default=1, help='Количество повторений')
```

_Булевый флаг:_

python

```python
parser.add_argument('--verbose', action='store_true', help='Включить подробный вывод')
```

_Аргумент с выбором значений:_

python

```python
parser.add_argument('--mode', choices=['fast', 'slow'], default='fast', help='Режим работы')
```

**3. `parse_args()`** — парсит аргументы командной строки и возвращает объект с атрибутами.

Пример:

python

```python
args = parser.parse_args()
print(f"Файл: {args.filename}")
print(f"Количество: {args.count}")
```

**4. `add_subparsers()`** — позволяет создавать подкоманды (subcommands), как в `git commit`, `git push`.

Пример:

python

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

python

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

bash

```bash
python calc.py 5 3 --operation add  # Результат: 8.0
python calc.py 5 3                   # Результат: 8.0 (по умолчанию)
```

**Пример 2: Скрипт с подкомандами**

python

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

bash

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

# Краткий справочник (шпаргалка)

| Функция/Метод          | Назначение                    | Пример                                                       |
| ---------------------- | ----------------------------- | ------------------------------------------------------------ |
| **`ArgumentParser()`** | Создаёт парсер                | `parser = argparse.ArgumentParser(description="Мой скрипт")` |
| **`add_argument()`**   | Добавляет аргумент            | `parser.add_argument('--name', help='Ваше имя')`             |
| **`parse_args()`**     | Парсит аргументы              | `args = parser.parse_args()`                                 |
| **`add_subparsers()`** | Добавляет поддержку подкоманд | `subparsers = parser.add_subparsers(dest='cmd')`             |