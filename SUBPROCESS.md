---
date: 02.05.2026
tags: python
authors: AzOV
Abstract:
---
> модуль subprocess — стандартная библиотека Python для создания новых процессов, подключения к их входным/выходным/ошибочным каналам и получения кодов возврата. Разработан для замены устаревших функций os.system(), os.spawn_(), os.popen_() и commands.*. Работа модуля существенно зависит от операционной системы из-за различий в командных интерпретаторах, путях поиска исполняемых файлов и доступных командах.

## Основные понятия и различия платформ

> **Процесс** — отдельная запущенная программа, имеющая собственную память, PID, сокеты, I/O. **Поток (thread)** — единица, которой ОС назначает процессорное время, существует только внутри процесса.

### Сравнение Linux/macOS (POSIX) и Windows

<table>
<thead>
<tr>
<th>Аспект</th>
<th>Linux/macOS</th>
<th>Windows</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Оболочка по умолчанию</strong></td>
<td>/bin/sh (bash, zsh)</td>
<td>cmd.exe</td>
</tr>
<tr>
<td><strong>Команды</strong></td>
<td>ls, cat, grep — отдельные программы или встроенные</td>
<td>dir, echo, copy — встроенные команды cmd.exe</td>
</tr>
<tr>
<td><strong>Разделитель путей</strong></td>
<td>/ (прямой слэш)</td>
<td>\ (обратный), но / поддерживается в Python</td>
</tr>
<tr>
<td><strong>Переменные среды</strong></td>
<td><span class="math inline">\(HOME, \)</span>PATH</td>
<td>%USERPROFILE%, %PATH%</td>
</tr>
<tr>
<td><strong>Регистр команд</strong></td>
<td>Чувствителен (LS ≠ ls)</td>
<td>Нечувствителен</td>
</tr>
<tr>
<td><strong>Код возврата</strong></td>
<td>0 — успех, отрицательные — сигналы (-N = сигнал N)</td>
<td>0 — успех, ненулевые — коды ошибок</td>
</tr>
<tr>
<td><strong>Сигналы</strong></td>
<td>SIGTERM (15), SIGKILL (9)</td>
<td>TerminateProcess</td>
</tr>
</tbody>
</table>

### Критическая особенность shell=True

> На Linux `shell=True` запускает команду через /bin/sh. На Windows `shell=True` **обязателен** для встроенных команд (echo, dir), так как они не существуют как отдельные файлы. Создаёт риск инъекций.

```python
# Linux/macos — работает без shell
subprocess.run(['ls', '-l'])
# Windows — ошибка FileNotFoundError
subprocess.run(['ls', '-l'])  # НЕ РАБОТАЕТ
# Windows — правильно
subprocess.run(['dir'], shell=True)
```

## Высокоуровневый интерфейс: subprocess.run()

> Рекомендованный способ (Python 3.5+). Возвращает `CompletedProcess`, автоматически ожидает завершения.

***subprocess.run(args, _, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None)_**

### Ключевые параметры

<table>
<thead>
<tr>
<th>Параметр</th>
<th>Описание</th>
<th>Особенности</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>args</strong></td>
<td>Список <code>['ls', '-l']</code> или строка (при <code>shell=True</code>)</td>
<td>На Windows пути с пробелами требуют обработки</td>
</tr>
<tr>
<td><strong>shell</strong></td>
<td>Выполнение через оболочку</td>
<td>Linux: /bin/sh, Windows: cmd.exe. Требуется для Windows-команд</td>
</tr>
<tr>
<td><strong>capture_output</strong></td>
<td>Перехват stdout и stderr</td>
<td>Эквивалент <code>stdout=PIPE, stderr=PIPE</code></td>
</tr>
<tr>
<td><strong>text</strong></td>
<td>Режим строк (str) вместо байт</td>
<td>Рекомендуется <code>encoding='utf-8'</code> для Windows</td>
</tr>
<tr>
<td><strong>check</strong></td>
<td>Выброс <code>CalledProcessError</code> при ошибке</td>
<td>Рекомендуется для обработки ошибок</td>
</tr>
<tr>
<td><strong>timeout</strong></td>
<td>Таймаут в секундах</td>
<td>Процесс убивается при истечении</td>
</tr>
</tbody>
</table>

### Объект CompletedProcess

- **args** — использованные аргументы
- **returncode** — код возврата (0 = успех)
- **stdout**, **stderr** — перехваченные выводы
- **check_returncode()** — метод, вызывающий исключение при ошибке

