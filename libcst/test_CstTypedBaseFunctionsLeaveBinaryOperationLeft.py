import pytest
from libcst._nodes.expression import BinaryOperation
import copy
from _typed_visitor import leave_BinaryOperation_left

class Test_CstTypedBaseFunctionsLeaveBinaryOperationLeft:

    @pytest.mark.parametrize(
        "test_input,expected",
        [(BinaryOperation('*'),None), (BinaryOperation(10), None), (BinaryOperation('test'), None)]
    )
    def test_return_of_BinaryOperation_left(self, test_input, expected):
        """
        Test to ensure that the leave_BinaryOperation_left function returns None
        """
        assert leave_BinaryOperation_left(test_input) == expected

    def test_different_nodes_for_BinaryOperation_left(self):
        """
        Test to ensure that the leave_BinaryOperation_left function can handle various BinaryOperation nodes
        """
        binary_operation_nodes = [BinaryOperation('*'), BinaryOperation(10), BinaryOperation('test')]
        
        for node in binary_operation_nodes:
            try:
                assert leave_BinaryOperation_left(node) is None
            except Exception as e:
                pytest.fail(f"leave_BinaryOperation_left function failed with {node}, error: {str(e)}")

    def test_immutable_BinaryOperation_left(self):
        """
        Test to ensure that the leave_BinaryOperation_left function does not modify the BinaryOperation node
        """
        binary_operation_node = BinaryOperation('*')
        deepcopied_node = copy.deepcopy(binary_operation_node)
        leave_BinaryOperation_left(binary_operation_node)
        assert binary_operation_node == deepcopied_node
