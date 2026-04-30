---
date: 29.04.2026
tags:
  - python
  - socket
authors:
Abstract:
---
[Документация](https://docs.python.org/3/library/socket.html)
[Руководство по программированию сокетов на Python](https://habr.com/ru/companies/skillfactory/articles/690186/)

модуль socket — встроенная библиотека Python для низкоуровневого сетевого программирования, предоставляющая интерфейс к системным сокетам BSD (Berkeley Software Distribution). Позволяет создавать клиент-серверные приложения, использующие протоколы TCP (надежный потоковый обмен) и UDP (быстрая доставка дейтаграмм без гарантий)

<a href="https://javarush.com/quests/lectures/ru.javarush.python.core.lecture.level13.lecture06">javarush.com</a>

,

<a href="https://docs-python.ru/standart-library/modul-socket-setevoj-interfejs-python/">docs-python.ru</a>

.

## Основные понятия

> **Сокет** — конечная точка (“розетка”) двустороннего канала связи между двумя программами по сети. Идентифицируется комбинацией IP-адреса (идентификатор устройства в сети, аналог адреса дома) и номера порта (идентификатор приложения на устройстве, аналог номера квартиры)
> 
> <a href="https://javarush.com/quests/lectures/ru.javarush.python.core.lecture.level13.lecture06">javarush.com</a>
> 
> .
> 
> **TCP (SOCK_STREAM)** — протокол с установлением соединения (connection-oriented). Обеспечивает надежную, упорядоченную доставку потока байтов без потерь и дублирования. Используется для HTTP, FTP, почты.
> 
> **UDP (SOCK_DGRAM)** — протокол без установления соединения (connectionless). Отправляет независимые дейтаграммы без гарантии доставки, порядка или отсутствия дубликатов. Быстрее TCP, используется для потокового видео, онлайн-игр, DNS-запросов
> 
> <a href="https://javarush.com/quests/lectures/ru.javarush.python.core.lecture.level13.lecture06">javarush.com</a>
> 
> .

## Создание сокета

***<span style="color: green">socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)</span>*** — фабричная функция, создающая и возвращающий объект сокета.

- **family** — семейство адресов: `AF_INET` (IPv4, по умолчанию), `AF_INET6` (IPv6), `AF_UNIX` (локальные Unix-сокеты).
- **type** — тип сокета: `SOCK_STREAM` (TCP), `SOCK_DGRAM` (UDP), `SOCK_RAW` (низкоуровневый доступ).
- **proto** — номер протокола (обычно 0 для TCP/UDP).

```python
import socket
# TCP-сокет IPv4
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# UDP-сокет IPv4
udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Использование контекстного менеджера (автоматическое закрытие)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    pass  # сокет будет закрыт автоматически
```

## TCP-сервер

> Алгоритм работы сервера на TCP: создание сокета → привязка к адресу (`bind`) → перевод в режим прослушивания (`listen`) → принятие соединения (`accept`, блокирующий вызов) → обмен данными → закрытие
> 
> <a href="https://python-course.readthedocs.io/projects/year2/en/latest/lessons/06-sockets.html">python-course.readthedocs.io</a>
> 
> ,
> 
> <a href="https://sky.pro/media/kak-rabotat-s-modulem-socket-v-python/">sky.pro</a>
> 
> .

```python
import socket
serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Разрешение повторного использования адреса (избежать "Address already in use")
serv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_sock.bind(('localhost', 55000))  # или ('', 55000) для всех интерфейсов
serv_sock.listen(5)  # backlog=5, размер очереди ожидающих соединений
print("Сервер ожидает соединения...")
conn, addr = serv_sock.accept()  # Блокировка до подключения клиента
# conn — новый сокет для общения с клиентом, addr — кортеж (IP, port)
with conn:
    print(f"Подключен {addr}")
    while True:
        data = conn.recv(1024)  # Чтение до 1024 байт
        if not data:
            break  # Клиент отключился
        conn.sendall(data.upper())  # Отправка ответа
serv_sock.close()
```

***<span style="color: green">socket.bind(address)</span>*** — привязывает сокет к локальному адресу (хост, порт). Для TCP-сервера обязательно перед `listen`.

***<span style="color: green">socket.listen([backlog])</span>*** — переводит серверный сокет в режим прослушивания входящих соединений. `backlog` — максимальное количество соединений в очереди на обработку

<a href="https://python-course.readthedocs.io/projects/year2/en/latest/lessons/06-sockets.html">python-course.readthedocs.io</a>

.

***<span style="color: green">socket.accept()</span>*** — принимает входящее соединение. Возвращает кортеж `(conn_socket, address)`, где `conn_socket` — новый объект сокета для отправки/получения данных от конкретного клиента, а `address` — адрес клиента. Исходный сокет продолжает слушать новые подключения

<a href="https://javarush.com/quests/lectures/ru.javarush.python.core.lecture.level13.lecture06">javarush.com</a>

.

***<span style="color: green">socket.recv(bufsize[, flags])</span>*** — получает данные из сокета. Возвращает объект bytes. Максимальный размер буфера — `bufsize`. Если соединение закрыто, возвращает пустой байтовый объект `b''`

<a href="https://python-course.readthedocs.io/projects/year2/en/latest/lessons/06-sockets.html">python-course.readthedocs.io</a>

.

***<span style="color: green">socket.send(bytes[, flags])</span>*** — отправляет данные в сокет. Возвращает количество фактически отправленных байт (может быть меньше длины данных из-за заполнения буфера).

***<span style="color: green">socket.sendall(bytes[, flags])</span>*** — отправляет все данные, автоматически обрабатывая фрагментацию (циклически вызывает `send` до полной отправки или возникновения ошибки). Предпочтительнее для TCP

<a href="https://javarush.com/quests/lectures/ru.javarush.python.core.lecture.level13.lecture06">javarush.com</a>

.

## TCP-клиент

> Клиент инициирует соединение (`connect`), отправляет запрос (`sendall`), получает ответ (`recv`) и закрывает сокет. Важно учитывать, что TCP — потоковый протокол: данные могут приходить частями (фрагментация), поэтому для приема сообщений фиксированной длины необходим цикл чтения
> 
> <a href="https://sky.pro/media/kak-rabotat-s-modulem-socket-v-python/">sky.pro</a>
> 
> .

```python
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))  # Подключение к серверу
try:
    sock.sendall('Hello, world'.encode('utf-8'))
    data = sock.recv(1024)  # Может потребоваться цикл для больших данных
    print(data.decode('utf-8'))
finally:
    sock.close()
```

***<span style="color: green">socket.connect(address)</span>*** — устанавливает соединение с сервером по указанному адресу (хост, порт). Для TCP вызывает `ConnectionRefusedError`, если сервер недоступен

<a href="https://javarush.com/quests/lectures/ru.javarush.python.core.lecture.level13.lecture06">javarush.com</a>

.

## UDP (дейтаграммные сокеты)

> В UDP нет понятия “соединения” (connectionless). Сервер просто привязывается к порту (`bind`) и ждет данных. Для отправки/получения используются методы, требующие явного указания адреса
> 
> <a href="https://javarush.com/quests/lectures/ru.javarush.python.core.lecture.level13.lecture06">javarush.com</a>
> 
> .

```python
# UDP-сервер
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 55000))
data, addr = sock.recvfrom(1024)  # Возвращает и данные, и адрес отправителя
print(f"Получено {data} от {addr}")
sock.sendto(b'Response', addr)  # Отправка по конкретному адресу
sock.close()
```

```python
# UDP-клиент
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(b'Hello', ('localhost', 55000))
data, addr = sock.recvfrom(1024)
sock.close()
```

***<span style="color: green">socket.recvfrom(bufsize[, flags])</span>*** — для UDP. Возвращает кортеж `(data, address)`, где `address` — адрес отправителя, необходимый для отправки ответа.

***<span style="color: green">socket.sendto(bytes, address)</span>*** — для UDP. Отправляет дейтаграмму по указанному адресу без предварительного `connect` (хотя `connect` возможен и для UDP для фиксации адреса по умолчанию).

## Управление сокетами

***<span style="color: green">socket.close()</span>*** — закрывает сокет, освобождая системные ресурсы и порт. Рекомендуется