```python
import subprocess
import sys
# Кроссплатформенный пример
try:
    if sys.platform == 'win32':
        cmd, shell = ['dir'], True
    else:
        cmd, shell = ['ls', '-l'], False
    
    result = subprocess.run(
        cmd, shell=shell, capture_output=True,
        text=True, encoding='utf-8', check=True
    )
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Ошибка: {e.cmd}, код {e.returncode}")
```

## Низкоуровневый интерфейс: Popen

> Для асинхронного выполнения, потоковой обработки, конвейеров.

**_subprocess.Popen(args, …)_**

<table>
<thead>
<tr>
<th>Метод</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>poll()</strong></td>
<td>Проверка статуса (None = работает)</td>
</tr>
<tr>
<td><strong>wait(timeout=None)</strong></td>
<td>Блокировка до завершения</td>
</tr>
<tr>
<td><strong>communicate(input=None, timeout=None)</strong></td>
<td>Передача stdin, чтение stdout/stderr. <strong>Рекомендуется</strong></td>
</tr>
<tr>
<td><strong>terminate()</strong></td>
<td>Мягкое завершение</td>
</tr>
<tr>
<td><strong>kill()</strong></td>
<td>Принудительное завершение</td>
</tr>
</tbody>
</table>

### Конвейеры между процессами

```python
p1 = subprocess.Popen(['dmesg'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(['grep', 'hda'], stdin=p1.stdout, stdout=subprocess.PIPE)
p3 = subprocess.Popen(['cut', '-f', '3', '-d:'], stdin=p2.stdout, stdout=subprocess.PIPE)
p1.stdout.close()  # Важно для SIGPIPE
p2.stdout.close()
output, _ = p3.communicate()
```

## Перенаправление потоков

<table>
<thead>
<tr>
<th>Константа</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>subprocess.PIPE</strong></td>
<td>Создать канал</td>
</tr>
<tr>
<td><strong>subprocess.STDOUT</strong></td>
<td>stderr → stdout</td>
</tr>
<tr>
<td><strong>subprocess.DEVNULL</strong></td>
<td>/dev/null (игнорирование)</td>
</tr>
</tbody>
</table>

## Безопасность

> **Опасно с пользовательским вводом:**
> 
> ```python
> # Linux: инъекция через ; && ||
> subprocess.run(f'cat {user_input}', shell=True)  # Риск!
> # Windows: инъекция через && || |
> subprocess.run(f'type {user_input}', shell=True)  # Риск!
> # Безопасно: список без shell
> subprocess.run(['cat', user_input])
> ```

## Исключения

<table>
<thead>
<tr>
<th>Исключение</th>
<th>Когда возникает</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>CalledProcessError</strong></td>
<td><code>check=True</code> и ненулевой код</td>
</tr>
<tr>
<td><strong>TimeoutExpired</strong></td>
<td>Превышен <code>timeout</code></td>
</tr>
<tr>
<td><strong>FileNotFoundError</strong></td>
<td>Команда не найдена</td>
</tr>
</tbody>
</table>

## Замена устаревших функций

<table>
<thead>
<tr>
<th>Устаревшее</th>
<th>Замена</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>os.system(cmd)</code></td>
<td><code>subprocess.run(cmd, shell=True)</code></td>
</tr>
<tr>
<td><code>subprocess.call()</code></td>
<td><code>subprocess.run(…).returncode</code></td>
</tr>
<tr>
<td><code>subprocess.check_output()</code></td>
<td><code>subprocess.run(…, capture_output=True, check=True).stdout</code></td>
</tr>
</tbody>
</table>

# Перехват вывода в реальном времени (построчно)
> Перехват вывода в реальном времени (построчно) требуется для длительных процессов (загрузка файлов, сборка проекта, сканирование), где нужно отображать прогресс по мере появления, а не ждать завершения. Функция `run()` и метод `communicate()` не подходят — они буферизируют весь вывод до завершения процесса.

## Базовое решение: Popen + итерация по stdout

> Используем `subprocess.Popen` с `stdout=PIPE` и читаем поток построчно в цикле до завершения процесса. Параметр `bufsize=1` (или `universal_newlines=True` в старых версиях) обеспечивает построчную буферизацию — вывод передается сразу после `\n`, а не накапливается.

**_Popen.stdout.readline()_** — читает одну строку из вывода процесса. Блокирует выполнение до получения строки (включая символ новой строки) или закрытия потока (возвращает пустую строку `''`).

