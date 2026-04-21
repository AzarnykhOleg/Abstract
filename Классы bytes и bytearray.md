---
date: 
tags: 
authors: GB

Abstract:  
---
### [PDF](zotero://open-pdf/library/items/)

# [Классы bytes и bytearray](zotero://open-pdf/library/items/PKBGH6XX?page=38&annotation=KR7SP6YE)

	байты (англ. bytes) - неизменяемая (immutable) последовательность байтов (целых чисел от 0 до 255), представляющая собой сырой бинарный поток данных без привязки к конкретной кодировке текста.

	байтовый массив (англ. bytearray) - изменяемая (mutable) версия bytes, поддерживающая те же операции чтения, но позволяющая модифицировать содержимое после создания (добавление, удаление, изменение отдельных байтов по индексу).
    
# Основные свойства байтовых типов
    
>- неизменяемость bytes против изменяемости bytearray; bytearray можно использовать когда требуется частое изменение бинарных данных без создания копий

>- элементы представляют собой 8-битные беззнаковые целые числа (0-255); при индексации возвращается int, а не односимвольная строка

>- поддержка буферного протокола (buffer protocol) - совместимы с memoryview и различными библиотеками для работы с бинарными данными

>- bytes являются hashable (могут быть ключами словаря), bytearray - нет

>- оба типа поддерживают общие операции последовательностей (срезы, конкатенацию, умножение, проверку вхождения)


# Способы создания bytes
> Пустой bytes
```python
b1 = bytes()
b2 = b''
print(b2)
```

> Важно: bytes(n) создает последовательность из n нулевых байтов, а не преобразует число!
```python
b3 = bytes(4)  
print(b3)  # b'\x00\x00\x00\x00'
```

> Из списка/итерируемого с числами 0-255
```python
b4 = bytes([65, 66, 67])
b5 = bytes(range(65, 70))
print(b4)  # b'ABC'
print(b5)  # b'ABCDE'
```

> Байтовый литерал (префикс b, только ASCII-символы)
```python
b6 = b'Hello World'
print(b6)
```

> Из строки с указанием кодировки (encode)
```python
text = "Привет"
b7 = text.encode('utf-8')
b8 = bytes(text, 'utf-8')  # альтернативный синтаксис
print(b7)  # b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'
print(b8)  # b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'
```

# Способы создания bytearray

> Пустой bytearray
```python
ba1 = bytearray()
print(ba1)
```

> Нулевые байты заданной длины
```python
ba2 = bytearray(5)  
print(ba2)  # bytearray(b'\x00\x00\x00\x00\x00')
```

> Из списка чисел
```python
ba3 = bytearray([72, 101, 108, 108, 111])  # bytearray(b'Hello')
print(ba3)
```

> Из bytes или другого байтового объекта
```python
ba4 = bytearray(b'Hello')
print(ba4)
```

> Из строки с указанием кодировки
```python
ba5 = bytearray("Hello", 'utf-8')
print(ba5)
```

> Копирование с изменением
```python
original = b'Hello'
mutable = bytearray(original)
mutable[0] = 74  # ASCII 'J'
print(mutable)  # bytearray(b'Jello')
```


# Преобразование между строками и байтами

    Текст и байты - разные сущности. Для преобразования обязательно указание кодировки (UTF-8, CP1251, Latin-1 и т.д.). Неправильная кодировка при декодировании вызывает UnicodeDecodeError.

> Кодирование: str → bytes
```python
s = "Emoji: 🎉"
b_utf8 = s.encode('utf-8')
print(b_utf8)  # b'Emoji: \xf0\x9f\x8e\x89'
```

> Декодирование: bytes → str
```python
s2 = b_utf8.decode('utf-8')
print(s2)  # Emoji: 🎉
```

> Обработка ошибок при декодировании
```python
broken = b'\xff\xfe\n'  # невалидные UTF-8 байты
text = broken.decode('utf-8', errors='replace')  # замена символом 
text2 = broken.decode('utf-8', errors='ignore')   # пропуск ошибок
print(text)
print(text2)
```

# Доступ к элементам и базовые операции

```python
 b = b'Python'
# Индексация возвращает int (0-255)
print(b[0])       # 80 (ASCII 'P')
print(b[-1])      # 110 (ASCII 'n')
# Срезы возвращают новый объект того же типа
print(b[0:2])     # b'Py'
print(b[::-1])    # b'nohtyP' (реверс)
# Конкатенация (типы должны совпадать или быть совместимы)
new_b = b'Hello ' + b'World'
print(new_b)      # b'Hello World'
# Повторение
print(b'A' * 5)   # b'AAAAA'
# Проверка вхождения (in)
print(80 in b)        # True (число)
print(b'Py' in b)     # True (подпоследовательность)
print(b'Java' not in b)  # True
# Длина
print(len(b))     # 6
# Перебор (итерация по int)
for byte in b:
     print(byte, end=' ')  # 80 121 116 104 111 110
```

