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
with open(‘source.txt’, ‘rb’) as src, open(‘dest.txt’, ‘wb’) as dst:  
	shutil.copyfileobj(src, dst, length=1024*1024) # 1MB буфер
```

> 💡 Не гарантирует `flush()` на dst — вызови `dst.flush()` или `close()` перед чтением.

### copyfile — копирование содержимого (без метаданных)

***<span style="color: green">shutil.copyfile(src, dst, _, follow_symlinks=True)</span>*** 

|Параметр|Описание|
|---|---|
|`src, dst`|Пути к файлам. **dst должен быть полным именем файла**, не директорией|
|`follow_symlinks=False`|Копировать саму ссылку, а не то, на что она указывает|

python  
shutil.copyfile(‘data.txt’, ‘backup/data_copy.txt’)

Исключения: `SameFileError` (src == dst), `SpecialFileError` (pipe/device).

### copy — + права доступа

***<span style="color: green">shutil.copy(src, dst, _, follow_symlinks=True)</span>*** 

Как `copyfile`, но дополнительно копирует **режим разрешений** (permissions). **Не сохраняет** времена создания/модификации

<a href="https://runebook.dev/ru/docs/python/library/shutil">runebook.dev</a>

.

python

# dst как файл

shutil.copy(‘report.pdf’, ‘/backup/report.pdf’)

# dst как директория — файл копируется с базовым именем

shutil.copy(‘report.pdf’, ‘/backup/’) # → /backup/report.pdf

### copy2 — + полные метаданные ⭐

***<span style="color: green">shutil.copy2(src, dst, _, follow_symlinks=True)</span>*** 

> **Рекомендуемый метод** — сохраняет содержимое, права, времена доступа/модификации, флаги. Использует `copystat()` внутри
> 
> <a href="https://docs.python.org/3/library/shutil.html">docs.python.org</a>
> 
> .

python  
shutil.copy2(‘important.docx’, ‘archive/’)

|Что копирует|copyfile|copy|copy2|
|---|---|---|---|
|Содержимое|✅|✅|✅|
|Права (mode)|❌|✅|✅|
|Времена (atime, mtime)|❌|❌|✅|
|Флаги, extended attributes|❌|❌|✅ (платформозависимо)|

## Копирование метаданных отдельно

### copymode — только права

***<span style="color: green">shutil.copymode(src, dst, _, follow_symlinks=True)</span>*** 

Копирует биты разрешений (mode) с `src` на `dst`. Содержимое, владелец, группа не меняются.

python  
shutil.copymode(‘original.txt’, ‘existing_copy.txt’)

### copystat — права + времена + флаги

***<span style="color: green">shutil.copystat(src, dst, _, follow_symlinks=True)</span>*** 

Копирует: разрешения, время последнего доступа, время модификации, флаги. На Linux также расширенные атрибуты

<a href="https://docs.python.org/3/library/shutil.html">docs.python.org</a>

.

python  
shutil.copystat(‘reference.txt’, ‘target.txt’)

## Рекурсивное копирование директорий

***<span style="color: green">shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False, dirs_exist_ok=False)</span>*** 

|Параметр|Описание|
|---|---|
|`symlinks=True`|Копировать ссылки как ссылки, а не содержимое|
|`ignore`|Callable-фильтр или результат `ignore_patterns()`|
|`copy_function`|Функция для копирования файлов (`copy2` по умолчанию)|
|`ignore_dangling_symlinks=True`|Игнорировать битые ссылки вместо ошибки|
|`dirs_exist_ok=True` _(Python 3.8+)_|Не выбрасывать `FileExistsError` если dst существует|

python

# Простое копирование

shutil.copytree(‘project_v1’, ‘project_v1_backup’)

# С игнорированием **pycache** и .git

shutil.copytree(‘project’, ‘project_clean’,  
ignore=shutil.ignore_patterns(’**pycache**’, ‘*.pyc’, ‘.git’))

# Обновление существующей директории (Python 3.8+)

shutil.copytree(‘src’, ‘dst’, dirs_exist_ok=True)

### ignore_patterns — фабрика фильтров

python  
ignore = shutil.ignore_patterns(’_.tmp’, ‘_.log’, ‘node_modules’)  
shutil.copytree(‘app’, ‘app_backup’, ignore=ignore)

## Удаление директорий

***<span style="color: green">shutil.rmtree(path, ignore_errors=False, onerror=None, _, onexc=None, dir_fd=None)</span>*** 

> ⚠️ **Безвозвратно удаляет** директорию и всё содержимое — не в корзину!
> 
> <a href="https://egorovegor.ru/python-shutil/">egorovegor.ru</a>

|Параметр|Описание|
|---|---|
|`ignore_errors=True`|Пропускать все ошибки|
|`onerror`|Deprecated в Python 3.12, использовать `onexc`|
|`onexc`|Callable `(func, path, excinfo)` для обработки ошибок|

python

# С обработкой ошибок прав доступа

def onexc_handler(func, path, exc_info):  
print(f”Не удалось удалить {path}: {exc_info}“)  
# Можно изменить права и повторить  
os.chmod(path, stat.S_IWRITE)  
func(path)

shutil.rmtree(‘temp_dir’, onexc=onexc_handler)

Проверка защиты от symlink-атак:  
python  
if shutil.rmtree.avoids_symlink_attacks:  
print(“Защита от symlink-атак активна”)

## Перемещение файлов и директорий

***<span style="color: green">shutil.move(src, dst, copy_function=copy2)</span>*** 

Логика:  
- **Если на той же файловой системе** — использует `os.rename()` (атомарно, быстро)  
- **Если разные ФС** — копирует через `copy_function`, затем удаляет `src`

<a href="https://docs.python.org/3/library/shutil.html">docs.python.org</a>

python

# Переименование

shutil.move(‘old_name.txt’, ‘new_name.txt’)

# Перемещение в директорию

shutil.move(‘file.txt’, ‘archive/’)

# С копированием без метаданных (для разных ФС)

shutil.move(‘large_file.dat’, ‘/mnt/backup/’, copy_function=shutil.copy)

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

<a href="https://docs.python.org/uk/3/library/shutil.html">docs.python.org</a>

— официальная документация (украинский перевод, актуально для русскоязычных)

<a href="https://docs-python.ru/standart-library/modul-shutil-python/brief-description/">docs-python.ru</a>

— краткое описание функций shutil

<a href="https://noisycake.ru/notes/os_shutil_shelve/">noisycake.ru</a>

— конспект по os, shutil и shelve

<a href="https://runebook.dev/ru/docs/python/library/shutil">runebook.dev</a>

— практика и типичные ошибки

<a href="https://devhops.ru/code/python/files/shutil/">devhops.ru</a>

— примеры копирования и перемещения