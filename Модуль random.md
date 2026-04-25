---
date: 
tags: python
authors: GB

Abstract:  
---
# [Модуль random](zotero://open-pdf/library/items/NW29V7HX?page=21&annotation=QDILKXHP)

модуль random — стандартная библиотека Python для генерации псевдослучайных чисел. Основан на алгоритме Mersenne Twister (вихрь Мерсенна) с периодом 2**19937-1, обеспечивающем высокое качество последовательности и скорость работы. Генератор детерминированный (при том же seed результат воспроизводим), поэтому **не подходит для криптографии и безопасности** — для этих целей используется модуль secrets.

## Основные свойства

> Псевдослучайность — числа генерируются детерминировано на основе начального состояния (seed). При одинаковом seed последовательность повторяется идентично.
> 
> Потокобезопасность — базовые функции модуля используют общий скрытый экземпляр класса Random. При многопоточности для thread-safe рекомендуется создавать отдельные экземпляры Random.
> 
> Диапазоны — функции с плавающей точкой обычно возвращают значения в полуоткрытом интервале [0.0, 1.0), а целочисленные — с включенными границами (зависит от функции).

## Инициализация и управление состоянием

```python
import random
# Установка seed для воспроизводимости
random.seed(42)  # может быть int, str, bytes, bytearray или None (системное время)
# Сохранение и восстановление состояния
state = random.getstate()  # получить внутреннее состояние
random.setstate(state)     # восстановить состояние
# Получение n случайных бит
print(random.getrandbits(8))  # число от 0 до 255
```

## Функции для целых чисел

**<span style="color: green">random.randint(a, b)</span>** — возвращает случайное целое число N в диапазоне a <= N <= b (обе границы включительно). Эквивалент randrange(a, b+1).

**<span style="color: green">random.randrange(stop)</span>** / **<span style="color: green">random.randrange(start, stop[, step])</span>** — случайный элемент из диапазона range(start, stop, step). stop исключен из диапазона. Эффективнее, чем choice(range()), так как не создает список.

**<span style="color: green">random.getrandbits(k)</span>** — возвращает неотрицательное целое число, представляющее k случайных бит (эквивалентно randrange(0, 2^k)).

**<span style="color: green">random.randbytes(n)</span>** — (Python 3.9+) возвращает n случайных байт в виде объекта bytes.

```python
random.randint(1, 100)      # число от 1 до 100 включительно
random.randrange(10)        # 0..9
random.randrange(0, 101, 2) # четное число 0..100
```

## Функции для вещественных чисел

**<span style="color: green">random.random()</span>** — возвращает случайное число с плавающей точкой в интервале [0.0, 1.0).

