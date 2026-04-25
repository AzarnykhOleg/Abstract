---
date: 
tags: python
authors: GB

Abstract:  
---
# [CSV](zotero://open-pdf/library/items/GMUCHLBQ?page=11&annotation=76HQTPWQ)

	CSV (Comma-Separated Values) — текстовый формат для представления табличных данных, где значения разделены запятыми, а строки — символами перевода строки. Является наиболее универсальным форматом для обмена данными между различными приложениями, системами баз данных и электронными таблицами. Поддерживается Excel, Google Sheets, LibreOffice Calc и большинством СУБД.

## Структура и особенности CSV

> Формат CSV не имеет строгой спецификации (RFC 4180 является рекомендацией, но не стандартом). Основные особенности:

|Элемент|Описание|
|---|---|
|Разделитель полей|Обычно запятая (,), но может быть точка с запятой (;), табуляция (\t) или другой символ|
|Разделитель строк|Перевод строки (\n или \r\n)|
|Заголовок|Первая строка с именами столбцов (опционально, но рекомендуется)|
|Кавычки|Двойные кавычки (“) для значений, содержащих разделители, кавычки или переносы строк|
|Кодировка|Часто UTF-8, но встречается CP1251 (Windows) в старых системах|

> CSV не поддерживает:  
> - Вложенные структуры (иерархические данные)  
> - Типизацию данных (всё хранится как строка)  
> - Комментарии  
> - Множественные листы/таблицы в одном файле

## Таблица конвертации: Python ↔ CSV

|Python|CSV-представление|Примечание|
|---|---|---|
|str|“текст” или текст|Значения в кавычках при наличии спецсимволов|
|int|“42”|Всегда строка в CSV|
|float|“3.14”|Разделитель десятичной части — точка|
|bool|“True” / “False” или “1” / “0”|Зависит от настроек записи|
|None|”” или “None”|Пустое значение или строка|
|list, dict|Не поддерживается напрямую|Требует сериализации в JSON или flattening|
|datetime|“2024-01-15” или “2024-01-15 09:30:00”|Формат зависит от настроек|

## Модуль csv: основные функции

Python предоставляет встроенный модуль `csv` для работы с CSV-файлами. Модуль автоматически обрабатывает экранирование кавычек и разделителей.

## Чтение CSV-файлов

### reader() — базовое чтение

> Функция **<span style="color: green">csv.reader(csvfile, dialect=‘excel’, \**fmtparams)</span>** возвращает объект-итератор, который построчно читает CSV-файл и возвращает каждую строку как список строк.

```python
import csv
# Чтение с разделителем-запятой (по умолчанию)
with open('data.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # ['name', 'age', 'city']
                    # ['Alice', '30', 'NYC']
```

> **Важно:** Параметр `newline=''` при открытии файла обязателен! Иначе возможны проблемы с переводами строк в кавычках на Windows.

### DictReader() — чтение в словари

> Класс **<span style="color: green">csv.DictReader(csvfile, fieldnames=None, restkey=None, restval=None, dialect=‘excel’, \**fmtparams)</span>** читает CSV-файл и возвращает каждую строку как OrderedDict, где ключи — заголовки столбцов.

```python
import csv
with open('data.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['name'], row['age'])
        # row — {'name': 'Alice', 'age': '30', 'city': 'NYC'}
```

> Если заголовков нет, можно передать `fieldnames=['name', 'age', 'city']` для задания имен столбцов.

## Запись CSV-файлов

### writer() — базовая запись

> Функция **<span style="color: green">csv.writer(csvfile, dialect=‘excel’, \**fmtparams)</span>** создает объект для записи строк в CSV-формате.

**<span style="color: green">writer.writerow(row)</span>** — записывает одну строку (список или кортеж).

**<span style="color: green">writer.writerows(rows)</span>** — записывает несколько строк из итерируемого объекта.

```python
import csv
data = [
    ['name', 'age', 'city'],
    ['Alice', 30, 'NYC'],
    ['Bob', 25, 'LA']
]
with open('output.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data)
```

### DictWriter() — запись из словарей

> Класс **<span style="color: green">csv.DictWriter(csvfile, fieldnames, restval=“, extrasaction=‘raise’, dialect=‘excel’, \**fmtparams)</span>** записывает данные из словарей, ключи которых соответствуют fieldnames.

```python
import csv
fieldnames = ['name', 'age', 'city']
data = [
    {'name': 'Alice', 'age': 30, 'city': 'NYC'},
    {'name': 'Bob', 'age': 25, 'city': 'LA'}
]
with open('output.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()  # Пишет заголовки
    writer.writerows(data)
```

## Дополнительные параметры

### Параметры форматирования (fmtparams)

|Параметр|Описание|По умолчанию|
|---|---|---|
|delimiter|Разделитель полей|’,’|
|quotechar|Символ кавычек|’”’|
|quoting|Когда ставить кавычки (QUOTE_MINIMAL, QUOTE_ALL, QUOTE_NONNUMERIC, QUOTE_NONE)|csv.QUOTE_MINIMAL|
|lineterminator|Символ конца строки|’\r\n’ (Windows) или ‘\n’ (Unix)|
|escapechar|Символ экранирования при QUOTE_NONE|None|
|doublequote|Удваивать ли кавычки внутри значения|True|

```python
import csv
# Запись с точкой с запятой и всеми значениями в кавычках
with open('output.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_ALL)
    writer.writerow(['Alice', '30', 'NYC'])
    # Результат: "Alice";"30";"NYC"
```

### Диалекты (Dialects)

> Модуль csv предопределяет несколько диалектов для совместимости:

|Диалект|Описание|
|---|---|
|excel|Стандартный формат Excel (запятая, двойные кавычки)|
|excel-tab|Excel с разделителем-табуляцией (TSV)|
|unix|Минимальное использование кавычек, \n в конце строки|

```python
# Чтение TSV-файла (Tab-Separated Values)
with open('data.tsv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.reader(f, dialect='excel-tab')
    for row in reader:
        print(row)
```

## Практические рекомендации

> **Кодировка:** Всегда указывайте `encoding=‘utf-8’`. Excel в Windows часто сохраняет в CP1251 — используйте `encoding=‘cp1251’` или `‘utf-8-sig’` (с BOM) для совместимости.
> 
> **Переводы строк:** Используйте `newline=''` при открытии файла для корректной обработки многострочных полей в кавычках.
> 
> **Типизация:** CSV хранит только строки. Преобразуйте числа и даты самостоятельно при чтении.

```python
# Чтение с преобразованием типов
with open('data.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        age = int(row['age'])
        score = float(row['score'])
```

---

## [csv docs](https://docs.python.org/3/library/csv.html)
## [habr.com](https://habr.com/ru/companies/otus/articles/1024158/)
