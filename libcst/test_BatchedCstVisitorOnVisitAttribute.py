import inspect
from typing import Callable, cast, Iterable, List, Mapping, MutableMapping, Optional, TYPE_CHECKING
from libcst import CSTNode
from unittest.mock import Mock
import pytest

def test_on_visit_attribute_regular_node():
    class TestVisitor:
        def visit_CSTNode_attr(self, node: CSTNode):
            return True
    visitor = TestVisitor()
    node = CSTNode()
    _batched_visitor.on_visit_attribute(visitor, node, "attr")
    assert visitor.visit_CSTNode_attr(node)

def test_on_visit_attribute_no_matching_methods():
    class TestVisitor:
        pass
    visitor = TestVisitor()
    node = CSTNode()
    attribute = "attr"
    with pytest.raises(AttributeError):
        _batched_visitor.on_visit_attribute(visitor, node, attribute)

def test_on_visit_attribute_multiple_methods():
    class TestVisitor:
        def visit_CSTNode_attr1(self, node):
            node.test1 = True
        def visit_CSTNode_attr2(self, node):
            node.test2 = True
    visitor = TestVisitor()
    node = CSTNode()
    _batched_visitor.on_visit_attribute(visitor, node, "attr1")
    _batched_visitor.on_visit_attribute(visitor, node, "attr2")
    assert node.test1
    assert node.test2

def test_on_visit_attribute_empty_node():
    class TestVisitor:
        def visit_CSTNode_attr(self):
            pass
    visitor = TestVisitor()
    node = CSTNode()
    with pytest.raises(AttributeError):
        _batched_visitor.on_visit_attribute(visitor, node, "attr")
