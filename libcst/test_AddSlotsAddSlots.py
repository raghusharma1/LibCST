import pytest
import dataclasses
from itertools import chain, filterfalse
from typing import Any, Mapping, Type, TypeVar
from _add_slots import add_slots
import pickle

@pytest.mark.regression
def test_no_slots_defined():
    @dataclasses.dataclass
    class TestClassWithoutSlots:
        a: int
        b: str

    TestClass = add_slots(TestClassWithoutSlots)

    assert '__slots__' in TestClass.__dict__
    assert hasattr(TestClass, 'a')
    assert hasattr(TestClass, 'b')

@pytest.mark.negative
def test_slots_already_defined():
    @dataclasses.dataclass
    class TestClassWithSlots:
        __slots__ = ['a', 'b']
        a: int
        b: str

    with pytest.raises(TypeError):
        TestClass = add_slots(TestClassWithSlots)

@pytest.mark.regression
def test_inherited_slots_mro():
    @dataclasses.dataclass
    class ParentClass:
        __slots__ = ['x']
        x: int

    @dataclasses.dataclass
    class ChildClass(ParentClass):
        y: str

    TestClass = add_slots(ChildClass)

    assert '__slots__' in TestClass.__dict__
    assert hasattr(TestClass, 'x')
    assert hasattr(TestClass, 'y')

@pytest.mark.valid
def test_preservation_of_class_attributes():
    @dataclasses.dataclass
    class TestedClass:
        __a: int
        b: str

    TestClass = add_slots(TestedClass)

    assert '__slots__' in TestClass.__dict__
    assert hasattr(TestClass, '_TestedClass__a')
    assert hasattr(TestClass, 'b')

@pytest.mark.performance
def test_pickle_compatibility():
    @dataclasses.dataclass
    class TestPickleClass:
        a: int
        b: str

    TestClass = add_slots(TestPickleClass)
    instance = TestClass(a=1, b='test')

    pickled_instance = pickle.dumps(instance)
    unpickled_instance = pickle.loads(pickled_instance)

    assert unpickled_instance.a == instance.a
    assert unpickled_instance.b == instance.b
