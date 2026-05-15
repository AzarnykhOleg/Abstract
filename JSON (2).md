---
date: 
tags: python
authors: GB

Abstract:  
---
### [Сериализация. JSON. CSV.](zotero://open-pdf/library/items/)


# [JSON](zotero://open-pdf/library/items/GMUCHLBQ?page=4&annotation=3YF9J6UH)

	JSON (JavaScript Object Notation) — это популярный формат текстовых данных,  который используется для обмена данными в современных веб- и мобильных  приложениях. Кроме того, JSON используется для хранения неструктурированных  данных в файлах журналов или базах данных NoSQL.

## [Формат JSON](zotero://open-pdf/library/items/GMUCHLBQ?page=4&annotation=PXHGPEGS)

```json
{  
	"id": 2,  
	"name": "Ervin Howell",  
	"username": "Antonette",  
	"email": [  
		"Shanna@melissa.tv",  
		"antonette@howel.com"  
	],  
	"address": {  
		"street": "Victor Plains",  
		"suite": "Suite 879",  
		"city": "Wisokyburgh",  
		"zipcode": "90566-7771",  
		"geo": {  
			"lat": "-43.9509",  
			"lng": "-34.4618"  
		}  
	},  
	"phone": "010-692-6593 x09125",  
	"website": "anastasia.net",  
	"company": {  
		"name": "Deckow-Crist",  
		"catchPhrase": "Proactive didactic contingency",  
		"bs": "synergize scalable supply-chains"  
	} 
}
```

|**Python**|**JSON**|**Python**|
|---|---|---|
|dict|object|dict|
|list, tuple|array|list|
|str|string|str|
|int|number (int)|int|
|float|number (real)|float|
|True|true|True|
|False|false|False|
|None|null|None|

# [Модуль JSON](zotero://open-pdf/library/items/GMUCHLBQ?page=6&annotation=LH9INL7E)

## [Преобразование JSON в Python (десериализация)](zotero://open-pdf/library/items/GMUCHLBQ?page=6&annotation=LXRUALXH)

> Десериализация — процесс преобразования JSON-данных в объекты Python. Модуль json парсит текстовое представление и создает соответствующие структуры данных Python согласно таблице типов.

**<span style="color: green">json.loads(s, _, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, \**kw)</span>** — парсит JSON-строку s и возвращает Python-объект (dict, list, str, int, float, bool или None). Используется для работы с данными, полученными из сети или сгенерированными программно.

```python
import json
json_str = '{"name": "Мария", "age": 25, "active": true}'
data = json.loads(json_str)
print(data)  # {'name': 'Мария', 'age': 25, 'active': True}
print(data['name'])  # Мария
```

**<span style="color: green">json.load(fp, _, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, \**kw)</span>** — читает JSON из файлового объекта fp (открытого в текстовом режиме с кодировкой UTF-8) и десериализует его. Возвращает Python-объект.

```python
with open('data.json', 'r', encoding='utf-8') as f:
    config = json.load(f)
print(config['database_host'])
```

## Параметры десериализации (loads/load)

> Параметры object_hook и object_pairs_hook позволяют кастомизировать процесс создания объектов при декодировании. parse_float, parse_int и parse_constant изменяют обработку числовых литералов.

- **object_hook** — функция, вызываемая для каждого декодированного JSON-объекта (dict). Получает словарь, должен вернуть объект Python. Используется для преобразования JSON в экземпляры классов.
- **object_pairs_hook** — аналогично object_hook, но получает список пар (key, value) для сохранения порядка ключей (важно для OrderedDict).
- **parse_float** — функция для обработки чисел с плавающей точкой (по умолчанию float()). Можно указать decimal.Decimal для точных вычислений.
- **parse_int** — функция для обработки целых чисел (по умолчанию int()).
- **parse_constant** — функция для обработки специальных значений ‘-Infinity’, ‘Infinity’, ‘NaN’.
- **cls** — пользовательский подкласс JSONDecoder для расширенной кастомизации декодирования.

```python
from decimal import Decimal
# Использование Decimal для точности денежных расчетов
json_data = '{"price": 19.99, "quantity": 3}'
result = json.loads(json_data, parse_float=Decimal)
print(result['price'])  # Decimal('19.99')
# Преобразование в экземпляр класса
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"<{self.name}: {self.age}>"
def hook(dct):
    if 'name' in dct and 'age' in dct:
        return User(**dct)
    return dct
user = json.loads('{"name": "Иван", "age": 30}', object_hook=hook)
print(user)  # <Иван: 30>
```

***❗❗❗ При открытии файлов важно учитывать их размер. Огромные  JSON объекты даёт высокую нагрузку на процессор и оперативную память. ***

## [Преобразование Python в JSON (сериализация)](zotero://open-pdf/library/items/GMUCHLBQ?page=8&annotation=B2ND6753)

