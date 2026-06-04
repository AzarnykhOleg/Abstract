---
date: 03.06.2025
tags: network
authors: AzOV
Abstract:
---
> curl — это консольная утилита для отправки сетевых запросов (HTTP, HTTPS, FTP и др.) и получения ответов от серверов. Часто используется для тестирования API, загрузки файлов и отладки сетевых взаимодействий.

**_curl_** — основная команда.

**_❗❗❗ curl работает с множеством протоколов, но чаще всего используется для HTTP/HTTPS._**

## Базовый запрос

**_curl_**

**_<a href="https://example.com">https://example.com</a>_**

— отправляет GET-запрос и выводит ответ.

```bash
curl https://example.com
```

> По умолчанию curl делает GET-запрос.

## Указание метода запроса

**_curl -X POST url_** — задать HTTP-метод.

```bash
curl -X POST https://example.com/api
```

**_❗❗❗ Если используется -d, метод POST ставится автоматически._**

## Отправка данных

**_curl -d “key=value” url_** — отправка данных (POST).

```bash
curl -d "name=Ivan&age=25" https://example.com/api
```

**_-d_** — данные формы (application/x-www-form-urlencoded).

### JSON-запрос

```bash
curl -X POST https://example.com/api \
  -H "Content-Type: application/json" \
  -d '{"name": "Ivan"}'
```

## Заголовки

**_curl -H “Header: value” url_** — добавление HTTP-заголовка.

```bash
curl -H "Authorization: Bearer TOKEN" https://api.example.com
```

## Сохранение ответа в файл

**_curl -o file.txt url_** — сохранить в файл.

**_curl -O url_** — сохранить с оригинальным именем.

```bash
curl -o page.html https://example.com
```

## Вывод заголовков

**_curl -i url_** — показать заголовки + тело.

**_curl -I url_** — только заголовки (HEAD-запрос).

```bash
curl -I https://example.com
```

## Подробный режим

**_curl -v url_** — подробный вывод (debug).

```bash
curl -v https://example.com
```

> Показывает весь процесс соединения: DNS, TLS, заголовки.

## Работа с редиректами

**_curl -L url_** — автоматически переходить по редиректам.

```bash
curl -L http://example.com
```

**_❗❗❗ Без -L curl не будет переходить по 301⁄302._**

## Ограничение скорости и таймаут

**_curl –max-time 5 url_** — общий таймаут.

**_curl –limit-rate 100k url_** — ограничение скорости.

```bash
curl --max-time 5 https://example.com
```

## Работа с HTTPS

**_curl -k url_** — игнорировать ошибки SSL.

```bash
curl -k https://self-signed.badssl.com
```

**_❗❗❗ Использовать -k только для тестов — это небезопасно._**

## Аутентификация

**_curl -u user:password url_** — Basic Auth.

```bash
curl -u admin:1234 https://example.com
```

## Cookies

**_curl -c cookies.txt url_** — сохранить cookies.

**_curl -b cookies.txt url_** — отправить cookies.

```bash
curl -c cookies.txt https://example.com
curl -b cookies.txt https://example.com/profile
```

## Загрузка файла

**_curl -F “file=@file.txt” url_** — отправка файла.

```bash
curl -F "file=@image.png" https://example.com/upload
```

## Пайпы и использование в скриптах

**_curl url | command_** — передача вывода.

```bash
curl https://example.com | grep title
```

## Проверка только кода ответа

**_curl -o /dev/null -w “%{http_code}” url_** — получить только статус.

```bash
curl -o /dev/null -w "%{http_code}" https://example.com
```

## Частые сценарии

### Проверка API

```bash
curl -X GET https://api.example.com/users
```

### POST JSON

```bash
curl -X POST https://api.example.com \
  -H "Content-Type: application/json" \
  -d '{"key":"value"}'
```

### Скачать файл

```bash
curl -O https://example.com/file.zip
```

## Краткий вывод

> curl — универсальный инструмент для работы с HTTP и другими протоколами: от простых GET-запросов до тестирования API, загрузки файлов и диагностики сети.

Если хотите, могу сделать продолжение в том же стиле: «curl для REST API (с авторизацией, токенами, pagination)» или сравнение curl vs Postman — что полезнее разобрать дальше