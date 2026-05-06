---
date: 29.04.2026
tags:
  - python
  - socket
authors:
Abstract:
---

	Модуль socket — встроенная библиотека Python для низкоуровневого сетевого программирования, предоставляющая интерфейс к системным сокетам BSD (Berkeley Software Distribution). Позволяет создавать клиент-серверные приложения, использующие протоколы TCP (надежный потоковый обмен) и UDP (быстрая доставка дейтаграмм без гарантий)

# Основные понятия

> **Сокет** — конечная точка (“розетка”) двустороннего канала связи между двумя программами по сети. Идентифицируется комбинацией IP-адреса (идентификатор устройства в сети, аналог адреса дома) и номера порта (идентификатор приложения на устройстве, аналог номера квартиры)

> **TCP (SOCK_STREAM)** — протокол с установлением соединения (connection-oriented). Обеспечивает надежную, упорядоченную доставку потока байтов без потерь и дублирования. Используется для HTTP, FTP, почты.

> **UDP (SOCK_DGRAM)** — протокол без установления соединения (connectionless). Отправляет независимые дейтаграммы без гарантии доставки, порядка или отсутствия дубликатов. Быстрее TCP, используется для потокового видео, онлайн-игр, DNS-запросов

# Создание сокета

***<span style="color: green">socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)</span>*** — фабричная функция, создающая и возвращающий объект сокета.

- **family** — семейство адресов: 
***AF_INET*** (IPv4, по умолчанию), 
***AF_INET6*** (IPv6), 
***AF_UNIX*** (локальные Unix-сокеты).
- **type** — тип сокета: 
***SOCK_STREAM*** (TCP), 
***SOCK_DGRAM*** (UDP), 
***SOCK_RAW*** (низкоуровневый доступ).
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

# Основные методы сокета

***<span style="color: green">socket.bind(address)</span>*** — привязывает сокет к локальному адресу (хост, порт). Для TCP-сервера обязательно перед `listen`.

***<span style="color: green">address --> (host, port)</span>***

***<span style="color: green">socket.listen([backlog])</span>*** — переводит серверный сокет в режим прослушивания входящих соединений. `backlog` — максимальное количество соединений в очереди на обработку

***<span style="color: green">socket.accept()</span>*** — принимает входящее соединение. Возвращает кортеж `(conn_socket, address)`, где `conn_socket` — новый объект сокета для отправки/получения данных от конкретного клиента, а `address` — адрес клиента. Исходный сокет продолжает слушать новые подключения

***<span style="color: green">socket.connect(address)</span>*** — устанавливает соединение с сервером по указанному адресу (хост, порт). Для TCP вызывает `ConnectionRefusedError`, если сервер недоступен

***<span style="color: green">socket.connect_ex(address)</span>*** — используется для установления TCP-соединения с удаленным сервером и возвращает индикатор ошибки вместо того, чтобы поднимать исключение в случае сбоя соединения.

***<span style="color: green">socket.send(bytes[, flags])</span>*** — отправляет данные в сокет. Возвращает количество фактически отправленных байт (может быть меньше длины данных из-за заполнения буфера).

***<span style="color: green">socket.sendall(bytes[, flags])</span>*** — отправляет все данные, автоматически обрабатывая фрагментацию (циклически вызывает `send` до полной отправки или возникновения ошибки). Предпочтительнее для TCP

***<span style="color: green">socket.sendto(bytes, address)</span>*** — для UDP. Отправляет дейтаграмму по указанному адресу без предварительного `connect` (хотя `connect` возможен и для UDP для фиксации адреса по умолчанию).

***<span style="color: green">socket.recv(bufsize[, flags])</span>*** — получает данные из сокета. Возвращает объект bytes. Максимальный размер буфера — `bufsize`. Если соединение закрыто, возвращает пустой байтовый объект `b''`

***<span style="color: green">socket.recvfrom(bufsize[, flags])</span>*** — для UDP. Возвращает кортеж `(data, address)`, где `address` — адрес отправителя, необходимый для отправки ответа.

***<span style="color: green">socket.close()</span>*** — закрывает сокет, освобождая системные ресурсы и порт. Рекомендуется

## TCP-сервер

> Алгоритм работы сервера на TCP: создание сокета → привязка к адресу (`bind`) → перевод в режим прослушивания (`listen`) → принятие соединения (`accept`, блокирующий вызов) → обмен данными → закрытие

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



## TCP-клиент

> Клиент инициирует соединение (`connect`), отправляет запрос (`sendall`), получает ответ (`recv`) и закрывает сокет. Важно учитывать, что TCP — потоковый протокол: данные могут приходить частями (фрагментация), поэтому для приема сообщений фиксированной длины необходим цикл чтения


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


## UDP (дейтаграммные сокеты)

> В UDP нет понятия “соединения” (connectionless). Сервер просто привязывается к порту (`bind`) и ждет данных. Для отправки/получения используются методы, требующие явного указания адреса

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