# Методы bytes и bytearray (общие)
    
***<span style="color: green">bytes.decode(encoding=‘utf-8’, errors=‘strict’)</span>*** — преобразует байты в строку str с указанной кодировкой. Параметр errors: ‘strict’ (исключение при ошибке), ‘replace’ (замена символом ), ‘ignore’ (пропуск).
    
***<span style="color: green">bytes.hex()</span>*** — возвращает строку из шестнадцатеричных цифр (каждый байт → две hex-цифры), разделитель отсутствует.
    
***<span style="color: green">bytes.fromhex(string)</span>*** — статический метод, создает bytes из строки hex-цифр (пробелы и табы игнорируются).
    
***<span style="color: green">bytes.count(sub[, start[, end]])</span>*** — возвращает количество неперекрывающихся вхождений байтовой подпоследовательности sub.
    
***<span style="color: green">bytes.find(sub[, start[, end]])</span>*** — возвращает индекс первого вхождения sub или -1, если не найдено. Аналогичен str.find().
    
***<span style="color: green">bytes.index(sub[, start[, end]])</span>*** — возвращает индекс первого вхождения sub или вызывает ValueError, если подпоследовательность не найдена.
    
***<span style="color: green">bytes.rfind(sub[, start[, end]])</span>*** — возвращает индекс последнего вхождения sub или -1.
    
***<span style="color: green">bytes.rindex(sub[, start[, end]])</span>*** — возвращает индекс последнего вхождения sub или ValueError.
    
***<span style="color: green">bytes.join(iterable)</span>*** — соединяет итерируемый объект байтовых объектов, используя текущий объект как разделитель между элементами.
    
***<span style="color: green">bytes.replace(old, new[, count])</span>*** — заменяет все вхождения байтов old на new; если указан count, заменяет только первые count вхождений.
    
***<span style="color: green">bytes.split(sep=None, maxsplit=-1)</span>*** — разбивает байты по разделителю sep, возвращает список bytes. При sep=None разбивает по любым пробельным символам ASCII.
    
***<span style="color: green">bytes.rsplit(sep=None, maxsplit=-1)</span>*** — разбиение справа, иначе аналогично split.
    
***<span style="color: green">bytes.partition(sep)</span>*** — разбивает на три части: (head, sep, tail) по первому вхождению sep. Возвращает кортеж.
    
***<span style="color: green">bytes.rpartition(sep)</span>*** — разбиение по последнему вхождению sep.
    
***<span style="color: green">bytes.startswith(prefix[, start[, end]])</span>*** — проверяет, начинается ли последовательность с указанного префикса (bytes или кортеж bytes).
    
***<span style="color: green">bytes.endswith(suffix[, start[, end]])</span>*** — проверяет, заканчивается ли последовательность указанным суффиксом.
    
***<span style="color: green">bytes.strip([chars])</span>*** — удаляет указанные байты с начала и конца; по умолчанию удаляет пробельные ASCII-символы.
    
***<span style="color: green">bytes.lstrip([chars])</span>*** — удаляет с начала (left).
    
***<span style="color: green">bytes.rstrip([chars])</span>*** — удаляет с конца (right).
    
***<span style="color: green">bytes.translate(table[, delete=b”])</span>*** — транслирует байты по таблице table (создается через maketrans), удаляет байты, указанные в delete.
    
***<span style="color: green">bytes.maketrans(from, to)</span>*** — статический метод, создает таблицу трансляции для translate; from и to должны быть bytes одинаковой длины.
    
***<span style="color: green">bytes.center(width[, fillbyte])</span>*** — центрирует последовательность в поле шириной width, заполняя fillbyte (по умолчанию ASCII-пробел).
    
***<span style="color: green">bytes.ljust(width[, fillbyte])</span>*** — выравнивание по левому краю.
    
***<span style="color: green">bytes.rjust(width[, fillbyte])</span>*** — выравнивание по правому краю.
    
***<span style="color: green">bytes.zfill(width)</span>*** — дополняет нулями ASCII (b’0’) слева до длины width.
   
# Изменяемые операции bytearray (специфичные методы)

   ***<span style="color: green">bytearray.append(x)</span>*** — добавляет байт x