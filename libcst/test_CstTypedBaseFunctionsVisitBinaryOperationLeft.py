# Importing necessary modules
import pytest
from libcst._nodes.expression import BinaryOperation, Call
from _typed_visitor import visit_BinaryOperation_left


class Test_CstTypedBaseFunctionsVisitBinaryOperationLeft:
    @pytest.mark.positive
    def test_visit_BinaryOperation_left_with_binaryoperation_node(self):
        # Arrange
        binary_node = BinaryOperation()
        # Act
        try:
            visit_BinaryOperation_left(binary_node)
        # Assert
        except Exception as e:
            pytest.fail(f"Test failed with error {str(e)}")

    @pytest.mark.negative
    def test_visit_BinaryOperation_left_with_non_binaryoperation_node(self):
        # Arrange
        call_node = Call()
        # Act
        try:
            visit_BinaryOperation_left(call_node)
        # Assert
        except Exception as e:
            pytest.fail(f"Test failed with error {str(e)}")

    @pytest.mark.edge
    def test_visit_BinaryOperation_left_with_None_node(self):
        # Arrange
        none_node = None
        # Act
        try:
            visit_BinaryOperation_left(none_node)
        # Assert
        except Exception as e:
            pytest.fail(f"Test failed with error {str(e)}")
