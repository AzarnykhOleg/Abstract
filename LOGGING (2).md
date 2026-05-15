---
date: 12.05.2026
tags:
  - python
authors: AzOV
Abstract:
---
> `logging` —  библиотека для гибкого журналирования событий. Поддерживает иерархическую структуру логгеров, множественные обработчики (handlers), форматирование и фильтрацию сообщений. Альтернатива `print()` для production-кода

```python
import logging
```

# Архитектура: Logger → Handler → Formatter

> → **Logger** - генерирует события → 
> → **Handler** - направляет в назначение (файл/консоль/сеть) → 
> → **Formatter** - определяет внешний вид записи

```bash
Код приложения
    ↓
Logger (уровень, фильтры)
    ↓
Handler (куда писать: файл, stderr, SMTP...)
    ↓
Formatter (как писать: timestamp, уровень, сообщение)
    ↓
Вывод (файл/консоль)
```

## Уровни логирования

|Уровень|Числовое значение|Когда использовать|Метод|
|---|---|---|---|
|**DEBUG**|10|Диагностика, детальный вывод при разработке|**_logger.debug()_**|
|**INFO**|20|Подтверждение нормальной работы|**_logger.info()_**|
|**WARNING**|30|Неожиданное поведение, проблемы в будущем|**_logger.warning()_**|
|**ERROR**|40|Не удалось выполнить функцию|**_logger.error()_**|
|**CRITICAL**|50|Серьёзная ошибка, программа может не работать дальше|**_logger.critical()_**|

> Уровень по умолчанию — **WARNING**. Сообщения ниже установленного уровня игнорируются

# Быстрый старт: basicConfig

_**logging.basicConfig(**kwargs)**_ — быстрая настройка корневого логгера (root). Должен вызываться до первого лог-сообщения

<a href="https://thecode.media/python-logger">thecode.media</a>

.

```python
import logging
# Настройка вывода в файл с указанием уровня и формата
logging.basicConfig(
    filename='app.log',
    filemode='w',  # 'a' — дописывать, 'w' — перезаписывать
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    encoding='utf-8'  # Python 3.9+
)
logging.debug('Отладочное сообщение')
logging.info('Информация')
logging.warning('Предупреждение')
```

### Основные параметры basicConfig

|Параметр|Описание|Пример|
|---|---|---|
|`level`|Минимальный уровень логирования|`logging.INFO`|
|`filename`|Путь к файлу (если не указан — вывод в stderr)|`'logs/app.log'`|
|`filemode`|Режим открытия файла|`'a'` (append), `'w'` (write)|
|`format`|Формат строки лога|`'%(asctime)s %(levelname)s %(message)s'`|
|`datefmt`|Формат даты/времени (как strftime)|`'%d/%m/%Y %H:%M:%S'`|
|`handlers`|Список обработчиков (вместо filename)|`[file_handler, console_handler]`|
|`force`|Перезаписать существующую конфигурацию (Python 3.8+)|`True`|

## Создание логгера (рекомендуемый способ)

Прямое использование `logging.info()` работает с root-логгером. Для модульного подхода используйте **_logging.getLogger(name)_**

<a href="https://docs.python.org/uk/3/library/logging.html">docs.python.org</a>

.

```python
# В каждом модуле создаём логгер с именем модуля
logger = logging.getLogger(__name__)
# Если __name__ = 'my_package.module', иерархия:
# root → my_package → module
logger.info('Сообщение от модуля')
```

> Использование `__name__` позволяет строить иерархию логгеров по структуре пакетов. Дочерние логгеры наследуют настройки родителей, если не имеют собственных handlers
> 
> <a href="https://habr.com/ru/articles/899244">habr.com</a>
> 
> .

## Обработчики (Handlers)

Обработчики определяют **куда** направлять логи.

### Встроенные обработчики

|Класс|Назначение|Импорт|
|---|---|---|
|**_StreamHandler_**|Вывод в поток (stderr/stdout по умолчанию)|`logging.StreamHandler()`|
|**_FileHandler_**|Запись в файл|`logging.FileHandler(filename)`|
|**_RotatingFileHandler_**|Ротация по размеру файла|`logging.handlers.RotatingFileHandler`|
|**_TimedRotatingFileHandler_**|Ротация по времени (ежедневно/ежечасно)|`logging.handlers.TimedRotatingFileHandler`|
|**_SMTPHandler_**|Отправка по email|`logging.handlers.SMTPHandler`|
|**_QueueHandler_**|Асинхронная запись через очередь (неблокирующая)<br><br><a href="https://habr.com/ru/articles/899244">habr.com</a>|`logging.handlers.QueueHandler`|

```python
import logging
from logging.handlers import RotatingFileHandler
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# Консольный обработчик
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)
# Файловый обработчик с ротацией (10 МБ, 5 backups)
file_handler = RotatingFileHandler(
    'app.log', maxBytes=10*1024*1024, backupCount=5
)
file_handler.setLevel(logging.INFO)
# Добавляем обработчики к логгеру
logger.addHandler(console_handler)
logger.addHandler(file_handler)
logger.info('Запишется в файл и возможно в консоль (если INFO >= WARNING)')
logger.warning('Запишется и туда, и туда')
```

### Методы Handler

**_setLevel(level)_** — установить минимальный уровень для этого обработчика (может отличаться от уровня логгера).

**_setFormatter(formatter)_** — назначить форматтер.

**_addFilter(filter)_** — добавить фильтр.

## Форматтеры (Formatters)

Определяют **как** выглядит запись в логе.

```python
formatter = logging.Formatter(
    fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
handler.setFormatter(formatter)
```

### Атрибуты LogRecord (для fmt)

|Атрибут|Описание|Пример|
|---|---|---|
|`%(asctime)s`|Время создания записи|`2025-05-12 14:30:00,123`|
|`%(name)s`|Имя логгера|`my_package.module`|
|`%(levelname)s`|Уровень логирования|`INFO`|
|`%(message)s`|Текст сообщения|`User logged in`|
|`%(filename)s`|Имя файла|