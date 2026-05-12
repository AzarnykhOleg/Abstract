---
date: 12.05.2026
tags:
  - python
authors: AzOV
Abstract:
---
> Модуль `shutil` предоставляет **высокоуровневые операции** над файлами и коллекциями файлов: копирование, перемещение, удаление дерева директорий, архивация. Для низкоуровневых операций (открытие, чтение, запись) используй встроенный `open()` или модуль `os`

# Копирование файлов — три уровня

### copyfileobj — низкоуровневое (файловые объекты)

***<span style="color: green">shutil.copyfileobj(fsrc, fdst, length=0)</span>***  - Копирует содержимое файлового объекта `fsrc` в `fdst`. Используется когда уже открыты файловые дескрипторы.

|Параметр|Описание|
|---|---|
|`fsrc`|Исходный файловый объект (должен быть открыт для чтения)|
|`fdst`|Целевой файловый объект (должен быть открыт для записи)|
|`length`|Размер буфера. `0` или отрицательное — копирование без чанкинга|

```python  
with open('source.txt', 'rb') as src, open('dest.txt', 'wb') as dst:  
	shutil.copyfileobj(src, dst, length=1024*1024) # 1MB буфер
```

### copyfile — копирование содержимого (без метаданных)

***<span style="color: green">shutil.copyfile(src, dst, _, follow_symlinks=True)</span>*** 

|Параметр|Описание|
|---|---|
|`src, dst`|Пути к файлам. **dst должен быть полным именем файла**, не директорией|
|`follow_symlinks=False`|Копировать саму ссылку, а не то, на что она указывает|

### copy — + права доступа

***<span style="color: green">shutil.copy(src, dst, _, follow_symlinks=True)</span>***  -  Как `copyfile`, но дополнительно копирует **режим разрешений** (permissions). **Не сохраняет** времена создания/модификации

### dst как файл

***<span style="color: green">shutil.copy(‘report.pdf’, ‘/backup/report.pdf’)</span>*** 

### dst как директория — файл копируется с базовым именем

***<span style="color: green">shutil.copy(‘report.pdf’, ‘/backup/’)</span>***  # → /backup/report.pdf

### copy2 — + полные метаданные ⭐

***<span style="color: green">shutil.copy2(src, dst, _, follow_symlinks=True)</span>***  - **Рекомендуемый метод** — сохраняет содержимое, права, времена доступа/модификации, флаги. Использует `copystat()` внутри.

|Что копирует|copyfile|copy|copy2|
|---|---|---|---|
|Содержимое|✅|✅|✅|
|Права (mode)|❌|✅|✅|
|Времена (atime, mtime)|❌|❌|✅|
|Флаги, extended attributes|❌|❌|✅ (платформозависимо)|

# Копирование метаданных отдельно

### copymode — только права

***<span style="color: green">shutil.copymode(src, dst, _, follow_symlinks=True)</span>***  - Копирует биты разрешений (mode) с `src` на `dst`. Содержимое, владелец, группа не меняются.

### copystat — права + времена + флаги

***<span style="color: green">shutil.copystat(src, dst, _, follow_symlinks=True)</span>***  - Копирует: разрешения, время последнего доступа, время модификации, флаги. На Linux также расширенные атрибуты

# Рекурсивное копирование директорий

***<span style="color: green">shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False, dirs_exist_ok=False)</span>*** 

|Параметр|Описание|
|---|---|
|`symlinks=True`|Копировать ссылки как ссылки, а не содержимое|
|`ignore`|Callable-фильтр или результат `ignore_patterns()`|
|`copy_function`|Функция для копирования файлов (`copy2` по умолчанию)|
|`ignore_dangling_symlinks=True`|Игнорировать битые ссылки вместо ошибки|
|`dirs_exist_ok=True` _(Python 3.8+)_|Не выбрасывать `FileExistsError` если dst существует|

# Простое копирование

***<span style="color: green">shutil.copytree(‘project_v1’, ‘project_v1_backup’)</span>***

# С игнорированием **pycache** и .git

***<span style="color: green">shutil.copytree(‘project’, ‘project_clean’, 
ignore=shutil.ignore_patterns(’**pycache**’, ‘*.pyc’, ‘.git’))</span>***

# Обновление существующей директории (Python 3.8+)

***<span style="color: green">shutil.copytree(‘src’, ‘dst’, dirs_exist_ok=True)</span>***

### ignore_patterns — фабрика фильтров

```python  
ignore = shutil.ignore_patterns('_.tmp', '_.log', 'node_modules')  
shutil.copytree('app', 'app_backup', ignore=ignore)
```

# Удаление директорий

***<span style="color: green">shutil.rmtree(path, ignore_errors=False, onerror=None, _, onexc=None, dir_fd=None)</span>***  - Безвозвратно удаляет** директорию и всё содержимое — не в корзину!

|Параметр|Описание|
|---|---|
|`ignore_errors=True`|Пропускать все ошибки|
|`onerror`|Deprecated в Python 3.12, использовать `onexc`|
|`onexc`|Callable `(func, path, excinfo)` для обработки ошибок|

# Перемещение файлов и директорий

***<span style="color: green">shutil.move(src, dst, copy_function=copy2)</span>*** 

# Переименование

***<span style="color: green">shutil.move(‘old_name.txt’, ‘new_name.txt’)</span>***

# Перемещение в директорию

***<span style="color: green">shutil.move(‘file.txt’, ‘archive/’)</span>***

# С копированием без метаданных (для разных ФС)

***<span style="color: green">shutil.move(‘large_file.dat’, ‘/mnt/backup/’, copy_function=shutil.copy)</span>***

Если `dst` существует и является файлом — перезаписывает (если директория — перемещает внутрь).

## Архивация

***<span style="color: green">shutil.make_archive(base_name, format, root_dir=None, base_dir=None, verbose=0, dry_run=0, owner=None, group=None, logger=None)</span>*** 

|Формат|Описание|
|---|---|
|`zip`|ZIP-архив|
|`tar`|Несжатый TAR|
|`gztar`|Gzip-сжатый TAR (.tar.gz)|
|`bztar`|Bzip2-сжатый TAR|
|`xztar`|XZ-сжатый TAR|

# Ссылки

[Официальная документация](https://docs.python.org/uk/3/library/shutil.html)
[Краткое описание функций shutil](https://docs-python.ru/standart-library/modul-shutil-python/brief-description/)
[    Конспект по os, shutil и shelve](https://noisycake.ru/notes/os_shutil_shelve/)