**_Popen.poll()_** — проверяет, завершился ли процесс. Возвращает `None`, если процесс еще работает, или код возврата.

```python
import subprocess
proc = subprocess.Popen(
    ['ping', 'google.com', '-c', '5'] if sys.platform != 'win32' else ['ping', 'google.com', '-n', '5'],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,  # Перенаправляем stderr в stdout
    text=True,                 # Режим строк (автоматически декодирует)
    bufsize=1,                 # Построчная буферизация (требуется text=True или universal_newlines)
    encoding='utf-8'           # Явная кодировка
)
# Чтение построчно до завершения процесса
while True:
    line = proc.stdout.readline()
    if not line and proc.poll() is not None:
        break  # Поток закрыт и процесс завершился
    if line:
        print(f"[LOG] {line.strip()}")  # Обработка строки в реальном времени
# Важно: закрыть поток и дождаться завершения
proc.stdout.close()
proc.wait()
```

## Альтернатива: итератор по файловому объекту

> Объект `Popen.stdout` является файловым объектом с итератором по строкам. Цикл `for` автоматически использует буферизацию и завершается при закрытии потока.

```python
import subprocess
with subprocess.Popen(
    ['ping', 'google.com', '-c', '4'],
    stdout=subprocess.PIPE,
    text=True,
    bufsize=1,
    encoding='utf-8'
) as proc:
    for line in proc.stdout:  # Итерация по строкам в реальном времени
        print(line.strip())
    # При выходе из контекста вызывается wait()
```

## Одновременное чтение stdout и stderr

> Если нужно раздельно обрабатывать stdout и stderr без блокировок, используется `select` (POSIX) или потоки (`threading`). На Windows `select` работает только с сокетами, поэтому для файловых дескрипторов процессов рекомендуется `threading`.

```python
import subprocess
import threading
import sys
def reader(stream, prefix):
    """Читает поток в отдельном потоке"""
    for line in iter(stream.readline, ''):
        print(f"[{prefix}] {line.strip()}")
    stream.close()
proc = subprocess.Popen(
    ['some_command'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    bufsize=1
)
# Запуск потоков для параллельного чтения
threading.Thread(target=reader, args=(proc.stdout, 'OUT')).start()
threading.Thread(target=reader, args=(proc.stderr, 'ERR')).start()
proc.wait()
```

## Платформенные особенности и проблемы

### Буферизация вывода целевой программы

> Некоторые программы (включая Python по умолчанию) буферизируют вывод при перенаправлении в pipe. Для принудительной построчной вывода используются специальные флаги:

<table>
<thead>
<tr>
<th>Команда</th>
<th>Решение</th>
</tr>
</thead>
<tbody>
<tr>
<td>Python script.py</td>
<td><code>python -u script.py</code> (unbuffered) или <code>PYTHONUNBUFFERED=1</code></td>
</tr>
<tr>
<td>Стандартные утилиты Linux</td>
<td><code>stdbuf -oL command</code> (line buffering)</td>
</tr>
<tr>
<td>grep, awk</td>
<td>Обычно работают построчно по умолчанию</td>
</tr>
<tr>
<td>Windows cmd</td>
<td>Может требовать <code>shell=True</code> для встроенных команд, но лучше избегать</td>
</tr>
</tbody>
</table>

### Windows: специфика работы

> На Windows `bufsize=1` работает корректно только с `text=True` или `universal_newlines=True`. Для бинарного режима построчное чтение требует ручной обработки `\n`.

```python
# Windows-специфичный пример с PowerShell
proc = subprocess.Popen(
    ['powershell', '-Command', 'Get-Process | Select-Object -First 10'],
    stdout=subprocess.PIPE,
    text=True,
    bufsize=1,
    encoding='cp866'  # или 'utf-8' для современных Windows
)
```

## Полный кроссплатформенный пример

> Пример с обработкой прерывания (Ctrl+C) и таймаутом мониторинга.

```python
import subprocess
import sys
import time
def stream_output(cmd, timeout=None):
    """Запускает команду и возвращает вывод построчно"""
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
        encoding='utf-8'
    )
    
    start = time.time()
    try:
        for line in proc.stdout:
            yield line
            if timeout and (time.time() - start) > timeout:
                proc.terminate()
                raise TimeoutError(f"Превышен таймаут {timeout}с")
    finally:
        proc.stdout.close()
        proc.wait()
# Использование
for line in stream_output(['ping', '127.0.0.1', '-c', '3']):
    print(f">>> {line.strip()}")
```