## Паттерны корректной работы с TCP-фрагментацией

```python
import socket
def send_all(sock, data):
    """Гарантированная отправка всех байтов"""
    total_sent = 0
    while total_sent < len(data):
        sent = sock.send(data[total_sent:])
        if sent == 0:
            raise ConnectionError("Соединение разорвано")
        total_sent += sent
def recv_exact(sock, n):
    """Прием ровно n байт (обработка фрагментации TCP)"""
    chunks = []
    received = 0
    while received < n:
        chunk = sock.recv(n - received)
        if not chunk:
            raise ConnectionError("Соединение закрыто до получения всех данных")
        chunks.append(chunk)
        received += len(chunk)
    return b''.join(chunks)
# Пример полноценного эхо-клиента с контекстным менеджером
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(10)
    s.connect(('localhost', 55000))
    
    # Отправка длины сообщения (протокол с фреймированием)
    message = "Привет, сервер!".encode('utf-8')
    header = len(message).to_bytes(4, 'big')  # 4 байта на длину
    send_all(s, header + message)
    
    # Получение ответа
    resp_header = recv_exact(s, 4)
    resp_len = int.from_bytes(resp_header, 'big')
    response = recv_exact(s, resp_len)
    print(response.decode('utf-8'))
```

## Сравнительная таблица TCP vs UDP

<table>
<thead>
<tr>
<th>Характеристика</th>
<th>TCP (Transmission Control Protocol)</th>
<th>UDP (User Datagram Protocol)</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Тип соединения</strong></td>
<td>С установлением соединения (connection-oriented) <a href="https://ip-calculator.ru/blog/networking/tcp-vs-udp/">ip-calculator.ru</a></td>
<td>Без установления соединения (connectionless)</td>
</tr>
<tr>
<td><strong>Установление связи</strong></td>
<td>Трёхстороннее рукопожатие (SYN → SYN-ACK → ACK) <a href="https://habr.com/ru/articles/732794/">habr.com</a></td>
<td>Нет рукопожатия, отправка сразу</td>
</tr>
<tr>
<td><strong>Надёжность</strong></td>
<td>Гарантия доставки (ACK, повторная отправка) <a href="https://teta-arm.ru/raznitsa-mezhdu-tcp-i-udp-portami-ischerpyvayuschee-rukovodstvo-s-prakticheskimi-primerami/">teta-arm.ru</a></td>
<td>Нет гарантии (“fire and forget”)</td>
</tr>
<tr>
<td><strong>Упорядоченность</strong></td>
<td>Данные приходят в порядке отправки (последовательная нумерация)</td>
<td>Нет гарантии порядка (приложение само управляет)</td>
</tr>
<tr>
<td><strong>Контроль перегрузки</strong></td>
<td>Да (slow start, congestion window) <a href="https://habr.com/ru/articles/732794/">habr.com</a></td>
<td>Нет</td>
</tr>
<tr>
<td><strong>Управление потоком</strong></td>
<td>Да (flow control, sliding window)</td>
<td>Нет</td>
</tr>
<tr>
<td><strong>Размер заголовка</strong></td>
<td>20-60 байт <a href="https://habr.com/ru/articles/732794/">habr.com</a></td>
<td>8 байт</td>
</tr>
<tr>
<td><strong>Тип передачи</strong></td>
<td>Поток байт (stream), границы сообщений не сохраняются</td>
<td>Дейтаграммы (datagram), сохраняются границы</td>
</tr>
<tr>
<td><strong>Адресация</strong></td>
<td>Unicast (точка-точка)</td>
<td>Unicast, Multicast, Broadcast</td>
</tr>
<tr>
<td><strong>Скорость</strong></td>
<td>Медленнее (накладные расходы на надёжность)</td>
<td>Быстрее (минимальная задержка)</td>
</tr>
<tr>
<td><strong>Применение</strong></td>
<td>HTTP/HTTPS, FTP, SMTP, SSH</td>
<td>DNS, VoIP, потоковое видео, онлайн-игры</td>
</tr>
</tbody>
</table>

# Последовательность вызовов API сокетов и поток данных TCP

## Схема взаимодействия « Клиент-Сервер »

```python
СЕРВЕР                              КЛИЕНТ
  |                                    |
  |  socket()                          |  socket()
  |     ↓                              |     ↓
  |  bind()  ←——— (IP, PORT) ———→      |
  |     ↓                              |     ↓
  |  listen()                          |  connect()
  |     ↓                              |     ↓
  |  accept()  ←—— SYN ————————→       |
  |     ↓                              |     ↓
  |  ←————←—— SYN+ACK ——————————→      |
  |     ↓                              |     ↓
  |  ←————←—— ACK —————————————→       |  установлено
  |     ↓                              |     ↓
  |  ←——— соединение установлено ———→  |
  |     ↓                              |     ↓
  |  recv()  ←——————————————————→      |  send()
  |     ↓                              |     ↓
  |  send()  ←——————————————————→      |  recv()
  |     ↓                              |     ↓
  |  ... обмен данными ...             |  ... обмен данными ...
  |     ↓                              |     ↓
  |  close()  ←—— FIN —————————→       |  close()
  |     ↓                              |     ↓
  |  ←————←—— FIN+ACK —————————→       |
  |     ↓                              |     ↓
  |  ←————←—— ACK —————————————→       |
```

