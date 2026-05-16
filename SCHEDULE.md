---
date: 17.05.2026
tags: python
authors: AzOV 
Abstract:
---
> модуль `schedule` в Python — простой инструмент для планирования повторяющихся задач (аналог cron внутри Python‑скриптов).

# Установка

Перед использованием установите библиотеку:

```bash
pip install schedule
```

# Базовый пример

Простой скрипт, выполняющий функцию каждые 10 секунд:

```python
import schedule
import time

def job():
    print("Выполняется запланированная задача…")

# Планируем выполнение задачи каждые 10 секунд
schedule.every(10).seconds.do(job)

# Бесконечный цикл для проверки и запуска задач
while True:
    schedule.run_pending()
    time.sleep(1)  # Пауза 1 секунда, чтобы не нагружать CPU
```

# Синтаксис планирования

Примеры разных вариантов расписания:

- **Каждую минуту:** ***<span style="color: green">schedule.every().minute.do(job)</span>***
    
- **Каждый час:** ***<span style="color: green">schedule.every().hour.do(job)</span>***
    
- **Каждый день в 10:30:** ***<span style="color: green">schedule.every().day.at("10:30").do(job)</span>***
    
- **Каждый понедельник:** ***<span style="color: green">schedule.every().monday.do(job)</span>***
    
- **Каждый понедельник в 13:15:** ***<span style="color: green">schedule.every().monday.at("13:15").do(job)</span>***
    
- **Каждые 2 часа:** ***<span style="color: green">schedule.every(2).hours.do(job)</span>***
    
- **Каждые 5 минут:** ***<span style="color: green">schedule.every(5).minutes.do(job)</span>***
    
- **Каждые N секунд (например, 30):** ***<span style="color: green">schedule.every(30).seconds.do(job)</span>***
    

# Передача аргументов в функцию

Если функция принимает параметры, передайте их в `.do()`:

```python
def greet(name):
    print(f"Привет, {name}!")

schedule.every().day.at("09:00").do(greet, name="Анна")
```

# Управление задачами

### Отмена конкретной задачи

Сохраните ссылку на задачу и отмените её:

```python
job_instance = schedule.every().hour.do(job)
schedule.cancel_job(job_instance)
```

### Очистка всех задач

Чтобы отменить все запланированные задачи:

```python
schedule.clear()
```

### Очистка задач с тегом

Можно помечать задачи тегами и очищать по ним:

```python
schedule.every().day.do(job).tag('daily-tasks')
schedule.every().hour.do(another_job).tag('hourly-tasks')

# Очистить только ежедневные задачи
schedule.clear('daily-tasks')
```

# Продвинутый пример

Полный скрипт с несколькими задачами и обработкой ошибок:

```python
import schedule
import time
import logging

logging.basicConfig(level=logging.INFO)

def backup_database():
    try:
        logging.info("Запуск резервного копирования базы данных…")
        # Здесь код бэкапа
        logging.info("Бэкап успешно создан.")
    except Exception as e:
        logging.error(f"Ошибка при создании бэкапа: {e}")

def send_report():
    logging.info("Отправка ежедневного отчёта…")

def cleanup_temp_files():
    logging.info("Очистка временных файлов…")

# Расписание задач
schedule.every().day.at("02:00").do(backup_database)
schedule.every().monday.at("09:00").do(send_report)
schedule.every().sunday.do(cleanup_temp_files)

# Основной цикл
while True:
    try:
        schedule.run_pending()
        time.sleep(60)  # Проверка каждую минуту
    except KeyboardInterrupt:
        logging.info("Планировщик остановлен пользователем.")
        break
```

---

## Плюсы и минусы модуля `schedule`

**Плюсы:**

- Простой и понятный синтаксис.
    
- Не требует знания cron‑синтаксиса.
    
- Легко интегрируется в Python‑скрипты.
    
- Подходит для лёгких автоматизаций.
    

**Минусы:**

- Нет сохранения расписания между перезапусками (задачи теряются при остановке скрипта).
    
- Работает только в рамках одного процесса.
    
- Для надёжности нужно оборачивать в systemd, Docker или иной менеджер процессов.
    
- Не подходит для высоконагруженных или критически важных задач.