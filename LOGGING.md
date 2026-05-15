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

***<span style="color: green">logger = logging.getLogger(name)</span>***  — создает или получает логгер с именем текущего модуля.

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

## Практический пример настройки logging

```python
import logging

from logging.handlers import RotatingFileHandler
logger = logging.getLogger('app')
logger.setLevel(logging.DEBUG)
logger.propagate = False
formatter = logging.Formatter(
    '%(asctime)s | %(name)s | %(levelname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)
file_handler = RotatingFileHandler(
    'app.log',
    maxBytes=1024 * 1024,
    backupCount=3,
    encoding='utf-8'
)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(console_handler)
logger.addHandler(file_handler)
logger.debug('Отладочная информация')
logger.info('Приложение запущено')
logger.warning('Нестандартная ситуация')
logger.error('Ошибка в обработке данных')
```

## тот же код

```python
import logging
# Импортируем стандартный модуль logging.
# Он нужен для ведения логов: информационных сообщений, предупреждений, ошибок и т.д.
from logging.handlers import RotatingFileHandler
# Из подмодуля logging.handlers импортируем RotatingFileHandler.
# Это обработчик, который пишет логи в файл и автоматически
# делает ротацию, когда файл становится слишком большим.
logger = logging.getLogger('app')
# Создаем или получаем логгер с именем 'app'.
# Имя логгера помогает понимать, откуда пришло сообщение.
# Если логгер с таким именем уже существует, будет возвращен он же.
logger.setLevel(logging.DEBUG)
# Устанавливаем уровень логгера: DEBUG.
# Это значит, что сам логгер готов принимать сообщения всех уровней:
# DEBUG, INFO, WARNING, ERROR, CRITICAL.
# Но итоговый вывод еще зависит и от уровней handlers.
logger.propagate = False
# Отключаем передачу сообщений родительским логгерам.
# Иначе сообщения могли бы уйти выше по иерархии логгеров,
# например в root logger, и тогда возможен дублирующий вывод.
formatter = logging.Formatter(
    '%(asctime)s | %(name)s | %(levelname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
# Создаем объект Formatter — он отвечает за внешний вид логов.
# fmt = шаблон строки лога:
#   %(asctime)s   — время
#   %(name)s      — имя логгера
#   %(levelname)s — уровень сообщения
#   %(message)s   — текст сообщения
# datefmt задает формат даты и времени, например:
# 2026-05-15 14:30:12
console_handler = logging.StreamHandler()
# Создаем обработчик для вывода логов в поток.
# По умолчанию StreamHandler пишет в sys.stderr,
# то есть обычно сообщение видно в консоли/терминале.
console_handler.setLevel(logging.INFO)
# Устанавливаем уровень обработчика консоли: INFO.
# Значит, в консоль будут выведены сообщения уровня:
# INFO, WARNING, ERROR, CRITICAL.
# Сообщения DEBUG в консоль не попадут.
console_handler.setFormatter(formatter)
# Привязываем к обработчику созданный formatter.
# Теперь сообщения в консоли будут оформлены по заданному шаблону.
file_handler = RotatingFileHandler(
    'app.log',
    maxBytes=1024 * 1024,
    backupCount=3,
    encoding='utf-8'
)
# Создаем файловый обработчик с ротацией.
# 'app.log' — имя файла, куда будут записываться логи.
# maxBytes=1024 * 1024 — максимальный размер файла: 1 МБ.
# Когда файл достигает этого размера, выполняется ротация.
# backupCount=3 — хранить до 3 старых файлов лога.
# Обычно это будут app.log.1, app.log.2, app.log.3.
# encoding='utf-8' — кодировка файла, чтобы корректно писать русский текст.
file_handler.setLevel(logging.DEBUG)
# Устанавливаем уровень файлового обработчика: DEBUG.
# В файл будут записаны все сообщения начиная с DEBUG.
# То есть файл получит больше информации, чем консоль.
file_handler.setFormatter(formatter)
# Назначаем тот же formatter файловому обработчику.
# Поэтому формат логов в файле будет таким же, как в консоли.
logger.addHandler(console_handler)
# Подключаем консольный обработчик к логгеру.
# Теперь логгер сможет отправлять сообщения в консоль.
logger.addHandler(file_handler)
# Подключаем файловый обработчик к логгеру.
# Теперь тот же логгер сможет параллельно писать сообщения и в файл.
logger.debug('Отладочная информация')
# Отправляем сообщение уровня DEBUG.
# Логгер его принимает, потому что его уровень = DEBUG.
# Но console_handler его не покажет, потому что у консоли уровень INFO.
# А file_handler запишет это сообщение в app.log.
logger.info('Приложение запущено')
# Сообщение уровня INFO.
# Его пропустит и консольный обработчик, и файловый.
# Поэтому оно будет и в терминале, и в файле.
logger.warning('Нестандартная ситуация')
# Сообщение уровня WARNING.
# Тоже попадет и в консоль, и в файл.
# Обычно так логируют подозрительные, но не критические ситуации.
logger.error('Ошибка в обработке данных')
# Сообщение уровня ERROR.
# Также попадет и в консоль, и в файл.
# Обычно используется, когда операция завершилась ошибкой.
```

Теперь разберу логику работы этого кода по шагам

1. Импортируются инструменты для логирования  
    Сначала подключается модуль logging и специальный обработчик RotatingFileHandler. Это означает, что программа будет не просто печатать сообщения, а вести полноценный журнал работы
    
2. Создается логгер  
    Строка:
    

