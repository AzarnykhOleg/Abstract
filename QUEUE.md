---
date: 08.05.2026
tags:
  - python
authors: AzOV
Abstract:
---
> queue — стандартная библиотека Python для реализации потокобезопасных очередей (thread-safe).  Основное назначение — безопасная передача данных между потоками в многопоточных приложениях.

# Типы очередей

***<span style="color: green">queue.Queue(maxsize=0)</span>*** — классическая очередь FIFO (First In First Out). Элементы извлекаются в порядке добавления. При maxsize0 очередь не ограничена.

***<span style="color: green">queue.LifoQueue(maxsize=0)</span>*** — стек LIFO (Last In First Out). Последний добавленный элемент извлекается первым.

***<span style="color: green">queue.PriorityQueue(maxsize=0)</span>*** — очередь с приоритетами. Элементы извлекаются в порядке возрастания приоритета (наименьший сначала). Требует сравнимых элементов.

***<span style="color: green">queue.SimpleQueue</span>*** — упрощенная неограниченная очередь FIFO (Python 3.7+). Без отслеживания task_done/join, минимальные накладные расходы.

```python
from queue import Queue, LifoQueue, PriorityQueue, SimpleQueue
# FIFO очередь
fifo = Queue(maxsize=100)
# Стек
lifo = LifoQueue()
# Приоритетная очередь (кортеж: приоритет, данные)
pq = PriorityQueue()
pq.put((1, "высокий приоритет"))
pq.put((3, "низкий приоритет"))
pq.put((2, "средний приоритет"))
print(pq.get())  # (1, 'высокий приоритет')
```

## Основные методы

### Добавление и извлечение

***<span style="color: green">put(item, block=True, timeout=None)</span>*** — добавляет item в очередь. При block=True блокирует до освобождения места (или истечения timeout). При block=False выбрасывает Full если очередь заполнена.

***<span style="color: green">get(block=True, timeout=None)</span>*** — извлекает и возвращает элемент. При block=True блокирует до появления элемента. При timeoutNone ждёт указанное количество секунд.

***<span style="color: green">put_nowait(item)</span>*** — эквивалент put(item, block=False). Выбрасывает queue.Full при заполненной очереди.

***<span style="color: green">get_nowait()</span>*** — эквивалент get(block=False). Выбрасывает queue.Empty при пустой очереди.

```python
import queue

q = queue.Queue(maxsize=2)
q.put("первый")
q.put("вторый")
# Неблокирующее добавление
try:
    q.put_nowait("третий")  # Выбросит Full
except queue.Full:
    print("Очередь заполнена")
# Извлечение с таймаутом
try:
    item = q.get(timeout=1)
except queue.Empty:
    print("Очередь пуста")
```

### Проверка состояния

***<span style="color: green">qsize()</span>*** — возвращает приблизительный размер очереди. Не гарантируется точность в многопоточной среде (race condition между проверкой и использованием).

***<span style="color: green">empty()</span>*** — возвращает True если очередь пуста. Не гарантируется в многопоточной среде (может вернуть True, но другой поток добавит элемент до вашего get).

***<span style="color: green">full()</span>*** — возвращает True если очередь заполнена до maxsize.

```python
if not q.full():
    q.put(item)  # Небезопасно - другой поток мог заполнить после проверки
# Безопасный способ
try:
    q.put_nowait(item)
except queue.Full:
    pass
```

### Отслеживание задач (только Queue, LifoQueue, PriorityQueue)

***<span style="color: green">task_done()</span>*** — сигнализирует о завершении обработки элемента, полученного ранее через get(). Используется вместе с join().

***<span style="color: green">join()</span>*** — блокирует вызывающий поток до тех пор, пока все элементы не будут получены и обработаны (пока счётчик незавершённых задач не станет нулём).

