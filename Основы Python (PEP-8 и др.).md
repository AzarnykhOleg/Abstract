---
date: 
tags: 
authors: GB

Abstract:  
---


## Работа в IDE
([13](zotero://open-pdf/library/items/7WNSNKIW?page=13&annotation=8BH3WFTT))

Python-программы можно писать в любом текстовом редакторе, главное сохранять текст программы в кодировке UTF-8.

***❗❗❗ Не давайте именам питоновских файлов имена встроенных и  внешних модулей. Это приведёт к затиранию имён и отключению функционала  модулей. ***

## PEP-8 (руководство по стилю) и  PEP-257 (оформление  документации/комментариев)
([14](zotero://open-pdf/library/items/7WNSNKIW?page=14&annotation=TIFNX4IF))

## Переменные и требования к именам
([14](zotero://open-pdf/library/items/7WNSNKIW?page=14&annotation=SR44V9RK))

● Python использует кодировку utf-8. Поэтому в качестве имени переменной  может выступать любой набор символов, даже смайлик. Однако правильные  имена это имена на латинице, т.е. английские строчные буквы, слова.  Например name, age.  ● Если название переменной состоит из нескольких слов такие слова  записываются строчными буквами разделяются символом подчёркивания.  Этот стиль называется snake_case.  ● В качестве первого символа в имени переменной запрещено использовать  цифры и другие знаки пунктуации в этом случае Python выдаст ошибку. Имя  начинается с буквы или символа подчёркивания.  ● Не используйте написание слов на транслите. Воспользуйтесь онлайн  переводчиком на английский. Не zdorove, а health.

## Константы
([16](zotero://open-pdf/library/items/7WNSNKIW?page=16&annotation=ZKVK64J9))

константа — это переменная написанное прописными буквами.

`MAX_COUNT = 1000  ZERO = 0  DATA_AFTER_DELETE = &#39;No data&#39;  DAY = 60 * 60 * 24`

## Функция id()
([16](zotero://open-pdf/library/items/7WNSNKIW?page=16&annotation=TPDLVJ7Z))

функцией id(), которая возвращает адрес объекта в  оперативной памяти вашего компьютера.

`a=5  print(id(a))  a = &quot;hello world&quot;  print(id(a))  a = 42.0 * 3.141592 / 2.71828  print(id(a))`

> 1615821406576  1615826697776  1615831485936
([17](zotero://open-pdf/library/items/7WNSNKIW?page=17&annotation=XWMR2VRD))

## Зарезервированные слова, keyword.kwlist
([17](zotero://open-pdf/library/items/7WNSNKIW?page=17&annotation=FN49VGWI))

Существует чуть менее 40 зарезервированных слов

> False, None, True, and, as, assert, async, await, break, class,  continue, def, del, elif, else, except, finally, for, from,  global, if, import, in, is, lambda, nonlocal, not, or, pass,  raise, return, try, while, with, yield.
([17](zotero://open-pdf/library/items/7WNSNKIW?page=17&annotation=PAWFVBJH))

А также case и match начиная с версии Python 3.10.

***❗❗❗ Запрещено использовать в качестве имён переменных  зарезервированные слова. Python завершить код с ошибкой. ***

## Ввод и вывод данных
([17](zotero://open-pdf/library/items/7WNSNKIW?page=17&annotation=N9S59QMV))

`print()`

для вывода данных

`input()`

для ввода данных и  сохранение в переменные

### ➢ Вывод, функция print()

```python
print(*objects, sep=&#39; &#39;, end=&#39;&#92;n&#39;, file=sys.stdout, flush=False)
```

```python
print(42)  print(1, 2, 3, 4)  print(&#39;Hello&#39;, &#39;,&#39;, &#39;world&#39;, &#39;!&#39;)
```

> 42  1234  Hello , world !
([18](zotero://open-pdf/library/items/7WNSNKIW?page=18&annotation=V2ZIDLLB))

`sep`

по умолчанию хранит один пробел. Именно этим символом разделяются все  объекты, перечисленные через запятую.

`end`

по умолчанию хранит символ перехода на новую строку &#39;&#92;n&#39;. Это то, что функция  print добавляет после вывода всех объектов.

```python
print(42, sep=&#39;___&#39;, end=&#39;&#92;n(=^.^=)&#92;n&#39;)  print(1, 2, 3, 4, sep=&#39;___&#39;, end=&#39;&#92;n(=^.^=)&#92;n&#39;)  print(&#39;Hello&#39;, &#39;,&#39;, &#39;world&#39;, &#39;!&#39;, sep=&#39;___&#39;, end=&#39;&#92;n(=^.^=)&#92;n&#39;)
```

> 42  (=^.^=)  1___2___3___4  (=^.^=)  Hello___,___world___!  (=^.^=)
([18](zotero://open-pdf/library/items/7WNSNKIW?page=18&annotation=YYABM5X4))

### ➢ Ввод, функция input()

Для ввода данных и сохранение их в переменной

```python
result = input([prompt])
```

***❗❗❗ Функция возвращает объект строкового типа,  который можно сохранить в переменную. ***

```python
name = input(&#39;Ваше имя: &#39;)
```

Для приведения строки к числу используем функции int() — целый тип или float() вещественный тип

```python
age = float(input(&#39;Ваш возраст: &#39;))  how_old = age - 18  print(how_old, &quot;лет назад ты стал совершеннолетним&quot;)
```

> Ваш возраст: 33  15.0 лет назад ты стал совершеннолетним
([19](zotero://open-pdf/library/items/7WNSNKIW?page=19&annotation=KNT6DNI7))