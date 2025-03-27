import pytest
import inspect
from abc import ABC
from contextlib import contextmanager
from typing import Callable, cast, ClassVar, Collection, Generic, Iterator, Mapping, Type, TYPE_CHECKING, TypeVar, Union
from libcst._nodes.base import CSTNode
from libcst.metadata.base_provider import BaseMetadataProvider, ProviderT
from libcst.metadata.wrapper import MetadataWrapper
from _metadata_dependent import resolve


class Test_MetadataDependentResolve:

    def test_resolve_with_inherited_dependencies(self):
        # Arrange
        class SomeMetadataProvider(BaseMetadataProvider):
            pass
        metadata_wrapper = MetadataWrapper()
        provider = SomeMetadataProvider()

        # Act
        with provider.resolve(metadata_wrapper):
            pass

        # Assert
        # TODO: Validate if the dependencies are correctly cached in self.metadata
        # and reset after scope, would require inspecting private members or
        # catching side effects through methods this cache is used in, which goes
        # beyond resolving the dependencies and therefore is not done here.

    def test_resolve_without_inherited_dependencies(self):
        # Arrange
        class SomeMetadataProvider(BaseMetadataProvider):
            pass
        metadata_wrapper = MetadataWrapper()
        provider = SomeMetadataProvider()

        # Act
        with provider.resolve(metadata_wrapper):
            pass

        # Assert
        # TODO: Validate if no dependencies have been resolved, would require 
        # inspecting private members or catching side effects through methods 
        # this cache is used in, which goes beyond resolving the dependencies 
        # and therefore is not done here.

    def test_resolve_with_non_existent_dependencies(self):
        # Arrange
        class SomeMetadataProvider(BaseMetadataProvider):
            METADATA_DEPENDENCIES = (NonExistentMetadataProvider,)
        metadata_wrapper = MetadataWrapper()
        provider = SomeMetadataProvider()

        # Act
        with pytest.raises(Exception):
            with provider.resolve(metadata_wrapper):
                pass

        # Assert: Exception should have been raised due to non-existent dependencies
