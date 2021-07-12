from marshmallow.schema import Schema, SchemaMeta
from marshmallow import fields

from functools import partial

import typing


class _SchemaFieldsMeta(SchemaMeta):
    def __new__(mcs, name, bases, attrs):
        attr_mapper = _AttrMapper()

        _dataclass = attrs["_dataclass"]
        base_annotations = _dataclass.__annotations__
        for annotation_name in base_annotations:
            if attr_class := attr_mapper.get(_dataclass, base_annotations[annotation_name]):
                attrs[annotation_name] = attr_class()

        cls = super().__new__(mcs, _dataclass.__name__, bases, attrs)

        return cls


def schema(class_):
    def _schema(cls):
        if "_rec" not in cls.__dict__:
            cls._rec = False

        class _Schema(Schema, metaclass=_SchemaFieldsMeta):
            _dataclass = cls

        cls.Schema = _Schema
        return cls

    return _schema(class_)


class _AttrMapper:
    _TYPE_MAPPING = Schema.TYPE_MAPPING
    _NESTED_MAPPING = {
        list: fields.List
    }

    def get(self, base_class: typing.Any, annotation_class: typing.Any) -> partial:
        if isinstance(annotation_class, typing._GenericAlias):  # type: ignore
            return self._typing_hint_handler(base_class, annotation_class)
        return self._base_hint_handler(annotation_class)

    def _typing_hint_handler(self, base_class: typing.Any, annotation_class: typing.Any) -> partial:
        origin_class = annotation_class.__origin__
        class_args = annotation_class.__args__
        if class_args:
            fa = class_args[0]
            req = True

            if "__forward_arg__" in base_class.__dict__:
                nested_schema = fa.__forward_arg__ if fa.__forward_arg__ != base_class.__name__ else base_class
            else:
                nested_schema = fa

            if not nested_schema._rec:
                nested_schema._rec = True
                req = False
                nested_schema = schema(nested_schema)

            if "Schema" in nested_schema.__dict__:
                container_schema = fields.Nested(nested=nested_schema.Schema)
                return partial(self._NESTED_MAPPING.get(origin_class, fields.List), container_schema, required=req)

        return partial(self._TYPE_MAPPING.get(origin_class), required=True)

    def _base_hint_handler(self, annotation_class: typing.Any) -> partial:
        if not (_type := self._TYPE_MAPPING.get(annotation_class)):

            if "Schema" in annotation_class.__dict__:
                return partial(fields.Nested, annotation_class.Schema)

            return partial(fields.Raw, annotation_class)

        return partial(_type, required=True)
