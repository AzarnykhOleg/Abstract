---
date: 
tags: 
authors: GB

Abstract:  
---
# [Математика в Python](zotero://open-pdf/library/items/J46R29EE?page=25&annotation=5H37TVSK)

# [Модуль math](zotero://open-pdf/library/items/J46R29EE?page=25&annotation=DBA87QCN)

	В математическом модуле содержаться константы, например число "пи", "е",  бесконечность и др.

```python
import math


print(math.pi, math.e, math.inf, math.nan, math.tau, sep='\n')
```

	Кроме того внутри модуля есть множество математических функций: синусы,  косинусы, тангенсы, логарифмы, факториал.

# [Модуль decimal](zotero://open-pdf/library/items/J46R29EE?page=25&annotation=2UHN95I8))

	Модуль `decimal` позволяет хранить числа с плавающей запятой и проводить с ними  математические выселения без потери точности и ошибок преобразования. Для  этого надо воспользоваться классом `Decimal` из модуля.

```python
import decimal


pi =  decimal.Decimal('3.141_592_653_589_793_238_462_643_383_279_502_88  4_197_169_399_375')  
print(pi)  
num = decimal.Decimal(1) / decimal.Decimal(3)  
print(num)
```

	Часто при работе с модулем указывают точность вычислений. По умолчанию она  равна 28 знакам до и после запятой.

```python
import decimal


pi =  decimal.Decimal('3.141_592_653_589_793_238_462_643_383_279_502_88  4_197_169_399_375')
decimal.getcontext().prec = 120  
science = 2 * pi * decimal.Decimal(23.452346) ** 2  
print(science)
```

	В первой строке кода задали точность через обращение к атрибуту prec у метода  getcontext().

# [Модуль fractions](zotero://open-pdf/library/items/J46R29EE?page=26&annotation=NXG9EJJI)

	Для работы с дробями есть модуль `fractions`.

```python
import fractions


f1 = fractions.Fraction(1, 3)  
print(f1)  
f2 = fractions.Fraction(3, 5)  
print(f2)  
print(f1 * f2)
```

	Передаём в класс Fractions через запятую числитель и знаменатель дроби. Далее  работаем как с обычными числами.

# [Класс complex()](zotero://open-pdf/library/items/J46R29EE?page=27&annotation=FZKZQFX4)

```python
a = complex(2, 3)  
b = complex('2+3j')  
print(a, b, a == b, sep='\n')
```

***❗❗❗ Python для обозначения  мнимой единицы использует букву "j", а в математике принято использовать "i".  Во всём остальном математические операции в Python совпадают с  классической математикой. ***

# [Математические функции "из коробки"](zotero://open-pdf/library/items/J46R29EE?page=27&annotation=37XBK3L8)

***abs(x)*** — возвращает абсолютное значение числа x, число по модулю.

***divmod(a, b)*** — функция принимает два числа в качестве аргументов и  возвращает пару чисел — частное и остаток от целочисленного деления.  Аналогично вычислению a // b и a % b.

***pow(base, exp[, mod])*** — при передаче 2-х аргументов возводит base в  степень exp. При передаче 3-х аргументов, результат возведения в степень  делится по модулю на значение mod.
	
***round(number[, ndigits])*** — округляет число number до ndigits цифр  после запятой. Если второй аргумент не передать, округляет до ближайшего  целого.
