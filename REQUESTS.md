---
date: 01.05.2026
tags:
  - python
  - requests
authors:
Abstract:
---

***HTTP (HyperText Transfer Protocol)*** — прикладной протокол передачи данных на основе клиент-серверной архитектуры запрос-ответ. 
> Модуль `requests` — библиотека Python для выполнения HTTP-запросов, предоставляющая удобный API над низкоуровневым `urllib`. Для установки используется команда `pip install requests`.

# Основные HTTP-методы и их применение

> Модуль `requests` реализует основные HTTP-методы как функции верхнего уровня и методы объекта Session. Каждый метод принимает URL и опциональные параметры для заголовков, данных, аутентификации и пр.

***<span style="color: green">requests.get(url, params=None, \*\*kwargs)</span>*** — отправляет GET-запрос для получения данных с сервера. Параметры запроса передаются через словарь `params`, который автоматически кодируется в строку запроса (query string) после `?`.

***<span style="color: green">requests.post(url, data=None, json=None, \*\*kwargs)</span>*** — отправляет POST-запрос для отправки данных на сервер. Используется для форм, загрузки файлов, создания ресурсов. Тело запроса передается через `data` (dict или bytes) или `json` (автоматическая сериализация и установка Content-Type: application/json).

***<span style="color: green">requests.put(url, data=None, \*\*kwargs)</span>*** — полное обновление ресурса на сервере. Перезаписывает существующий ресурс или создает новый с указанным URI.

***<span style="color: green">requests.patch(url, data=None, \*\*kwargs)</span>*** — частичное обновление ресурса. Изменяет только указанные поля, оставляя остальные без изменений.

***<span style="color: green">requests.delete(url, \*\*kwargs)</span>*** — удаление ресурса по указанному URL.

***<span style="color: green">requests.head(url, \*\*kwargs)</span>*** — отправляет HEAD-запрос, идентичный GET, но возвращает только заголовки без тела ответа. Полезен для проверки существования ресурса и получения метаданных.

***<span style="color: green">requests.options(url, \*\*kwargs)</span>*** — возвращает список методов и параметров, поддерживаемых сервером для данного URL (CORS preflight).

***<span style="color: green">requests.request(method, url, \*\*kwargs)</span>*** — универсальный метод для отправки запроса любого типа, указанного в параметре `method`.

```python
import requests
# GET с параметрами в URL
params = {'q': 'python', 'page': 2}
r = requests.get('https://api.example.com/search', params=params)
print(r.url)  # https://api.example.com/search?q=python&page=2
# POST с данными формы
data = {'username': 'admin', 'password': 'secret'}
r = requests.post('https://example.com/login', data=data)
# POST с JSON
payload = {'title': 'Post', 'body': 'Content', 'userId': 1}
r = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload)
```

# Объект Response и работа с ответом

> Любая функция запроса возвращает объект `Response`, содержащий всю информацию, полученную от сервера: статус-код, заголовки, тело ответа и metadata о запросе.

***<span style="color: green">response.status_code</span>*** — целочисленный код состояния HTTP (200 OK, 404 Not Found, 500 Internal Server Error и т.д.).

***<span style="color: green">response.ok</span>*** — свойство-флажок, True если status_code меньше 400 (успешный запрос).

***<span style="color: green">response.raise_for_status()</span>*** — вызывает исключение HTTPError, если статус-код указывает на ошибку (4xx или 5xx). Рекомендуется для явной обработки ошибок.

***<span style="color: green">response.text</span>*** — содержимое ответа в виде строки Unicode (автоматически декодируется на основе кодировки из Content-Type или анализа содержимого).

***<span style="color: green">response.content</span>*** — содержимое ответа в виде байтов (bytes). Используется для бинарных данных: изображений, PDF, архивов.

***<span style="color: green">response.json(\*\*kwargs)</span>*** — десериализация JSON-ответа в объект Python (dict, list и т.д.). Вызывает исключение JSONDecodeError, если тело не является валидным JSON. Принимает те же параметры, что и встроенный `json.loads()`.

***<span style="color: green">response.headers</span>*** — словарь-объект (регистронезависимый) с заголовками ответа сервера (Content-Type, Server, Set-Cookie и др.).

***<span style="color: green">response.request</span>*** — объект PreparedRequest с информацией об исходном запросе (метод, URL, заголовки, тело).

***<span style="color: green">response.url</span>*** — конечный URL после всех редиректов (если allow_redirects=True, по умолчанию для GET).



```python
import requests  
import os  
  
url = ("https://img.freepik.com/free-photo/cute-kitten-sitting-looking-camera-surrounded-by-flowers-generated-by-artificial-intelligence_25030-66192.jpg?semt=ais_hybrid")  
filename = "cat_2.jpg"  
path = os.path.join('C:\\', 'Users', 'User', 'Pictures', filename)  
  
response = requests.get(url)  
  
if response.status_code == 200:  
    with open(path, 'wb') as file:  
        file.write(response.content)  
    print("Файл загружен")  
else:  
    print(f"Не удалось скачать изображение. Статус код: {response.status_code}")
```


```python
import requests  
  
url = "https://catfact.ninja/fact"  
  
response = requests.get(url, verify=True)  
  
if response.status_code == 200:  
    print(response.text)  
    print(response.json())  
    print(response.url)  
    print(response.headers)
```