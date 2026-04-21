---
date: 
tags: 
authors: GB

Abstract:  
---
### [PDF](zotero://open-pdf/library/items/)

# [Словарь, {dict}](zotero://open-pdf/library/items/PKBGH6XX?page=27&annotation=RCBCJM3A)

	словарь (англ. dict) - изменяемый (mutable) ассоциативный массив (хеш-таблица), представляющий собой набор пар “ключ-значение”, где каждый ключ уникален и должен быть неизменяемым (hashable), а значения могут быть объектами любых типов.

## Основные свойства словарей

>	- изменяемость - можно добавлять, удалять и изменять пары ключ-значение после создания

>	- ключи должны быть хешируемыми (неизменяемыми): строки, числа, кортежи из неизменяемых элементов, frozenset

>	- значения могут быть любыми объектами, включая списки, словари и другие изменяемые типы

>	- с Python 3.7+ гарантированно сохраняется порядок вставки элементов (insertion order)

>	- динамическая структура, автоматически расширяется при добавлении элементов

## Способы создания словарей

```python
dict_1 = dict()
dict_2 = dict(name="Иван", age=30, city="Москва")
dict_3 = {}
dict_4 = {"name": "Мария", "age": 25, "active": True}
print(dict_1)
print(dict_2)
print(dict_3)
print(dict_4)
```

> 	Из списка кортежей (ключ, значение)
```python
dict_5 = dict([("a", 1), ("b", 2), ("c", 3)])
print(dict_5)
```

>	Использование zip для объединения последовательностей ключей и значений
```python
keys = ["x", "y", "z"]
values = [10, 20, 30]
dict_6 = dict(zip(keys, values))
print(dict_6)
```

> 	Создание словаря с одинаковым начальным значением для всех ключей
```python
dict_7 = dict.fromkeys(["a", "b", "c"], 0)
print(dict_7)
```

>	Генератор словаря (dictionary comprehension)
```python
dict_8 = {x: x**2 for x in range(5)}
print(dict_8)           
```

## Доступ к элементам и базовые операции

>	Доступ по ключу (вызывает KeyError, если ключ отсутствует)
```python
user = {"name": "Алексей", "age": 28, "email": "alex@example.com"}
name = user["name"]
print(name)
```

>	Безопасное получение значения (возвращает None или default)
```python
user = {"name": "Алексей", "age": 28, "email": "alex@example.com"}
city = user.get("city")  # None
print(city)
city = user.get("city", "Неизвестно")  # "Неизвестно"
print(city)
```

>	Проверка наличия ключа (проверяет только ключи, не значения)
```python
user = {"name": "Алексей", "age": 28, "email": "alex@example.com"}
has_name = "name" in user  # True
has_city = "city" in user  # False
print(has_name)
print(has_city)
```

>	Количество пар ключ-значение
```python
user = {"name": "Алексей", "age": 28, "email": "alex@example.com"}
count = len(user)
print(count)
```

## Методы словарей

***<span style="color: green">dict.clear()</span>*** - удаляет все элементы из словаря, превращая его в пустой словарь {}.

***<span style="color: green">dict.copy()</span>*** - возвращает поверхностную (мелкую) копию словаря. Вложенные изменяемые объекты остаются общими с оригиналом.

***<span style="color: green">dict.fromkeys(iterable, value=None)</span>*** - классовый метод, создает новый словарь, используя элементы iterable в качестве ключей, всем присваивая значение value (по умолчанию None).

***<span style="color: green">dict.get(key, default=None)</span>*** - возвращает значение по ключу key. Если ключ отсутствует, возвращает default вместо вызова исключения KeyError.

***<span style="color: green">dict.items()</span>*** - возвращает объект-представление (dict_items) всех пар (ключ, значение) в виде кортежей. Представление динамически отражает изменения словаря.

***<span style="color: green">dict.keys()</span>*** - возвращает объект-представление (dict_keys) всех ключей словаря.

***<span style="color: green">dict.values()</span>*** - возвращает объект-представление (dict_values) всех значений словаря.

***<span style="color: green">dict.pop(key, default)</span>*** - удаляет ключ key из словаря и возвращает соответствующее значение. Если ключ не найден и указан default, возвращает default, иначе вызывает KeyError.

***<span style="color: green">dict.popitem()</span>*** - удаляет и возвращает последнюю добавленную пару (ключ, значение) в виде кортежа (key, value). Работает по принципу LIFO (последний пришел - первый ушел) в Python 3.7+. Вызывает KeyError, если словарь пуст.

