---
date: 17.05.2026
tags: python
authors: AzOV
Abstract:
---
> модуль ***<span style="color: green">APScheduler</span>*** (Advanced Python Scheduler) — мощный инструмент для планирования задач в Python с поддержкой разных типов расписаний, сохранения заданий и интеграции с веб‑фреймворками.

# Установка

```bash
pip install apscheduler
```

# Основные компоненты

- ***<span style="color: green">Scheduler</span>*** — главный объект, управляющий планированием и запуском задач.
    
- ***<span style="color: green">Job</span>*** — запланированная задача (функция + параметры запуска).
    
- ***<span style="color: green">Trigger</span>*** — определяет, _когда_ запускать задачу (интервал, cron‑выражение, конкретная дата).
    
- ***<span style="color: green">Executor</span>*** — отвечает за _выполнение_ задачи (в потоке, процессе и т. д.).
    
- ***<span style="color: green">Job store</span>*** — хранилище задач (память, база данных и др.).
    

# Типы планировщиков

***<span style="color: green">BlockingScheduler</span>*** — блокирует основной поток, подходит для standalone‑скриптов.
    
***<span style="color: green">BackgroundScheduler</span>*** — работает в фоновом потоке, идеален для веб‑приложений (Flask, Django).
    
***<span style="color: green">AsyncIOScheduler</span>*** — для асинхронных приложений на `asyncio`.
    

# Триггеры (Triggers)

***<span style="color: green">Interval trigger</span>*** — запуск через фиксированный интервал:

```python
from apscheduler.schedulers.blocking import BlockingScheduler

def job():
    print("Задача выполняется каждые 5 минут")

scheduler = BlockingScheduler()
scheduler.add_job(job, 'interval', minutes=5)
scheduler.start()
```

**Cron trigger** — синтаксис, похожий на Unix `cron`:

```python
# Каждый день в 17:30
scheduler.add_job(job, 'cron', hour=17, minute=30)

# По понедельникам в 9:00
scheduler.add_job(job, 'cron', day_of_week='mon', hour=9)

# 1‑го числа каждого месяца в 8:00
scheduler.add_job(job, 'cron', day=1, hour=8)
```

***<span style="color: green">Date trigger</span>*** — однократный запуск в заданное время:

```python
from datetime import datetime

# Запуск 25 декабря 2024 года в 15:30
run_date = datetime(2024, 12, 25, 15, 30, 0)
scheduler.add_job(job, 'date', run_date=run_date)
```

# Полный пример с обработкой ошибок

```python
import logging
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor
from datetime import datetime
import atexit

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def backup_database():
    try:
        logger.info(f"Запуск бэкапа базы данных в {datetime.now()}")
        # Код бэкапа...
        logger.info("Бэкап успешно создан")
    except Exception as e:
        logger.error(f"Ошибка при создании бэкапа: {e}")

def send_daily_report():
    logger.info("Отправка ежедневного отчёта...")

# Конфигурация планировщика
executors = {
    'default': ThreadPoolExecutor(20)  # Максимум 20 потоков
}
job_defaults = {
    'coalesce': False,  # Не объединять пропущенные запуски
    'max_instances': 3  # Максимум 3 экземпляра задачи одновременно
}

scheduler = BackgroundScheduler(
    executors=executors,
    job_defaults=job_defaults,
    timezone='Europe/Moscow'  # Указываем часовой пояс
)

# Добавляем задачи
scheduler.add_job(
    backup_database,
    'cron',
    hour=2, minute=0,  # Каждый день в 02:00
    id='daily_backup',
    name='Ежедневный бэкап БД'
)

scheduler.add_job(
    send_daily_report,
    'cron',
    day_of_week='mon-sun', hour=18, minute=0,  # Ежедневно в 18:00
    id='daily_report',
    name='Ежедневный отчёт'
)

# Запускаем планировщик
scheduler.start()
logger.info("Планировщик запущен")

# Корректное завершение при остановке программы
atexit.register(lambda: scheduler.shutdown())
```

# Сохранение задач (Job stores)

По умолчанию задачи хранятся в памяти. Для сохранения между перезапусками используйте БД:

```python
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

jobstores = {
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}
scheduler = BackgroundScheduler(jobstores=jobstores)
```

Поддерживаемые хранилища:

- SQLAlchemy (SQLite, PostgreSQL, MySQL);
    
- MongoDB;
    
- Redis;
    
- ZooKeeper.
    

# Управление задачами

- **Просмотр задач:** ***<span style="color: green">scheduler.get_jobs()</span>***.
    
- **Удаление задачи:** ***<span style="color: green">scheduler.remove_job('job_id')</span>***.
    
- **Пауза/возобновление:** ***<span style="color: green">scheduler.pause_job('job_id') / scheduler.resume_job('job_id')</span>***.
    
- **Обновление:** ***<span style="color: green">scheduler.reschedule_job('job_id', trigger='interval', seconds=30)</span>***.
    

# Обработка сигналов (корректное завершение)

Для production‑среды важно корректно останавливать планировщик:

```python
import signal
import sys

def shutdown(signum, frame):
    logger.info("Получен сигнал остановки. Завершаем работу планировщика...")
    scheduler.shutdown(wait=True)
    sys.exit(0)

signal.signal(signal.SIGINT, shutdown)   # Ctrl+C
signal.signal(signal.SIGTERM, shutdown) # Системный сигнал завершения
```

---

# Плюсы и минусы APScheduler

**Плюсы:**

- Поддержка разных типов расписаний (interval, cron, date).
    
- Сохранение задач в БД.
    
- Гибкая настройка исполнителей и хранилищ.
    
- Интеграция с веб‑фреймворками.
    
- Обработка ошибок и перезапуск задач.
    

**Минусы:**

- Более сложная настройка, чем у `schedule`.
    
- Требует понимания многопоточности/асинхронности.
    
- Для persistence нужна внешняя БД.
    

# Когда использовать APScheduler?

- Автоматизация бэкапов, отчётов, очистки данных.
    
- Периодический сбор данных с API или веб‑страниц.
    
- Отправка уведомлений по расписанию.
    
- Фоновые задачи в веб‑приложениях.