---
date: 11.05.2026
tags:
  - python
authors: AzOV
Abstract:
---
---
> Модуль `time` предоставляет низкоуровневые функции для работы с временем: получение меток времени (timestamps), форматирование, задержки выполнения и высокоточные измерения. Для объектно-ориентированной работы с датами см. [[datetime]].

```python
import time
```

# Базовые понятия

**Эпоха (Epoch)** — точка отсчёта времени. Для Unix-систем: 1 января 1970, 00:00:00 UTC

**struct_time** — именованный кортеж для представления времени с атрибутами: `tm_year`, `tm_mon`, `tm_mday`, `tm_hour`, `tm_min`, `tm_sec`, `tm_wday` (0=Пн), `tm_yday`, `tm_isdst`

# Получение текущего времени

|        Функция        |           Назначение           |                         Особенности                         |
| :-------------------: | :----------------------------: | :---------------------------------------------------------: |
|     `time.time()`     | Секунды с начала эпохи (float) |      Может “прыгать” при коррекции системного времени       |
|  `time.monotonic()`   |        Монотонное время        | Гарантированно не идёт назад, не зависит от системных часов |
| `time.perf_counter()` |      Высокоточный счётчик      |     Наилучшее разрешение для измерений, включает sleep      |
| `time.process_time()` |       Время CPU процесса       |               Без учёта sleep и ожидания I/O                |

```python
import time

# Unix timestamp
print(time.time())  # 1736611200.5071821
# Монотонное время (для таймаутов)
start = time.monotonic()
```

# Задержки выполнения

```python
time.sleep(seconds)  # Приостанавливает поток на указанное время (может быть float)
```

***❗❗❗ `sleep` освобождает GIL, позволяя другим потокам работать во время паузы.***

# Работа со struct_time

### Получение структуры времени

```python
import time

# Местное время (с учётом часового пояса)
local = time.localtime()  # time.struct_time(tm_year=2025, tm_mon=1...)
# UTC (GMT)
utc = time.gmtime()
# Из timestamp
past = time.localtime(1609459200)  # 1 января 2021

print(local)
print(utc)
print(past)
```

### Компоненты struct_time

|Индекс|Атрибут|Диапазон|Описание|
|---|---|---|---|
|0|`tm_year`|2025|Год|
|1|`tm_mon`|1-12|Месяц|
|2|`tm_mday`|1-31|День месяца|
|3|`tm_hour`|0-23|Часы|
|4|`tm_min`|0-59|Минуты|
|5|`tm_sec`|0-61|Секунды (61 для високосных)|
|6|`tm_wday`|0-6|День недели (0=Понедельник)|
|7|`tm_yday`|1-366|День года|
|8|`tm_isdst`|0,1,-1|Летнее время (0-нет, 1-да, -1-неизвестно)|

```python
t = time.localtime()
print(f'{t.tm_hour}:{t.tm_min}:{t.tm_sec}')
```

# Преобразования времени

### Обратное преобразование (struct_time → секунды)

```python
# Обратная функция к localtime()
t = time.localtime()
seconds = time.mktime(t)  # Возвращает float
```

### Строковое представление

```python
# Быстрое преобразование timestamp в строку
print(time.ctime())  # 'Sat Jan 11 14:30:00 2025'
print(time.ctime(1609459200))  # Из конкретного timestamp
# Из struct_time (asctime)
t = time.localtime()
print(time.asctime(t))  # Тот же формат, что и ctime
```

# Форматирование и парсинг

### strftime — форматирование

```python
formatted = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# 2025-01-11 14:30:00
```

**Основные коды форматирования**

|Код|Значение|Пример|
|---|---|---|
|`%Y`|Год (4 цифры)|2025|
|`%m`|Месяц (01-12)|01|
|`%d`|День (01-31)|11|
|`%H`|Часы 24-час (00-23)|14|
|`%I`|Часы 12-час (01-12)|02|
|`%M`|Минуты (00-59)|30|
|`%S`|Секунды (00-59)|00|
|`%p`|AM/PM|PM|
|`%a`|День недели (сокр.)|Sat|
|`%A`|День недели (полн.)|Saturday|
|`%b`|Месяц (сокр.)|Jan|
|`%B`|Месяц (полн.)|January|

### strptime — парсинг строки

```python
time_string = "11 January, 2025"
result = time.strptime(time_string, "%d %B, %Y")
# time.struct_time(tm_year=2025, tm_mon=1, tm_mday=11...)
```

> 💡 Разница между `strftime` и `strptime` в одной букве: **f**ormat (в строку) vs **p**arse (из строки)

# Измерение производительности

### Правильный способ (perf_counter)

```python
start = time.perf_counter()
time.sleep(2)
end = time.perf_counter()
print(f"Выполнено за {end - start:.6f} секунд")
```

### Измерение в миллисекундах

```python
start = time.perf_counter()
time.sleep(2)
elapsed_ms = (time.perf_counter() - start) * 1000
print(f"{elapsed_ms:.2f} ms")
```

### Профилирование CPU time

```python
start = time.process_time()
# ... вычисления без sleep ...
print(f"CPU time: {time.process_time() - start}")
```

# Практические паттерны

### Таймаут выполнения

```python
import signal
def timeout_handler(signum, frame):
    raise TimeoutError("Превышено время выполнения")
signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(10)  # 10 секунд
try:
    # длительная операция
    pass
except TimeoutError:
    print("Таймаут!")
```

### Таймер обратного отсчета

```python
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Время вышло!')
countdown(60)
```

### Текущее время в миллисекундах (timestamp)

```python
ms = int(time.time() * 1000)
# или для высокой точности
ms_precise = int(time.perf_counter() * 1000)
```

## Сравнение подходов к измерению

|Метод|Точность|Устойчивость к скачкам времени|Учёт sleep|
|---|---|---|---|
|`time()`|~1 сек|❌ Нет|✅ Да|
|`perf_counter()`|Наносекунды|✅ Да (monotonic)|✅ Да|
|`monotonic()`|