> Сериализация — процесс преобразования объектов Python в формат JSON (строку или файл). Не все типы Python сериализуемы напрямую; для нестандартных типов требуется кастомная логика через default или cls.

**<span style="color: green">json.dumps(obj, _, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, \**kw)</span>** — сериализует объект Python obj в JSON-форматированную строку. Возвращает str (или bytes в режимах сencoding).

```python
import json
data = {
    "user": "Алексей",
    "age": 28,
    "skills": ["Python", "Docker"],
    "premium": None
}
json_str = json.dumps(data, ensure_ascii=False)
print(json_str)
# {"user": "Алексей", "age": 28, "skills": ["Python", "Docker"], "premium": null}
```

**<span style="color: green">json.dump(obj, fp, _, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, \**kw)</span>** — сериализует объект obj и записывает результат в файловый объект fp (должен поддерживать метод write()).

```python
data = {'logins': 150, 'status': 'active'}
with open('stats.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
```

## Основные различия dump и dumps

|Функция|Возвращает|Использование|Аргументы|
|---|---|---|---|
|**dumps**|str (JSON-строка)|Передача по сети, логирование, хранение в переменной|Только объект для сериализации|
|**dump**|None (записывает в файл)|Сохранение конфигурации, кэширование в файл|Объект + файловый объект fp|

> Функция dump более эффективна по памяти для больших данных, так как записывает порциями, тогда как dumps создает полную строку в памяти перед возвратом.

## Дополнительные параметры dump и dumps

> Параметры форматирования и поведения сериализации позволяют контролировать читаемость, кодировку, обработку специальных типов и безопасность.

**<span style="color: green">ensure_ascii</span>** — (bool, по умолчанию True) если True, все не-ASCII символы экранируются в \uXXXX последовательности. Если False, символы выводятся как есть (требуется кодировка UTF-8).

```python
data = {"город": "Москва"}
print(json.dumps(data))  # "\u0433\u043e\u0440\u043e\u0434": "\u041c\u043e\u0441..."
print(json.dumps(data, ensure_ascii=False))  # "город": "Москва"
```

**<span style="color: green">indent</span>** — (int, str или None) отступы для “красивой печати”. Если число — количество пробелов; если строка — используется как префикс отступа. None (по умолчанию) — компактный формат без переносов строк.

```python
print(json.dumps({'a': 1, 'b': 2}, indent=2))
# {
#   "a": 1,
#   "b": 2
# }
```

**<span style="color: green">sort_keys</span>** — (bool, по умолчанию False) если True, ключи словарей сортируются по алфавиту. Полезно для детерминированного вывода и сравнения JSON-файлов.

```python
print(json.dumps({'z': 1, 'a': 2, 'm': 3}, sort_keys=True))
# {"a": 2, "m": 3, "z": 1}
```

**<span style="color: green">separators</span>** — (tuple (item_separator, key_separator), по умолчанию (‘, ‘, ‘: ‘) при indent=None или (’,‘, ‘: ‘) при indent!=None) — позволяет задать разделители элементов и ключей. Уменьшение пробелов уменьшает размер JSON.

```python
# Максимально компактный JSON без пробелов
compact = json.dumps(data, separators=(',', ':'), ensure_ascii=False)
```

**<span style="color: green">skipkeys</span>** — (bool, по умолчанию False) если True, ключи нестрокового типа (не str) пропускаются вместо вызова TypeError. Иначе TypeError при нестроковых ключах.

```python
data = {(1, 2): "tuple_key", "normal": "value"}
print(json.dumps(data, skipkeys=True))  # Пропустит кортеж-ключ
# {"normal": "value"}
```

**<span style="color: green">default</span>** — (callable или None) функция, вызываемая для объектов, которые нельзя сериализовать стандартно. Должна вернуть сериализуемый объект или вызвать TypeError.

```python
from datetime import datetime
def datetime_handler(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")
data = {'created': datetime.now()}
print(json.dumps(data, default=datetime_handler, ensure_ascii=False))
```

**<span style="color: green">cls</span>** — (класс, по умолчанию JSONEncoder) пользовательский класс кодировщика, наследующий json.JSONEncoder, для переопределения метода default() и кастомной сериализации.

```python
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return super().default(obj)
print(json.dumps({'items': {1, 2, 3}}, cls=CustomEncoder))
# {"items": [1, 2, 3]}
```

**<span style="color: green">allow_nan</span>** — (bool, по умолчанию True) если True, float(‘nan’), float(‘inf’), float(‘-inf’) сериализуются как NaN, Infinity, -Infinity (расширение JSON). Если False — вызывает ValueError для соответствия строгому стандарту JSON.

**<span style="color: green">check_circular</span>** — (bool, по умолчанию True) проверка циклических ссылок в структурах данных (словари, списки, объекты). Если False и есть циклическая ссылка — RecursionError.