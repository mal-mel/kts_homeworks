import typing
import unittest

from marshmallow.exceptions import ValidationError

from schema_ori.schema_oris import schema


@schema
class Person:
    name: str
    age: int
    height: int
    is_put_in: bool


@schema
class Country:
    name: str
    area: float
    population: int
    president: Person
    goverment: typing.List[Person]


president = {
    "name": "Gvido",
    "age": 65,
    "height": 180,
    "is_put_in": True
}

goverment = [
    {
        "name": 123,
        "age": "twenty five",
        "height": 110,
        "is_put_in": False
    },
    {
        "name": 123,
        "age": 40,
        "height": "many",
        "is_put_in": False
    }
]

country = {
    "name": "PythonLand",
    "area": 3.10,
    "population": 8_200_000,
    "president": president,
    "goverment": goverment
}


class TestCase(unittest.TestCase):
    def test_error(self):
        self.assertRaises(ValidationError, Country.Schema().load, country)


if __name__ == '__main__':
    unittest.main()
