import inspect
from typing import Callable, cast, Iterable, List, Mapping, MutableMapping, Optional, TYPE_CHECKING 
from libcst._metadata_dependent import MetadataDependent 
from libcst._typed_visitor import CSTTypedVisitorFunctions 
from libcst._visitors import CSTNodeT, CSTVisitor 
from libcst._nodes.base import CSTNode
import pytest
from unittest.mock import MagicMock

# Import class to test
from _batched_visitor import _BatchedCSTVisitor


@pytest.mark.regression
class Test_BatchedCstVisitorOnLeaveAttribute:

    @pytest.fixture
    def batched_cst_visitor(self):
        f = MagicMock(return_value=None)
        return _BatchedCSTVisitor({"leave_CSTNode_attribute": [f]})

    @pytest.mark.timing
    def test_on_leave_attribute_calls_correct_method(self, batched_cst_visitor):
        node = CSTNode()
        batched_cst_visitor.on_leave_attribute(node, "attribute")
        f = batched_cst_visitor.visitor_methods["leave_CSTNode_attribute"][0]
        f.assert_called() # f should have been called
        f.assert_called_with(node) # f should have been called with the correct node

    @pytest.mark.smoke
    def test_on_leave_attribute_no_method_in_collection(self):
        batched_cst_visitor = _BatchedCSTVisitor({})
        node = CSTNode()
        # Even if there are no relevant methods in visitor_methods, this line should not raise an error
        batched_cst_visitor.on_leave_attribute(node, "attribute")

    @pytest.mark.positive
    def test_on_leave_attribute_calls_multiple_methods(self):
        f1 = MagicMock(return_value=None)
        f2 = MagicMock(return_value=None)
        batched_cst_visitor = _BatchedCSTVisitor({"leave_CSTNode_attribute": [f1, f2]})
        node = CSTNode()
        batched_cst_visitor.on_leave_attribute(node, "attribute")
        # Both f1 and f2 should have been called
        f1.assert_called()
        f2.assert_called()
        # Both f1 and f2 should have been called with the correct node
        f1.assert_called_with(node)
        f2.assert_called_with(node)