**<span style="color: green">random.uniform(a, b)</span>** — возвращает случайное число N в интервале [a, b](https://study24.ai/chat/или%20[b,%20a]). Включает конечные точки с вероятностью, зависимой от округления.

**<span style="color: green">random.triangular(low, high, mode)</span>** — треугольное распределение. low <= N <= high, mode — пик вероятности (по умолчанию середина).

```python
# Случайное float
prob = random.random()  # 0.0 <= x < 1.0
# Диапазон
val = random.uniform(10.5, 20.5)
# Треугольное распределение (симметричное)
tri = random.triangular(0, 100, 50)
```

## Функции для последовательностей

**<span style="color: green">random.choice(seq)</span>** — возвращает случайный элемент из непустой последовательности seq. Вызывает IndexError, если seq пуст.

***random.choices(population, weights=None, *, cum_weights=None, k=1)*** — возвращает список длиной k из элементов population с возвратом (выбор с повторением). Можно задать веса (weights) для неравномерного распределения вероятностей.

**<span style="color: green">random.shuffle(x[, random])</span>** — перемешивает последовательность x на месте (in-place), изменяя исходный список. Не работает с неизменяемыми объектами (tuple, str). Возвращает None.

***random.sample(population, k, *, counts=None)*** — возвращает список длины k из уникальных элементов population (выбор без возврата). Исходная последовательность не изменяется. counts позволяет задать кратность элементов без дублирования в population.

```python
items = ['apple', 'banana', 'cherry', 'date']
# Один элемент
print(random.choice(items))
# Несколько с возвратом (могут повторяться)
print(random.choices(items, k=3))
# Несколько с весами (apple в 2 раза вероятнее)
print(random.choices(items, weights=[2, 1, 1, 1], k=3))
# Перемешивание списка
random.shuffle(items)
print(items)
# Выборка без повторений
print(random.sample(items, k=2))
# Выборка с кратностью через counts
print(random.sample(['red', 'blue'], counts=[4, 2], k=3))
```

## Статистические распределения

**<span style="color: green">random.gauss(mu=0.0, sigma=1.0)</span>** — нормальное (гауссово) распределение. Быстрее normalvariate, но не thread-safe. mu — среднее, sigma — стандартное отклонение.

**<span style="color: green">random.normalvariate(mu, sigma)</span>** — нормальное распределение, thread-safe, но медленнее gauss.

**<span style="color: green">random.expovariate(lambd)</span>** — экспоненциальное распределение. lambd = 1 / среднее_значение. Используется для моделирования времени между событиями.

**<span style="color: green">random.lognormvariate(mu, sigma)</span>** — логнормальное распределение. Если взять натуральный логарифм результата, получится нормальное распределение с параметрами mu и sigma.

**<span style="color: green">random.gammavariate(alpha, beta)</span>** — гамма-распределение (alpha > 0, beta > 0).

**<span style="color: green">random.betavariate(alpha, beta)</span>** — бета-распределение на интервале [0, 1](https://study24.ai/chat/alpha%20>%200,%20beta%20>%200).

**<span style="color: green">random.vonmisesvariate(mu, kappa)</span>** — распределение фон Мизеса для углов (mu в радианах, kappa >= 0).

**<span style="color: green">random.paretovariate(alpha)</span>** — распределение Парето.

**<span style="color: green">random.weibullvariate(alpha, beta)</span>** — распределение Вейбулла.

```python
# Нормальное распределение (колокол)
height = random.gauss(170, 10)  # средний рост 170, отклонение 10см
# Экспоненциальное (время между заявками)
wait_time = random.expovariate(1/5)  # среднее ожидание 5 минут
# Равномерный угол
angle = random.vonmisesvariate(0, 0)  # равномерное 0..2π
```

## Классы генераторов

**<span style="color: green">random.Random([seed])</span>** — класс, реализующий генератор псевдослучайных чисел. Можно создать независимые экземпляры для изоляции состояния или многопоточности.

**<span style="color: green">random.SystemRandom([seed])</span>** — класс, использующий os.urandom() — источник энтропии ОС (непредсказуемый). Не поддерживает seed(), getstate(), setstate(). Более безопасен, но медленнее.

```python
# Создание независимого генератора
rng = random.Random(42)
print(rng.randint(1, 100))
# Системный генератор (более случайный)
secure_rng = random.SystemRandom()
print(secure_rng.random())  # для криптографии лучше использовать secrets модуль
```

## Практические замечания и паттерны

> Воспроизводимость экспериментов
> 
> ```python
> # Для детерминированных тестов и отладки
> random.seed(42)  # фиксируем seed
> results = [random.random() for _ in range(10)]
> # При повторном запуске results будет идентичным
> ```
> 
> Выбор случайного элемента из диапазона с исключением
> 
> ```python
> # Исключаем число 5 из диапазона 0-9
> choices = [x for x in range(10) if x != 5]
> random.choice(choices)
> # Или через sample, если нужно несколько
> random.sample([x for x in range(10) if x != 5], k=3)
> ```
> 
> Перемешивание неизменяемой последовательности
> 
> ```python
> # Для строк, кортежей используем sample с k=len(x)
> s = "hello"
> shuffled = ''.join(random.sample(s, len(s))
> ```
