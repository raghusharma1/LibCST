import pytest
from typing import Optional, TYPE_CHECKING, Union
from libcst._nodes.expression import BinaryOperation, Name, Integer
from libcst._nodes.op import Add, Subtract, Multiply
from libcst._flatten_sentinel import FlattenSentinel
from libcst._maybe_sentinel import MaybeSentinel
from libcst._removal_sentinel import RemovalSentinel
from libcst._typed_visitor_base import mark_no_op
from libcst._nodes.whitespace import SimpleWhitespace

# Importing the function to be tested
from _typed_visitor import leave_BinaryOperation_right

class Test_CstTypedBaseFunctionsLeaveBinaryOperationRight:

    # Test Scenario 1
    def test_leave_BinaryOperation_right_termination(self):
        node = BinaryOperation(left=Name("x"), operator=Add(), right=Integer("1"))
        try:
            leave_BinaryOperation_right(node)
        except Exception as e:
            pytest.fail(f"Unexpected error: {e}")

    # Test Scenario 2
    def test_leave_BinaryOperation_left_invariance(self):
        node = BinaryOperation(left=Name("x"), operator=Add(), right=Integer("1"))
        snapshot = node.deep_clone()
        leave_BinaryOperation_right(node)
        assert node == snapshot # Asserts that the node's properties have not been mutated

    # Test Scenario 3
    def test_leave_BinaryOperation_right_binary_operation_types(self):
        operator_types = [Add(), Subtract(), Multiply()]
        for operator in operator_types:
            node = BinaryOperation(left=Name("x"), operator=operator, right=Integer("1"))
            try:
                leave_BinaryOperation_right(node)
            except Exception as e:
                pytest.fail(f"Failed for operator {operator}: {e.message}")
