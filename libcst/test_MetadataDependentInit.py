# Necessary imports
import inspect
from abc import ABC
from contextlib import contextmanager
from typing import Callable, cast, ClassVar, Collection, Generic, Iterator, Mapping, Type, TYPE_CHECKING, TypeVar, Union
from libcst._nodes.base import CSTNode
from libcst.metadata.base_provider import BaseMetadataProvider, ProviderT
from libcst.metadata.wrapper import MetadataWrapper
from _metadata_dependent import MetadataDependent
import pytest


class Test_MetadataDependentInit:

    def test_metadataresolver_initialization(self):
        md_resolver = MetadataDependent()
        assert isinstance(md_resolver.metadata, dict)
        assert len(md_resolver.metadata) == 0

    def test_add_metadata(self):
        md_resolver = MetadataDependent()
        node = CSTNode()
        md_key = self
        md_value = "test metadata"
        md_resolver.add_metadata(node, md_key, md_value)
        assert md_key in md_resolver.metadata
        assert md_resolver.metadata[md_key] == md_value

    def test_set_metadata(self):
        md_resolver = MetadataDependent()
        node = CSTNode()
        metadata = {"key": "value"}
        md_resolver.set_metadata(node, metadata)
        assert node in md_resolver.metadata
        assert md_resolver.metadata[node] == metadata

    def test_visit_method(self):
        md_resolver = MetadataDependent()
        node = CSTNode()
        md_resolver.visit(node)
        # assuming that the correct visit method for CSTNode is visit_CSTNode
        assert "visit_CSTNode" in md_resolver.metadata

    def test_no_metadata_for_node(self):
        md_resolver = MetadataDependent()
        node = CSTNode()
        # assuming that trying to add metadata for a node without metadata
        # throws a NoMetadataForNodeException
        with pytest.raises(NoMetadataForNodeException):
            md_resolver.add_metadata(node, "key", "value")
        assert node not in md_resolver.metadata
