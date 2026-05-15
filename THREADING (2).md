---
date: 08.05.2026
tags:
  - python
  - network
authors: AzOV
Abstract:
---
> threading — стандартная библиотека Python высокого уровня для работы с потоками выполнения (threads).

# Создание и запуск потоков

> Поток создаётся объектом Thread, запускается методом start(), выполняет целевую функцию в параллельном потоке управления.

**<span style="color: green">threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, _, daemon=None)</span>**  — класс для создания потока.

- **target** — callable, выполняемый в потоке
- **args, kwargs** — аргументы целевой функции
- **name** — имя потока (для отладки)
- **daemon** — фоновый поток, завершается при выходе из main

**<span style="color: green">start()</span>**  — запускает поток, вызывается ровно один раз.

**<span style="color: green">join(timeout=None)</span>**  — блокирует вызывающий поток до завершения целевого или истечения таймаута.

```python
import threading
import time

def worker(num):
    print(f"Поток {num} запущен")
    time.sleep(2)
    print(f"Поток {num} завершён")

threads = []

for i in range(3):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print("Все потоки завершены")
```
Вывод: 
```commandline
Поток 0 запущен
Поток 1 запущен
Поток 2 запущен
Поток 2 завершён
Поток 0 завершён
Поток 1 завершён
Все потоки завершены
```

# Класс-поток: наследование от Thread

> Альтернатива передаче target — переопределение метода run() в подклассе.

```python
class MyThread(threading.Thread):
    def __init__(self, num):
        super().__init__()
        self.num = num
    
    def run(self):
        print(f"Работа потока {self.num}")
        time.sleep(1)

t = MyThread(42)
t.start()
t.join()
```

# Синхронизация потоков

### Lock — примитив взаимного исключения

> Базовый механизм блокировки. Один поток захватывает lock, остальные блокируются до освобождения.

**<span style="color: green">threading.Lock()</span>**  — создаёт незаблокированный замок.

**<span style="color: green">acquire(blocking=True, timeout=-1)</span>**  — захватить замок. Блокирует если занят.

**<span style="color: green">release()</span>**  — освободить замок.

**<span style="color: green">with lock:</span>**  — контекстный менеджер (автоматическое освобождение).

```python
counter = 0
lock = threading.Lock()
def increment():
    global counter
    for _ in range(100000):
        with lock:  # Безопасный инкремент
            counter += 1
```

### RLock — реентерабельный замок

> Поток может многократно захватывать тот же RLock без блокировки. Счётчик захватов, освобождение при нуле.

```python
def outer():
    with rlock:
        inner()  # Тот же поток — не блокируется
def inner():
    with rlock:
        print("Внутренняя функция")
rlock = threading.RLock()
```

### Semaphore — семафор ограниченного доступа

> Разрешает фиксированному числу потоков одновременный доступ к ресурсу.

```python
semaphore = threading.Semaphore(3)  # Максимум 3 потока
def limited_resource():
    with semaphore:
        print("Доступ к ограниченному ресурсу")
        time.sleep(1)
```

### BoundedSemaphore

> То же, что Semaphore, но вызывает ValueError при превышении начального значения.

### Event — событие

> Простой механизм сигнализации: один поток устанавливает флаг, другие ждут.

**<span style="color: green">set()</span>**  — установить флаг.**<span style="color: green">clear()</span>**  — сбросить флаг.**<span style="color: green">wait(timeout=None)</span>**  — блокировка до установки флага.**<span style="color: green">is_set()</span>**  — проверка состояния.

```python
ready = threading.Event()
def producer():
    time.sleep(2)
    ready.set()
    print("Данные готовы")
def consumer():
    ready.wait()  # Ждёт set()
    print("Потребляем данные")
```

### Condition — условная переменная

> Комбинация Lock и Event. Потоки ждут определённого условия, получают уведомление при его изменении.

**<span style="color: green">acquire() / release()</span>**  — управление внутренним замком.**<span style="color: green">wait(timeout=None)</span>**  — атомарно освободить замок и ждать.**<span style="color: green">notify(n=1)</span>**  — разбудить n ожидающих потоков.**<span style="color: green">notify_all()</span>**  — разбудить всех.

```python
condition = threading.Condition()
queue = []
def producer():
    for item in range(5):
        with condition:
            queue.append(item)
            condition.notify_all()
        time.sleep(0.5)
def consumer():
    while True:
        with condition:
            while not queue:
                condition.wait()
            item = queue.pop(0)
        print(f"Обработано: {item}")
```

### Barrier — барьер синхронизации

> Блокирует заданное число потоков до их одновременного освобождения.

```python
barrier = threading.Barrier(3)  # Ждём 3 потока
def worker():
    print("Подготовка")
    time.sleep(random.randint(1, 3))
    barrier.wait()  # Все здесь — продолжаем одновременно
    print("Старт!")
```

### Timer — поток с задержкой

> Поток, запускающий функцию по истечении интервала.

```python
timer = threading.Timer(5.0, callback, args=("данные",))
timer.start()   # Запланирован
# timer.cancel()  # Отмена до срабатывания
```

# Локальные данные потока

> threading.local() создаёт пространство имен, уникальное для каждого потока.

```python
thread_local = threading.local()
def init_data(value):
    thread_local.value = value  # Уникально для каждого потока
def process():
    print(f"Значение: {thread_local.value}")
```

# Информация о потоках

|Функция/атрибут|Описание|
|---|---|
|**threading.current_thread()**|Объект текущего потока|
|**threading.enumerate()**|Список всех живых потоков|
|**threading.active_count()**|Количество живых потоков|
|**threading.main_thread()**|Объект главного потока|
|**thread.ident**|Уникальный идентификатор (int или None)|
|**thread.name**|Имя потока|
|**thread.is_alive()**|Жив ли поток|
|**thread.daemon**|Фоновый ли поток|
|**threading.get_native_id()**|Нативный ID ОС (Python 3.8+)|

# Ссылки
