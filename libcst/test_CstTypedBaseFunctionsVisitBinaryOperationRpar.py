import pytest
from libcst import BinaryOperation, Name, Integer, Add
from _typed_visitor import visit_BinaryOperation_rpar 

class Test_CstTypedBaseFunctionsVisitBinaryOperationRpar:

    @pytest.mark.positive
    def test_visit_BinaryOperation_rpar_valid(self):
        # Arrange
        node = BinaryOperation(left=Name("x"), operator=Add(), right=Integer("1"))

        # Act & Assert
        try:
            visit_BinaryOperation_rpar(node)
        except Exception as e:
            pytest.fail(f"Unexpected error occurred: {e}")

    @pytest.mark.negative
    def test_visit_BinaryOperation_rpar_invalid(self):
        # Invalid data types used (String instead of Name() etc.)
        # Arrange
        node = BinaryOperation(left="x", operator=5, right="abc")

        # Act & Assert
        with pytest.raises(Exception):
            visit_BinaryOperation_rpar(node)

    @pytest.mark.regression
    def test_visit_BinaryOperation_rpar_varied_binary_operations(self):
        valid_operations = [
            BinaryOperation(left=Name("abc"), operator=Add(), right=Integer("9")),
            BinaryOperation(left=Name("x"), operator=Add(), right=Integer("1")),
            BinaryOperation(left=Name("y"), operator=Add(), right=Integer("2")),
        ]

        for each_op in valid_operations:
            try:
                visit_BinaryOperation_rpar(each_op)
            except Exception as e:
                pytest.fail(f"Unexpected error occurred for operation {each_op}: {e}")
