from marshmallow.exceptions import ValidationError

import unittest

from schema_ori.schema_oris import schema


@schema
class Person:
    username: str
    age: int


valid_data = {
    "username": "Ivan",
    "age": 10
}

invalid_data_value = {
    "username": "Ivan",
    "age": "invalid"
}
invalid_data_key = {
    "username": "Ivan",
    "age": 10,
    "sex": "male"
}


class TestCase(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(Person.Schema().load(valid_data), valid_data)

    def test_invalid_value(self):
        self.assertRaises(ValidationError, Person.Schema().load, invalid_data_value)

    def test_invalid_key(self):
        self.assertRaises(ValidationError, Person.Schema().load, invalid_data_key)


if __name__ == '__main__':
    unittest.main()