***<span style="color: green">dict.setdefault(key, default=None)</span>*** - если ключ key существует, возвращает его значение. Если нет, вставляет ключ со значением default и возвращает это значение. Полезен для инициализации значений по умолчанию без дополнительных проверок.

***<span style="color: green">dict.update([other])</span>*** - обновляет словарь элементами из other (другой словарь или итерируемый объект с парами ключ-значение). Существующие ключи перезаписываются новыми значениями. Метод ничего не возвращает (None).

***<span style="color: green">dict | other</span>*** - (Python 3.9+) оператор объединения (merge), возвращает новый словарь, содержащий элементы из обоих словарей. При совпадении ключей используются значения из other.

***<span style="color: green">dict |= other</span>*** - (Python 3.9+) оператор обновления (in-place merge), добавляет элементы из other в существующий словарь. Эквивалентен update(), но возвращает обновленный словарь.

## Перебор словарей (итерация)

```python
data = {"a": 1, "b": 2, "c": 3}

# Перебор ключей (по умолчанию, эквивалентно data.keys())
print("Перебор ключей (по умолчанию, эквивалентно data.keys())---------")
for key in data:
    print(key, data[key])

# Явный перебор ключей
print("Явный перебор ключей---------")
for key in data.keys():
    print(key)

# Перебор только значений
print("Перебор только значений---------")
for value in data.values():
    print(value)

# Перебор пар ключ-значение (items возвращает кортежи)
print("Перебор пар ключ-значение (items возвращает кортежи)---------")
for key, value in data.items():
    print(f"{key}: {value}")

# Безопасное удаление элементов во время итерации
print("Безопасное удаление элементов во время итерации---------")
for key in list(data.keys()):
    if key == "b":
        del data[key]
print(data)
```

## Обновление и расширение словарей

>	Добавление или изменение одного элемента
```python
dict_1 = {"a": 1, "b": 2}

dict_1["d"] = 5
print(dict_1)
```

>	Обновление другим словарем (перезаписывает существующие ключи)
```python
dict_1 = {"a": 1, "b": 2}
dict_2 = {"b": 3, "c": 4}

dict_1.update(dict_2)
print(dict_1)
```


>	Обновление списком кортежей (ключ, значение)
```python
dict_1 = {"a": 1, "b": 2}

dict_1.update([("e", 6), ("f", 7)])
print(dict_1)
```

>	Обновление именованными аргументами
```python
dict_1 = {"a": 1, "b": 2}

dict_1.update(g=8, h=9)
print(dict_1)
```

>	Распаковка словарей (Python 3.5+), создание нового словаря
```python
dict_1 = {"a": 1, "b": 2}
dict_2 = {"b": 3, "c": 4}

merged = {**dict_1, **dict_2}
print(merged)
```

>	Оператор объединения | (Python 3.9+), создает новый словарь
```python
dict_1 = {"a": 1, "b": 2}
dict_2 = {"b": 3, "c": 4}

new_dict = dict_1 | dict_2
print(new_dict)
```

>	Оператор in-place |= (Python 3.9+), модифицирует dict_1
```python
dict_1 = {"a": 1, "b": 2}
dict_2 = {"b": 3, "c": 4}

dict_1 |= dict_2
print(dict_1)
```



## Генераторы словарей (Dictionary Comprehensions)

>	Базовый синтаксис: {ключ: значение for элемент in итерируемый_объект}
```python
squares = {x: x**2 for x in range(6)}
print(squares)
```

>	С условием (фильтрация)
```python
even_cubes = {x: x**3 for x in range(10) if x % 2 == 0}
print(even_cubes)
```

>	Преобразование существующего словаря
```python
prices = {"apple": 100, "banana": 50, "orange": 80}
discounted = {k: v * 0.9 for k, v in prices.items()}
print(discounted)
```

>	Использование enumerate для индексации
```python
items = ["apple", "banana", "cherry"]
indexed = {i: item for i, item in enumerate(items)}
print(indexed)
```

>	Вложенные генераторы словарей
```python
matrix = {i: {j: i*j for j in range(3)} for i in range(3)}
print(matrix)
```

> Обратное отображение (меняем ключи и значения местами)
```python
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {v: k for k, v in original.items()}
print(reversed_dict)
```

## Вложенные словари
>	Словари как значения для построения иерархических структур
```python
company = {
    "departments": {
        "IT": {
            "head": "Иванов",
            "employees": 15,
            "budget": 5000000
        },
        "HR": {
            "head": "Петрова",
            "employees": 5,
            "budget": 1500000
        }
    }
}
print(company)
```