import typing
import unittest

from schema_oris.schema_oris import schema


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
        "name": "Sorin Sbarnea",
        "age": 25,
        "height": 110,
        "is_put_in": False
    },
    {
        "name": "Stefano Rivera",
        "age": 40,
        "height": 106,
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
    def test_base(self):
        self.assertEqual(Country.Schema().load(country).data, country)


if __name__ == '__main__':
    unittest.main()