```python
q = queue.Queue()

# Производитель
for i in range(5):
    q.put(i)
# Потребитель
def worker():
    while True:
        item = q.get()
        print(f"Обработка: {item}")
        q.task_done()  # Сигнализируем о завершении
threading.Thread(target=worker, daemon=True).start()
q.join()  # Ждём завершения всех task_done()
print("Все задачи выполнены")
```

# Исключения

***<span style="color: green">queue.Empty</span>*** — выбрасывается get_nowait() или get(block=False) при пустой очереди, либо get() с timeout при истечении времени.

***<span style="color: green">queue.Full</span>*** — выбрасывается put_nowait() или put(block=False) при заполненной очереди.

```python
import queue

try:
    item = q.get_nowait()
except queue.Empty:
    print("Очередь пуста")
try:
    q.put_nowait(item)
except queue.Full:
    print("Очередь полна")
```

# Паттерн “Производитель-Потребитель”

> Классический паттерн: один или несколько потоков производят данные, другие потребляют. Модуль queue обеспечивает потокобезопасность и сигнализацию.

```python
import threading
import queue
import time
import random

class ProducerConsumer:
    def __init__(self):
        self.q = queue.Queue(maxsize=10)
        self.sentinel = None  # Маркер завершения
    
    def producer(self, items):
        for item in items:
            time.sleep(random.random())  # Имитация работы
            self.q.put(item)
            print(f"Произведено: {item}")
        self.q.put(self.sentinel)  # Сигнал конца
    
    def consumer(self):
        while True:
            item = self.q.get()
            if item is self.sentinel:
                self.q.task_done()
                break
            time.sleep(random.random())
            print(f"Потреблено: {item}")
            self.q.task_done()
pc = ProducerConsumer()
threading.Thread(target=pc.producer, args=(range(5),)).start()
threading.Thread(target=pc.consumer).start()
```

# Множественные производители и потребители

```python
import threading
import queue

q = queue.Queue()
sentinel = object()
def producer(id, count):
    for i in range(count):
        q.put((id, i))
    q.put((sentinel, id))  # Каждый производитель сигнализирует
def consumer(num_producers):
    finished = 0
    while finished < num_producers:
        item = q.get()
        if item[0] is sentinel:
            finished += 1
            q.task_done()
            continue
        print(f"Обработка от {item[0]}: {item[1]}")
        q.task_done()
threads = []
for i in range(3):
    t = threading.Thread(target=producer, args=(i, 5))
    threads.append(t)
    t.start()
cons = threading.Thread(target=consumer, args=(3,))
cons.start()
for t in threads:
    t.join()
q.join()  # Ждём обработки всех элементов
cons.join()
```

# Аварийное завершение с Poison Pill

> “Ядовитая пилюля” (sentinel-значение) используется для сигнализации потребителям о необходимости завершения.

```python
import queue
sentinel = object()  # Уникальный объект
def worker(q):
    while True:
        item = q.get()
        if item is sentinel:
            q.task_done()
            break
        # Обработка
        print(f"Работа: {item}")
        q.task_done()
q = queue.Queue()
threads = [threading.Thread(target=worker, args=(q,)) for _ in range(4)]
for t in threads:
    t.start()
# Отправка задач
for i in range(20):
    q.put(i)
# Остановка всех рабочих
for _ in threads:
    q.put(sentinel)
q.join()
for t in threads:
    t.join()
```

# Приоритетная очередь с пользовательскими объектами

```python
import queue
from dataclasses import dataclass, field
@dataclass(order=True)
class Task:
    priority: int
    name: str = field(compare=False)
tasks = PriorityQueue()
tasks.put(Task(3, "низкая"))
tasks.put(Task(1, "высокая"))
tasks.put(Task(2, "средняя"))
while not tasks.empty():
    task = tasks.get()
    print(f"{task.priority}: {task.name}")
```

# Ссылки
[Не бойтесь потоков в Python, они не кусаются](https://habr.com/ru/companies/otus/articles/857094/)