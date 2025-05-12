import pytest
import dataclasses
from itertools import chain, filterfalse
from typing import Any, Mapping, Type, TypeVar
from _add_slots import __getstate__

class Test_AddSlotsGetstate:

    @pytest.mark.valid
    def test_all_fields_have_corresponding_attribute(self):
        @dataclasses.dataclass
        class TestDataClass:
            field1: int
            field2: str

        test_instance = TestDataClass(10, 'hello')
        expected_result = {'field1': 10, 'field2': 'hello'}

        assert __getstate__(test_instance) == expected_result

    @pytest.mark.valid
    def test_fields_without_corresponding_attribute(self):
        @dataclasses.dataclass
        class TestDataClass:
            field1: int
            field2: str
            field3: float

        test_instance = TestDataClass(20, 'world')
        expected_result = {'field1': 20, 'field2': 'world'}

        assert __getstate__(test_instance) == expected_result

    @pytest.mark.valid
    def test_mapping_correctness(self):
        @dataclasses.dataclass
        class TestDataClass:
            field1: int
            field2: str

        test_instance = TestDataClass(30, 'python')
        expected_result = {'field1': 30, 'field2': 'python'}

        obtained_result = __getstate__(test_instance)
        assert obtained_result == expected_result
        for key, value in obtained_result.items():
            assert getattr(test_instance, key) == value
