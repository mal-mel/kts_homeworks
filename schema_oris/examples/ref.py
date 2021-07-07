from datetime import date

import typing

from schema_ori.schema_oris import schema


@schema
class Person:
    first_name: str
    second_name: str
    email: str
    age: int
    height: int
    education: str
    date_birthday: date
    parents: typing.List["Person"]


if __name__ == '__main__':
    mother_data = {
        "first_name": "Kate",
        "second_name": "Chip",
        "email": "kate@gmail.com",
        "age": -35,
        "height": 315,
        "education": "High School",
        "date_birthday": date(2056, 1, 1).isoformat()
    }

    father_data = {
        "first_name": "Alen",
        "second_name": "Petrov",
        "email": "alen@gmail.com",
        "age": 34,
        "height": 150,
        "education": "High School",
        "date_birthday": date(1987, 1, 1).isoformat()
    }

    child_data = {
        "first_name": "John",
        "second_name": "Petrov",
        "email": "john@gmail.com",
        "age": 10,
        "height": 210,
        "education": "Middle School",
        "date_birthday": date(2011, 1, 1).isoformat(),
        "parents": [mother_data, father_data]
    }
    print(Person.Schema().load(child_data))
    print(Person.Schema)
