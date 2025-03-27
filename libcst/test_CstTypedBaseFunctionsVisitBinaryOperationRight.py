import pytest
from libcst._nodes.expression import BinaryOperation
from libcst._nodes.op import Add
from libcst._nodes.base import CSTNode
from libcst._typed_visitor import visit_BinaryOperation_right

class Test_CstTypedBaseFunctionsVisitBinaryOperationRight:

    @pytest.mark.regression
    def test_no_op_execution_visit_binaryop_right(self):
        # Arrange
        node = BinaryOperation(left="x", operator=Add(), right="y")
        original_node = node.deep_clone()

        # Act
        visit_BinaryOperation_right(node)

        # Assert
        assert node == original_node, "BinaryOperation node should remain unaffected"

    @pytest.mark.regression
    def test_visit_empty_binaryop_right(self):
        # Arrange
        empty_node = BinaryOperation()
        original_empty_node = empty_node.deep_clone()

        # Act
        visit_BinaryOperation_right(empty_node)

        # Assert
        assert empty_node == original_empty_node, "Empty BinaryOperation node should remain unaffected"

    @pytest.mark.regression
    def test_visit_non_binaryop_right(self):
        # Arrange
        non_binaryop_node = CSTNode()
        original_non_binaryop_node = non_binaryop_node.deep_clone()

        # Act
        visit_BinaryOperation_right(non_binaryop_node)

        # Assert
        assert non_binaryop_node == original_non_binaryop_node, "Non-BinaryOperation node should remain unaffected"