# Этапы TCP-сессии

> **1. Установление соединения (Three-way Handshake)**
> 
> ***<span style="color: green">socket()</span>*** → ***<span style="color: green">bind()</span>*** → ***<span style="color: green">listen()</span>*** (сервер)
> 
> ***<span style="color: green">socket()</span>*** → ***<span style="color: green">connect()</span>*** (клиент) → отправка SYN
> 
> Сервер вызывает ***<span style="color: green">accept()</span>***, получает SYN, отправляет SYN+ACK
> 
> Клиент получает SYN+ACK, отправляет ACK → соединение ESTABLISHED
> 
> **2. Передача данных**
> 
> ***<span style="color: green">send()</span>*** / ***<span style="color: green">sendall()</span>*** — отправка данных (с буферизацией и фрагментацией)
> 
> ***<span style="color: green">recv()</span>*** — приём данных (возвращает доступные байты, может быть меньше запрошенного)
> 
> > Важно: TCP — потоковый протокол. Границы сообщений не сохраняются. Для фиксированных сообщений используйте префикс длины или разделители.
> 
> **3. Разрыв соединения (Four-way Handshake)**
> 
> Вызывающий ***<span style="color: green">close()</span>*** отправляет FIN
> 
> Противоположная сторона получает FIN (***<span style="color: green">recv()</span>*** возвращает пустые байты `b''`), отправляет ACK
> 
> Противоположная сторона вызывает ***<span style="color: green">close()</span>***, отправляет FIN
> 
> Исходная сторона отправляет ACK → TIME_WAIT → закрытие

# Жизненный цикл сокета в коде

```python
import socket
# === СЕРВЕР ===
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', 55000))    # Назначение адреса
    s.listen(5)                    # Переход в режим прослушивания
    
    conn, addr = s.accept()        # Блокировка до подключения
    with conn:                     # conn — новый сокет для клиента
        while True:
            data = conn.recv(1024) # Чтение потока
            if not data:           # Клиент закрыл соединение (FIN)
                break
            conn.sendall(data)     # Отправка ответа
# === КЛИЕНТ ===
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('localhost', 55000)) # Установка соединения (SYN/SYN-ACK/ACK)
    s.sendall(b'Hello')             # Отправка данных
    data = s.recv(1024)             # Получение ответа
    # При выходе из контекста — graceful shutdown (FIN)
```

# Значение сокетов в кибербезе
### Для специалистов в области **кибербезопасности**
- анализировать сетевой трафик и выявлять аномалии,
- распознавать признаки подозрительных соединений (например, reverse shell),
- разрабатывать honeypot-сервисы для выявления активности злоумышленников,
- тестировать уязвимости приложений на уровне сетевого взаимодействия
### Для пентестеров
- реализовывать кастомные сканеры портов,
- имитировать сетевые атаки (например, SYN-флуд, spoofing, MITM),
- разрабатывать и использовать обратные подключения (reverse shell, bind shell),
- взаимодействовать напрямую с удалёнными сервисами, минуя высокоуровневые инструменты.






# Ссылки
## [Документация](https://docs.python.org/3/library/socket.html)
## [Модуль socket в Python: от основ к сложным сетевым приложениям](https://sky.pro/wiki/media/kak-rabotat-s-modulem-socket-v-python/)
1. [Создание простого TCP-сервера с помощью socket в Python](https://sky.pro/wiki/media/kak-rabotat-s-modulem-socket-v-python/#section-1)
2. [Разработка TCP-клиента: взаимодействие с сервером](https://sky.pro/wiki/media/kak-rabotat-s-modulem-socket-v-python/#section-2)
3. [Реализация UDP протокола в модуле socket Pytho](https://sky.pro/wiki/media/kak-rabotat-s-modulem-socket-v-python/#section-3)
4. [Неблокирующие сокеты и мультиплексирование ввода-вывода](https://sky.pro/wiki/media/kak-rabotat-s-modulem-socket-v-python/#section-5)
5. [Параметры сокетов и опции](https://sky.pro/wiki/media/kak-rabotat-s-modulem-socket-v-python/#section-6)
6. [DNS и сетевые функции](https://sky.pro/wiki/media/kak-rabotat-s-modulem-socket-v-python/#section-7)
7. [Асинхронное программирование с сокетами](https://sky.pro/wiki/media/kak-rabotat-s-modulem-socket-v-python/#section-8)
8. [SSL/TLS шифрование](https://sky.pro/wiki/media/kak-rabotat-s-modulem-socket-v-python/#section-9)

## [Руководство по программированию сокетов на Python](https://habr.com/ru/companies/skillfactory/articles/690186/)