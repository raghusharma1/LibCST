# Importing necessary modules
import pytest
import inspect
from abc import ABC
from contextlib import contextmanager
from typing import Callable, cast, ClassVar, Collection, Generic, Iterator, Mapping, Type, TYPE_CHECKING, TypeVar, Union
from libcst._nodes.base import CSTNode
from libcst.metadata.base_provider import BaseMetadataProvider, ProviderT
from libcst.metadata.wrapper import MetadataWrapper

# Import the __call__ method from the _metadata_dependent module
from _metadata_dependent import __call__

# Marking this class as a pytest test class
@pytest.mark.test_class()
class Test_LazyValueCall:
    
    @pytest.mark.positive()
    def test_callable_result_undefined(self):
        # Arrange
        callable_obj = lambda: 10
        instance = __call__(callable_obj)
        instance.return_value = __call__._UNDEFINED_DEFAULT

        # Act
        result = instance()

        # Assert
        assert result == 10, 'The return value does not match'

    @pytest.mark.positive()
    def test_callable_result_defined(self):
        # Arrange
        callable_obj = lambda: 50
        instance = __call__(callable_obj)
        instance.return_value = 20

        # Act
        result = instance()

        # Assert
        assert result == 20, 'The return value does not match the predefined return value'
  
    @pytest.mark.positive()
    def test_callable_result_matches_return_value(self):
        # Arrange
        callable_obj = lambda: 30
        instance = __call__(callable_obj)
        instance.return_value = __call__._UNDEFINED_DEFAULT

        # Act
        result = instance()

        # Assert
        assert result == 30, 'The return value does not match the callable return value'
        assert instance.return_value == 30, 'The instance return value does not match the callable return value'
