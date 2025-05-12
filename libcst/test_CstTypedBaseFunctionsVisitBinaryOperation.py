import pytest
from libcst._nodes.expression import BinaryOperation, BooleanOperation
from _typed_visitor import visit_BinaryOperation

class Test_CstTypedBaseFunctionsVisitBinaryOperation:
    def test_binaryOperation_with_valid_input(self):
        # Arrange
        binary_operation = BinaryOperation()

        try:
            # Act
            visit_BinaryOperation(binary_operation)
        except Exception as e:
            pytest.fail(f"Test failed due to the unexpected Error {e}")

    def test_binaryOperation_with_nested_input(self):
        # Arrange
        nested_binary_operation = BinaryOperation(left=BinaryOperation(), right=BinaryOperation())

        try:
            # Act
            visit_BinaryOperation(nested_binary_operation)
        except Exception as e:
            pytest.fail(f"Test failed due to the unexpected Error {e}")

    def test_binaryOperation_with_booleanOperation_input(self):
        # Arrange
        boolean_operation = BooleanOperation()

        with pytest.raises(TypeError):
            # Act
            visit_BinaryOperation(boolean_operation)

    def test_binaryOperation_with_none_input(self):
        with pytest.raises(TypeError):
            # Act
            visit_BinaryOperation(None)
