---
date: 02.05.2026
tags: python
authors: AzOV
Abstract:
---
   
> Модуль pathlib предоставляет объектно-ориентированный интерфейс для работы с путями и файловой системой. Он считается современным и более удобным способом работы с путями по сравнению с os.path.
    
**Path** — основной класс для представления пути к файлу или каталогу.
    
**from pathlib import Path** — стандартный способ импорта модуля.
    
**Path(‘file.txt’)** — создает объект пути. Сам по себе объект не создает файл на диске.
    
```python
from pathlib import Path

 p = Path('notes/file.txt')
 print(p)
 print(type(p))
```
    
**_❗❗❗ Объект Path описывает путь, но не обязательно означает, что такой файл или каталог уже существует._**
    
## Создание объекта пути
    
**Path(‘folder/file.txt’)** — путь из строки.
    
**Path.home()** — путь к домашнему каталогу пользователя.
    
**Path.cwd()** — путь к текущей рабочей директории.
    
**Path(‘/etc’) / ‘nginx’ / ‘nginx.conf’** — удобное объединение путей через оператор /.
    
```python
from pathlib import Path

p1 = Path('data/report.txt')
p2 = Path.home()
p3 = Path.cwd()
p4 = Path('/etc') / 'nginx' / 'nginx.conf'
print(p1)
print(p2)
print(p3)
print(p4)
```
    
## Основные свойства пути
    
**path.name** — имя файла или последней части пути.
    
**path.stem** — имя файла без последнего расширения.
    
**path.suffix** — последнее расширение файла.
    
**path.suffixes** — список всех расширений.
    
**path.parent** — родительский каталог.
    
**path.parts** — кортеж компонентов пути.
    
**path.anchor** — корень пути, например / или C:\.
    
```python
from pathlib import Path

p = Path('/home/user/archive.tar.gz')
print(p.name)       # archive.tar.gz
print(p.stem)       # archive.tar
print(p.suffix)     # .gz
print(p.suffixes)   # ['.tar', '.gz']
print(p.parent)     # /home/user
print(p.parts)      # ('/', 'home', 'user', 'archive.tar.gz')
print(p.anchor)     # /
```
    
## Формирование и преобразование пути
    
**path / ‘child’** — добавляет компонент к пути.
    
**path.joinpath(‘child’, ‘file.txt’)** — объединяет части пути.
    
**path.resolve()** — возвращает абсолютный нормализованный путь.
    
**path.absolute()** — возвращает абсолютный путь.
    
**path.with_name(‘new.txt’)** — заменяет имя файла.
    
**path.with_suffix(‘.md’)** — заменяет расширение файла.
    
```python
from pathlib import Path

p = Path('docs') / 'lesson1.txt'
print(p.resolve())
print(p.absolute())
print(p.with_name('lesson2.txt'))
print(p.with_suffix('.md'))
```
    
**_❗❗❗ Метод resolve() часто удобнее, чем absolute(), так как дополнительно нормализует путь и обрабатывает относительные сегменты._**
    
## Проверка существования и типа объекта
    
**path.exists()** — существует ли путь.
    
**path.is_file()** — является ли путь файлом.
    
**path.is_dir()** — является ли путь каталогом.
    
**path.is_symlink()** — является ли путь символической ссылкой.
    
**path.is_absolute()** — является ли путь абсолютным.
    
```python
from pathlib import Path

p = Path('example.txt')
print(p.exists())
print(p.is_file())
print(p.is_dir())
print(p.is_symlink())
print(p.is_absolute())
```
    
##     Создание каталогов
    
**path.mkdir()** — создает один каталог.
    
**path.mkdir(parents=True, exist_ok=True)** — создает каталог вместе с промежуточными родительскими каталогами и не вызывает ошибку, если он уже существует.
    
```python
from pathlib import Path

Path('new_folder').mkdir()
Path('parent/child/grandchild').mkdir(parents=True, exist_ok=True)
```
    
**parents=True** — аналог поведения os.makedirs(…).
    
**exist_ok=True** — подавляет ошибку при существовании каталога.
    
## Создание, чтение и запись файлов
    
**path.touch()** — создает пустой файл, если он не существует.
    
**path.read_text(encoding=‘utf-8’)** — читает текст из файла.
    
**path.write_text(data, encoding=‘utf-8’)** — записывает текст в файл.
    
**path.read_bytes()** — читает содержимое файла в байтах.
    
**path.write_bytes(data)** — записывает байты в файл.
    
```python
from pathlib import Path

file_path = Path('notes.txt')
file_path.touch()
file_path.write_text('Привет, pathlib!', encoding='utf-8')
text = file_path.read_text(encoding='utf-8')
print(text)
```
    
**_❗❗❗ write_text() и write_bytes() полностью перезаписывают файл. Если нужно добавление в конец, лучше использовать обычный open() через path.open()._**
    
##    Открытие файлов
    
**path.open(mode=‘r’, encoding=‘utf-8’)** — открывает файл так же, как встроенная функция open(), но вызывается как метод объекта Path.
    
```python
from pathlib import Path

path = Path('data.txt')
with path.open('w', encoding='utf-8') as f:
    f.write('Первая строка\n')
with path.open('a', encoding='utf-8') as f:
    f.write('Вторая строка\n')
with path.open('r', encoding='utf-8') as f:
    print(f.read())
```
    
## Удаление файлов и каталогов
    
**path.unlink()** — удаляет файл или символическую ссылку.
    
**path.rmdir()** — удаляет пустой каталог.
    
```python
from pathlib import Path

Path('temp.txt').unlink()
Path('empty_folder').rmdir()
```
    
**_❗❗❗ Метод rmdir() удаляет только пустой каталог. Если внутри есть файлы или подкаталоги, возникнет ошибка. Для рекурсивного удаления обычно используют shutil.rmtree()._**
    
##    Переименование и перемещение
    
**path.rename(target)** — переименовывает или перемещает файл/каталог.
    
**path.replace(target)** — переименовывает или перемещает с заменой целевого пути, если это допускается ОС.
    
```python
from pathlib import Path

src = Path('old_name.txt')
dst = Path('archive/new_name.txt
```




