---
date: 12.05.2026
tags:
  - python
authors: AzOV
Abstract:
---
> Модуль logging предназначен для ведения журнала работы программы: вывода диагностических сообщений, предупреждений, ошибок и другой служебной информации. В отличие от print(), logging позволяет задавать уровни важности сообщений, гибко настраивать формат вывода и направлять логи в консоль, файл или другие источники.

***<span style="color: green">import logging</span>***  — импорт стандартного модуля журналирования.

***<span style="color: green">logging.basicConfig()</span>***  — базовая настройка логирования.

***<span style="color: green">logging.getLogger(name)</span>***  — получение объекта логгера.

***<span style="color: green">❗❗❗ logging — это стандартный способ журналирования в Python. Для учебных и рабочих проектов он почти всегда предпочтительнее обычных print()-сообщений.</span>*** 

## Зачем использовать logging

> Логирование помогает понимать, что происходит в программе во время выполнения: какие этапы уже выполнены, где произошла ошибка, какие значения были получены и какие действия совершала система.

Преимущества logging:

- можно разделять сообщения по уровням важности
- можно отключать лишние сообщения без изменения кода
- можно писать логи и в консоль, и в файл
- можно задавать единый формат записей
- удобно использовать в больших проектах

## Уровни логирования

***<span style="color: green">logging.DEBUG</span>***  — подробная отладочная информация.

***<span style="color: green">logging.INFO</span>***  — обычные информационные сообщения о ходе работы программы.

***<span style="color: green">logging.WARNING</span>***  — предупреждения о потенциальной проблеме.

***<span style="color: green">logging.ERROR</span>***  — ошибка, из-за которой часть логики не выполнилась.

***<span style="color: green">logging.CRITICAL</span>***  — критическая ошибка, из-за которой программа может продолжать работать некорректно или завершиться.

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug('Отладочное сообщение')
logging.info('Информационное сообщение')
logging.warning('Предупреждение')
logging.error('Ошибка')
logging.critical('Критическая ошибка')
```

***<span style="color: green">❗❗❗ По умолчанию без настройки basicConfig() сообщения уровня DEBUG и INFO обычно не отображаются.</span>*** 

## Базовая настройка логирования

***<span style="color: green">logging.basicConfig(level=logging.INFO)</span>***  — включает вывод логов начиная с уровня INFO.

***<span style="color: green">level=…</span>***  — минимальный уровень сообщений, которые будут обрабатываться.

```python
import logging

logging.basicConfig(level=logging.INFO)
logging.debug('Это сообщение не будет показано')
logging.info('Программа запущена')
logging.warning('Найдено подозрительное значение')
```

## Формат сообщений

***<span style="color: green">format=‘%(levelname)s:%(message)s’</span>***  — задает формат записи лога.

Часто используемые поля формата:

- ***<span style="color: green">%(levelname)s</span>***  — уровень сообщения
- ***<span style="color: green">%(message)s</span>***  — текст сообщения
- ***<span style="color: green">%(asctime)s</span>***  — время события
- ***<span style="color: green">%(name)s</span>***  — имя логгера
- ***<span style="color: green">%(filename)s</span>***  — имя файла
- ***<span style="color: green">%(lineno)d</span>***  — номер строки

```python
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(name)s | %(message)s'
)
logging.info('Приложение стартовало')
```

## Формат даты и времени

***<span style="color: green">datefmt=‘%Y-%m-%d %H:%M:%S’</span>***  — задает формат отображения даты.

```python
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logging.info('Сообщение с красивой датой')
```

## Запись логов в файл

***<span style="color: green">filename=‘app.log’</span>***  — направляет логи в файл.

***<span style="color: green">encoding=‘utf-8’</span>***  — задает кодировку файла лога.

***<span style="color: green">filemode=‘w’</span>***  — перезаписывает файл при запуске.

***<span style="color: green">filemode=‘a’</span>***  — дописывает новые сообщения в конец файла.

```python
import logging
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    encoding='utf-8',
    filemode='a'
)
logging.info('Программа запущена')
logging.error('Произошла ошибка')
```

***<span style="color: green">❗❗❗ Если указан filename, то базовая конфигурация обычно пишет в файл, а не в консоль. Для одновременной записи в несколько мест используют handlers.</span>*** 

## Объект логгера

***<span style="color: green">logger = logging.getLogger(**name**)</span>***  — создает или получает логгер с именем текущего модуля.

***<span style="color: green">logger.info(…)</span>***  — отправка сообщения через конкретный логгер.

```python
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('Сообщение от логгера модуля')
```

> Использование отдельных логгеров особенно полезно в больших проектах с несколькими файлами и пакетами.

## Имя логгера

***<span style="color: green">logging.getLogger(‘my_app.database’)</span>***  — логгер с явным именем.

```python
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(name)s | %(levelname)s | %(message)s'
)
logger = logging.getLogger('my_app.database')
logger.info('Подключение к базе установлено')
```

## Передача переменных в лог

***<span style="color: green">logger.info(‘User id=%s’, user_id)</span>***  — рекомендуемый способ подстановки значений.

```python
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
user_id = 42
logger.info('Пользователь вошел в систему: id=%s', user_id)
```

***<span style="color: green">❗❗❗ В logging лучше передавать значения через аргументы, а не собирать строку вручную через f-строки или +, потому что форматирование тогда выполняется только при реальной записи сообщения.</span>*** 

## Логирование исключений

***<span style="color: green">logger.exception(‘Сообщение об ошибке’)</span>***  — записывает сообщение уровня ERROR и traceback текущего исключения.

***<span style="color: green">exc_info=True</span>***  — добавляет traceback к сообщению.

```python
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
try:
    result = 10 / 0
except ZeroDivisionError:
    logger.exception('Ошибка при вычислении')
```

Альтернативный вариант:

```python
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
try:
    data = int('abc')
except ValueError:
    logger.error('Не удалось преобразовать строку в число', exc_info=True)
```

## Обработчики handlers

> Handler определяет, куда именно будут отправляться логи: в консоль, файл, сокет, email и т.д.

***<span style="color: green">logging.StreamHandler()</span>***  — вывод в консоль.

***<span style="color: green">logging.FileHandler(‘app.log’, encoding=‘utf-8’)</span>***  — запись в файл.

***<span style="color: green">logger.addHandler(handler)</span>***  — добавление обработчика логгеру.

```python
import logging
logger = logging.getLogger('my_app')
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('app.log', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
logger.addHandler(console_handler)
logger.addHandler(file_handler)
logger.info('Лог пишется и в консоль, и в файл')
```

## Уровни у обработчиков

***<span style="color: green">handler.setLevel(logging.ERROR)</span>***  — задает уровень отдельно для конкретного обработчика.

```python
import logging
logger = logging.getLogger('my_app')
logger.setLevel(loggi
```


# Ссылки:
[logging — модуль логирования для Python](https://docs.python.org/uk/3/library/logging.html)
[Тонкости работы с логгированием в Python: краткий гайд для разработчиков](https://habr.com/ru/articles/899244)
