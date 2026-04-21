---
date: 
tags: 
authors: GB

Abstract:  
---
# [PDF](zotero://open-pdf/library/items/PKBGH6XX?page=19&annotation=NJRH4YHV)

# Строка (str) 

	- упорядоченная неизменяемая (immutable) последовательность Unicode-символов.  
### Литералы:  
>	Одинарные кавычки: ‘строка’  

>	Двойные кавычки: “строка”  

>	Тройные кавычки: “‘многострочная строка”’ или “”“многострочная строка”“”  

### Свойства:  
>	Неизменяемость: изменение символа по индексу невозможно (s[0] = ‘a’ вызовет ошибку TypeError)  
	
>	Индексация: доступ к символам по индексу с начала (s[0]) и с конца (s[-1])  
	
>	Срезы: получение подстроки через s[начало:конец:шаг]
---
# Встроенные функции  

***<span style="color: green">len(s)</span>***  - возвращает длину строки s  

***<span style="color: green">str(x)</span>***  - преобразует объект x в строку  

***<span style="color: green">ord(©)</span>***  - возвращает целочисленный код Unicode символа ©  

***<span style="color: green">chr(i)</span>***  - возвращает символ по его коду i  

***<span style="color: green">max(s)</span>***  - находит максимальный символ (по коду Unicode)  

***<span style="color: green">min(s)</span>***  - находит минимальный символ  

***<span style="color: green">sorted(s)</span>***  - возвращает отсортированный список символов строки  

***<span style="color: green">repr(s)</span>***  - возвращает строковое представление объекта (с экранированием)

---
# Методы строк
---
## Поиск и проверка содержимого:

***<span style="color: green">str.find(sub, start, end)</span>*** - индекс первого вхождения sub или -1

***<span style="color: green">str.rfind(sub, start, end)</span>*** - индекс последнего вхождения sub или -1

***<span style="color: green">str.index(sub, start, end)</span>*** - индекс первого вхождения или ValueError

***<span style="color: green">str.rindex(sub, start, end)</span>*** - индекс последнего вхождения или ValueError

***<span style="color: green">str.count(sub)</span>*** - количество непересекающихся вхождений sub

***<span style="color: green">str.startswith(prefix)</span>*** - проверка начала строки (True/False)

***<span style="color: green">str.endswith(suffix)</span>*** - проверка конца строки (True/False)

***<span style="color: green">str.isdigit()</span>*** - все символы - цифры

***<span style="color: green">str.isalpha()</span>*** - все символы - буквы

***<span style="color: green">str.isalnum()</span>*** - все символы буквенно-цифровые

***<span style="color: green">str.islower()</span>*** - все буквы в нижнем регистре

***<span style="color: green">str.isupper()</span>*** - все буквы в верхнем регистре

***<span style="color: green">str.istitle()</span>*** - каждое слово начинается с заглавной буквы

***<span style="color: green">str.isspace()</span>*** - все символы пробельные

---
## Изменение регистра (возвращают новую строку):

***<span style="color: green">str.lower()</span>*** - все буквы в нижний регистр

***<span style="color: green">str.upper()</span>*** - все буквы в верхний регистр

***<span style="color: green">str.capitalize()</span>*** - первая буква заглавная, остальные строчные

***<span style="color: green">str.title()</span>*** - каждое слово с заглавной буквы

***<span style="color: green">str.swapcase()</span>*** - инвертирование регистра (верхний/нижний)
    
---
## Модификация строк (возвращают новую строку):

***<span style="color: green">str.strip(chars)</span>*** - удаление пробелов или символов chars с обоих концов

***<span style="color: green">str.lstrip(chars)</span>*** - удаление слева

***<span style="color: green">str.rstrip(chars)</span>*** - удаление справа

***<span style="color: green">str.replace(old, new, count)</span>*** - замена old на new (count раз, если указан)

***<span style="color: green">str.split(sep, maxsplit)</span>*** - разбиение строки в список по разделителю sep

***<span style="color: green">str.rsplit(sep, maxsplit)</span>*** - разбиение справа

***<span style="color: green">str.splitlines()</span>*** - разбиение по символам перевода строки

***<span style="color: green">sep.join(iterable)</span>*** - объединение итерируемого объекта в строку с разделителем sep

***<span style="color: green">str.center(width, fillchar)</span>*** - центрирование в поле шириной width

***<span style="color: green">str.ljust(width, fillchar)</span>*** - выравнивание влево

***<span style="color: green">str.rjust(width, fillchar)</span>*** - выравнивание вправо

***<span style="color: green">str.zfill(width)</span>*** - дополнение нулями слева до ширины width

***<span style="color: green">str.expandtabs(tabsize)</span>*** - замена табуляций на пробелы

---
# Форматирование строк

## Конкатенация
	Через знак "+" - всегда создаётся новый объект.
---

## Старый стиль (оператор %)
  
```python
name = 'Alex'
age = 20
print('Меня зовут %s и мне %d лет' % (name, age))
```
   
   **Основные спецификаторы:**
   
***<span style="color: green">%s </span>*** - строка (str())
***<span style="color: green"> %r </span>*** - repr()
***<span style="color: green"> %d или %i</span>*** - целое число десятичное
***<span style="color: green"> %f </span>***- число с плавающей точкой
***<span style="color: green"> %e или %E</span>*** - экспоненциальная форма
***<span style="color: green"> %x или %X</span>*** - шестнадцатеричное представление
***<span style="color: green">%o</span>*** - восьмеричное представление
***<span style="color: green">\%%</span>*** - литеральный знак процента
   
   **Модификаторы:**
   