```python
logger = logging.getLogger('app')
```

создает именованный логгер app. Имя особенно полезно в больших проектах, где есть несколько модулей и несколько логгеров

1. Логгеру задается общий уровень  
    Строка:

```python
logger.setLevel(logging.DEBUG)
```

означает: логгер готов принимать вообще все основные сообщения, начиная с DEBUG

Важно понимать разницу:  
- уровень логгера решает, будет ли сообщение вообще обработано логгером  
- уровень handler решает, попадет ли уже обработанное сообщение в конкретное место вывода

То есть здесь логгер максимально «открыт», а фильтрация идет уже на уровне обработчиков

1. Отключается propagate  
    Строка:

```python
logger.propagate = False
```

запрещает передавать сообщения вверх, например корневому логгеру

Зачем это нужно:  
если где-то в программе уже настроен root logger, то без этого сообщения могли бы:  
- один раз попасть в ваши handlers  
- второй раз уйти в root logger  
- в итоге вы увидели бы дубли

1. Создается formatter  
    Это шаблон, по которому будет оформляться каждая запись лога

Шаблон:

```python
'%(asctime)s | %(name)s | %(levelname)s | %(message)s'
```

дает примерно такой вывод:

```text
2026-05-15 14:30:12 | app | INFO | Приложение запущено
```

Разбор полей:  
- %(asctime)s — дата и время  
- %(name)s — имя логгера, то есть app  
- %(levelname)s — текстовый уровень, например INFO  
- %(message)s — сам текст сообщения

1. Создается обработчик для консоли  
    Строка:

```python
console_handler = logging.StreamHandler()
```

создает вывод в поток, обычно это консоль

Потом:

```python
console_handler.setLevel(logging.INFO)
```

говорит, что в консоль не надо отправлять DEBUG, а только INFO и выше

Итог для консоли:  
- DEBUG — нет  
- INFO — да  
- WARNING — да  
- ERROR — да  
- CRITICAL — да

1. Создается обработчик для файла с ротацией  
    Этот handler пишет логи в файл app.log

Параметры важные:  
- app.log — текущий активный файл лога  
- maxBytes=1024 * 1024 — как только размер достигнет 1 МБ, файл будет «прокручен»  
- backupCount=3 — будет храниться до трех старых версий  
- encoding=‘utf-8’ — русский текст не сломается

Как работает ротация упрощенно:  
- текущий app.log переполняется  
- старый app.log переименовывается, например в app.log.1  
- предыдущие резервные копии сдвигаются  
- создается новый свежий app.log

Это полезно, чтобы лог-файл не рос бесконечно

1. Для файла ставится уровень DEBUG  
    Это означает, что файл будет хранить более подробную информацию, чем консоль

То есть идея кода такая:  
- консоль показывает только важное для пользователя или разработчика в момент запуска  
- файл хранит более полную историю, включая отладочные сообщения

Это очень типичный и правильный подход

1. Оба обработчика добавляются в логгер  
    После:

```python
logger.addHandler(console_handler)
logger.addHandler(file_handler)
```

логгер app начинает рассылать каждое подходящее сообщение в оба направления

Но каждое направление само решает, принимать его или нет, по своему уровню

1. Отправляются сообщения разных уровней  
    Вот что произойдет реально

Для строки:

```python
logger.debug('Отладочная информация')
```

- логгер примет сообщение
- консоль его отбросит, потому что INFO выше DEBUG
- файл запишет

Для строки:

```python
logger.info('Приложение запущено')
```

- логгер примет сообщение
- консоль покажет
- файл запишет

Для строки:

```python
logger.warning('Нестандартная ситуация')
```

- консоль покажет
- файл запишет

Для строки:

```python
logger.error('Ошибка в обработке данных')
```

- консоль покажет
- файл запишет

Итоговый результат работы кода

В консоли вы увидите примерно это:

```text
2026-05-15 14:30:12 | app | INFO | Приложение запущено
2026-05-15 14:30:12 | app | WARNING | Нестандартная ситуация
2026-05-15 14:30:12 | app | ERROR | Ошибка в обработке данных
```

А в файле app.log будет примерно это:

```text
2026-05-15 14:30:12 | app | DEBUG | Отладочная информация
2026-05-15 14:30:12 | app | INFO | Приложение запущено
2026-05-15 14:30:12 | app | WARNING | Нестандартная ситуация
2026-05-15 14:30:12 | app | ERROR | Ошибка в обработке данных
```

Почему такая конфигурация хороша

- консоль не засоряется лишним DEBUG
- файл сохраняет полную картину для разбора проблем
- логи читаемы благодаря formatter
- файл не разрастается бесконечно благодаря RotatingFileHandler
- нет дублей благодаря propagate = False

На что стоит обратить внимание

1. Если этот код выполнить несколько раз в одной и той же сессии Python, можно случайно добавить handlers повторно  
    Тогда сообщения начнут дублироваться

Обычно от этого защищаются так:

```python
if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
```

1. Если нужен вывод именно в stdout, а не stderr, StreamHandler можно создать явно

```python
import sys
console_handler = logging.StreamHandler(sys.stdout)
```

1. Для production часто полезно еще логировать traceback исключений через:

```python
logger.exception('Текст ошибки')
```

1. В больших проектах такую настройку обычно выносят в отдельную функцию или в конфиг

# Ссылки:
[logging — модуль логирования для Python](https://docs.python.org/uk/3/library/logging.html)
[Тонкости работы с логгированием в Python: краткий гайд для разработчиков](https://habr.com/ru/articles/899244)
