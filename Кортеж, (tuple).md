---
date: 
tags: python
authors: GB

Abstract:  
---
### [PDF](zotero://open-pdf/library/items/)

# [Кортеж, (tuple)](zotero://open-pdf/library/items/PKBGH6XX?page=26&annotation=7SMC4HVF)

	кортеж (англ. tuple) - абстрактный тип данных, представляющий собой неизменяемый (immutable) упорядоченный набор значений, элементы которого нельзя изменить, добавить или удалить после создания.

### Основные свойства кортежей
>	- упорядоченность
>	- неизменяемость (immutable)
>	- индексируемость
>	- допускаются дубликаты
>	- могут содержать элементы разных типов
>	- подходят для использования в качестве ключей словарей

# Способы создания кортежей

>	tuple_1 = tuple()

>	tuple_2 = tuple((3.14, True, “Hello world!”))

>	tuple_3 = ()

>	tuple_4 = (3.14, True, “Hello world!”)

>	tuple_5 = 3.14, True, “Hello world!”

>	tuple_6 = (5,) # кортеж из одного элемента, запятая обязательна

>	new_tuple = tuple(iterable_object)

# Доступ к элементам кортежа

```python
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

element = my_tuple[2] # доступ по индексу (нумерация с 0)
print(element)
last_element = my_tuple[-1] # доступ с конца
print(last_element)
slice_tuple = my_tuple[0:4] # срез, создается новый кортеж
print(slice_tuple)
```

# Операции с кортежами

Кортеж неизменяем, поэтому прямое изменение элементов невозможно. Для модификации создается новый кортеж:

### объединение (конкатенация)

```python
tuple_1 = (1, 2, 3)  
tuple_2 = (4, 5, 6)  
tuple_3 = tuple_1 + tuple_2
print(tuple_3)
```

### повторение

```python
tuple_1 = (1, 2, 3) 
tuple_4 = tuple_1 * 3
print(tuple_4)
```

### проверка вхождения

>	exists = 2 in tuple_1 # возвращает True или False

### удаление переменной (не элемента!)

>	del tuple_1

# Методы кортежей

***<span style="color: green">my_tuple.count(el)</span>*** - подсчитывает количество вхождений элемента el в кортеж.

***<span style="color: green">my_tuple.index(N, start, stop)</span>*** - возвращает индекс первого вхождения элемента N в часть кортежа от индекса start до индекса stop. Если элемента нет - возникает ValueError.

# Встроенные функции

***<span style="color: green">len(my_tuple)</span>*** - возвращает длину кортежа  

***<span style="color: green">max(my_tuple)</span>*** - находит максимальный элемент (по значению)  

***<span style="color: green">min(my_tuple)</span>*** - находит минимальный элемент  

***<span style="color: green">sum(my_tuple)</span>*** - вычисляет сумму элементов (только для чисел)  

***<span style="color: green">sorted(my_tuple)</span>*** - возвращает отсортированный СПИСОК (list!), НЕ КОРТЕЖ

# Преобразование типов и изменение

	Для изменения содержимого кортежа используется промежуточное преобразование в список:

```python
my_tuple = (1, 2, 3)  

temp_list = list(my_tuple)  
temp_list[0] = 100  
my_tuple = tuple(temp_list)
print(my_tuple)
```


	Обратное преобразование:   

```python
my_list = [1, 2, 3]  
my_tuple = tuple(my_list)
print(my_tuple)
```

# Распаковка кортежей

```python
a, b, c = (1, 2, 3)                             # a=1, b=2, c=3
print(f'{a = }\n {b = }\n {c = }')
```

```python
a, *b, c = (1, 2, 3, 4, 5)                    # a=1, b=[2, 3, 4], c=5
print(f'{a = }\n {b = }\n {c = }')
```

```python
name, age, company = tuple(["Иван", 37, "Яндекс"])
print(f'{name = }\n {age = }\n {company = }')
```


# Вложенные кортежи:  

>	nested = (1, (2, 3), [4, 5])                    # кортеж может содержать изменяемые объекты
