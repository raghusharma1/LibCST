import inspect
import pytest
from abc import ABC
from contextlib import contextmanager
from typing import Callable, cast, ClassVar, Collection, Generic, Iterator, Mapping, Type, TYPE_CHECKING, TypeVar, Union
from libcst._nodes.base import CSTNode
from libcst.metadata.base_provider import BaseMetadataProvider, ProviderT
from libcst.metadata.wrapper import MetadataWrapper
from _metadata_dependent import get_metadata

class Test_MetadataDependentGetMetadata:

    def test_retrieval_of_metadata(self):
        instance = VisitorTransformer() // TODO: Initialize with metadata for a node using a specific provider
        key = None // TODO: The metadata provider
        node = None // TODO: The node to get metadata from
        expected_metadata = None // TODO: The expected metadata
        actual_metadata = instance.get_metadata(key, node)
        assert actual_metadata == expected_metadata, "Retrieved metadata is not as expected."

    def test_undeclared_metadata_dependencies_exception(self):
        instance = VisitorTransformer() // TODO: Initialize without metadata for a node/key
        key = None // TODO: The undeclared key
        node = None // TODO: The node to get metadata from
        with pytest.raises(KeyError) as e:
            instance.get_metadata(key, node)
        assert str(e.value) == f"{key.__name__} is not declared as a dependency in {type(instance).__name__}.METADATA_DEPENDENCIES.", \
            "Expected undeclared dependency exception not raised."

    def test_unset_metadata_exception(self):
        instance = VisitorTransformer() // TODO: Initialize with METADATA_DEPENDENCIES defined but without setting any metadata
        key = None // TODO: The defined key
        node = None // TODO: The node to get metadata from
        with pytest.raises(KeyError) as e:
            instance.get_metadata(key, node)
        assert str(e.value) == f"{key.__name__} is a dependency, but not set; did you forget a MetadataWrapper?", \
            "Expected un-set metadata exception not raised."

    def test_get_metadata_with_default_value(self):
        instance = VisitorTransformer() // TODO: Initialize without setting any metadata
        key = None // TODO: The defined key
        node = None // TODO: The node to get metadata from
        default_value = None // TODO: The default value
        actual_value = instance.get_metadata(key, node, default=default_value)
        assert actual_value == default_value, "Default metadata value not returned."

    def test_lazyvalue_metadata_retrieval(self):
        instance = VisitorTransformer() // TODO: Initialize with metadata set as a LazyValue
        key = None // TODO: The set key
        node = None // TODO: The node to get metadata from
        expected_value = None // TODO: The expected computed value of the LazyValue
        actual_value = instance.get_metadata(key, node)
        assert actual_value == expected_value, "LazyValue not computed and returned correctly."
