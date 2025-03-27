import inspect
from typing import Callable, cast, Iterable, List, Mapping, MutableMapping, Optional, TYPE_CHECKING
from libcst._metadata_dependent import MetadataDependent
from libcst._typed_visitor import CSTTypedVisitorFunctions
from libcst._visitors import CSTNodeT, CSTVisitor
from libcst._nodes.base import CSTNode
import pytest
from _batched_visitor import _BatchedCSTVisitor


class Test_BatchedCstVisitorOnVisit:

    def test_on_visit_before_visit_is_not_none(self):
        global_variable = 0

        def modify_global(node):
            nonlocal global_variable
            global_variable = 1

        visitor_methods = _VisitorMethodCollection()
        node = CSTNode()
        batched_visitor = _BatchedCSTVisitor(visitor_methods, before_visit=modify_global)

        batched_visitor.on_visit(node)

        assert global_variable == 1

    def test_on_visit_calling_visit_methods(self):
        global_variable = 0
        def modify_global(node):
            nonlocal global_variable
            global_variable = 1

        visitor_methods = {"visit_CSTNode": [modify_global]}
        node = CSTNode()
        batched_visitor = _BatchedCSTVisitor(visitor_methods)

        batched_visitor.on_visit(node)

        assert global_variable == 1 

    def test_on_visit_return_true(self):
        visitor_methods = _VisitorMethodCollection()
        node = CSTNode()
        batched_visitor = _BatchedCSTVisitor(visitor_methods)

        result = batched_visitor.on_visit(node)

        assert result == True
