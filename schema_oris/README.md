# Schema Oris

Автоматический генератор **marshmallow** схем для произвольного датакласса.

# Установка:

`pip install -i https://test.pypi.org/simple/ schema-oris`

# Примеры:

``` python
@schema
class User:
    name: str
    age: int
    

User.Schema().load({"name": "John", "age": 20})
```

Кажется, что даже в typing анотации умеет:

``` python
import typing


class Wish:
    name: str
    
    
@schema
class User:
    name: str
    age: int
    wishes: typing.List[Wish]
```

И даже в typing рефы:

``` python
import typing


@schema
class User:
    name: str
    age: int
    parents: typing.List["User"]
```