***<span style="color: green">   %10s</span>*** - ширина поля 10 символов
***<span style="color: green">  %-10s</span>*** - выравнивание влево (-)
***<span style="color: green"> %010d</span>*** - заполнение нулями слева
***<span style="color: green">   %.2f</span>*** - 2 знака после запятой (точность)
***<span style="color: green">   %(имя)s</span>*** - подстановка по имени ключа из словаря

---
## Метод str.format()

```python
name = 'Alex'
age = 20
print('Меня зовут {} и мне {} лет'.format(name, age))
```

   **Заполнители {}:**
   
***<span style="color: green">{}</span>*** - автоматическая нумерация аргументов
***<span style="color: green">{0}, {1}</span>*** - позиционные индексы
***<span style="color: green">{name}</span>*** - именованные аргументы
***<span style="color: green">{0[0]}, {0[key]}</span>*** - доступ к индексам и ключам
***<span style="color: green">{0.attr}</span>*** - доступ к атрибутам объектов
   Распаковка словаря: ***<span style="color: green">.format(***словарь)</span>***
   Спецификация формата внутри {} описана в разделе Mini-Language ниже.

---
## F-строки (форматированные строковые литералы), Python 3.6+

```python
name = 'Alex'
age = 20
print(f'Меня зовут {name} и мне {age} лет')
```

   **Возможности:**
> **Переменные**: f"Привет, {name}"
**Выражения**: f"Сумма: {a + b}"
**Вызовы функций и методов**: f"{len(s)}, {str.upper()}"
**Индексы и ключи**: f"{lst[0]}, {dct['key']}"
**Спецификация формата**: f"{value:.2f}"
**Отладочный спецификатор = (Python 3.8+)**: f"{var=}" выводит "var=значение"

---
## Спецификация формата Mini-Language  
	Используется в методе format() и f-строках после двоеточия внутри фигурных скобок.  
**Структура**: 
**[имя переменной] : [заполнение]выравнивание][знак][#][0][ширина][разделитель][.точность][тип]**

**Параметры**:

**заполнение** - любой символ (например, 0, *, =), используется с выравниванием

**выравнивание**:
> ***<span style="color: green"><</span>*** - влево (по умолчанию для строк)
***<span style="color: green">></span>*** - вправо (по умолчанию для чисел)
***<span style="color: green">^</span>*** - по центру
***<span style="color: green">=</span>*** - знак числа прижат влево, значение вправо (только для чисел)

**знак**:
> ***<span style="color: green">+</span>*** - всегда показывать знак (+ или -)
***<span style="color: green">-</span>*** - показывать только минус (по умолчанию)
***<span style="color: green">пробел</span>*** - для положительных чисел пробел, для отрицательных минус

> ***<span style="color: green">#</span>*** - альтернативная форма (добавляет префикс 0b, 0o, 0x для систем счисления)

**ширина** - минимальная ширина поля (целое число)

**разделитель**:
> ***<span style="color: green">,</span>*** - разделитель тысяч (запятая)
***<span style="color: green">_</span>*** - разделитель тысяч (подчеркивание)
    
**.точност**ь:
> Для float: количество цифр после десятичной точки
Для str: максимальное количество символов

**тип** - тип представления:
> ***<span style="color: green">s</span>*** - строка
***<span style="color: green">b</span>*** - двоичная система счисления
***<span style="color: green">c</span>*** - символ (преобразует целое число в Unicode-символ)
***<span style="color: green">d</span>*** - десятичное целое число
***<span style="color: green">e или E</span>*** - экспоненциальная форма (e - строчная, E - заглавная)
***<span style="color: green">f или F</span>*** - число с фиксированной точкой
***<span style="color: green">g или G</span>*** - общий формат (использует e или f в зависимости от величины)
***<span style="color: green">n</span>*** - число с учетом локали
***<span style="color: green">o</span>*** - восьмеричная система
***<span style="color: green">x или X</span>*** - шестнадцатеричная система (x - строчные, X - заглавные буквы)
***<span style="color: green">%</span>*** - процент (умножает число на 100 и добавляет знак %)

**Примеры использования**:
> ***<span style="color: green">f"{x:>10}"</span>*** - строка шириной 10, выравнивание вправо
***<span style="color: green">f"{x:<10}" </span>***- строка шириной 10, выравнивание влево
***<span style="color: green">f"{x:^10}"</span>*** - строка шириной 10, по центру
***<span style="color: green">f"{num:.2f}"</span>*** - дробное число с 2 знаками после запятой
***<span style="color: green">f"{num:0>5}"</span>*** - дополнение нулями слева до длины 5
***<span style="color: green">f"{num:,}"</span>*** - разделение тысяч запятыми (1,234,567)
***<span style="color: green">f"{num:_}"</span>*** - разделение тысяч подчеркиванием (1_234_567)
***<span style="color: green">f"{text:*^20}"</span>*** - центрирование текста, заполнение звездочками
***<span style="color: green">f"{num:+d}"</span>*** - всегда показывать знак числа
***<span style="color: green">f"{num:b}"</span>*** - двоичное представление
***<span style="color: green">f"{num:#b}"</span>*** - двоичное с префиксом 0b
***<span style="color: green">f"{num:x}"</span>*** - шестнадцатеричное
***<span style="color: green">f"{percent:.1%}"</span>*** - процент с 1 знаком после запятой