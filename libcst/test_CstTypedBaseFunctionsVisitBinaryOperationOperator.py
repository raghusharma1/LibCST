import pytest
from libcst._nodes.expression import BinaryOperation, Integer, Float, SimpleString
from libcst._nodes.op import Add

# import the class with the function to test
from _typed_visitor import CSTTypedBaseFunctions

class Test_CstTypedBaseFunctionsVisitBinaryOperationOperator:
    @pytest.mark.valid
    def test_valid_return_visit_binaryoperation(self):
        # Arrange
        node = BinaryOperation(
            left=Integer("3"),
            operator=Add(),
            right=Integer("7"),
        )
        visitor = CSTTypedBaseFunctions()

        # Act
        result = visitor.visit_BinaryOperation_operator(node)

        # Assert
        assert result is None

    @pytest.mark.invalid
    def test_invalid_operator_instance(self):
        # Arrange
        integer_node = Integer("3")
        float_node = Float("3.14")
        string_node = SimpleString("'hello'")
        visitor = CSTTypedBaseFunctions()

        # Act & Assert
        # These calls should not raise any exception
        visitor.visit_BinaryOperation_operator(integer_node)
        visitor.visit_BinaryOperation_operator(float_node)
        visitor.visit_BinaryOperation_operator(string_node)

    @pytest.mark.valid
    def test_altered_operator_property(self):
        # Arrange
        node = BinaryOperation(
            left=Integer("3"),
            operator=Add(),
            right=Integer("7"),
        )
        visitor = CSTTypedBaseFunctions()
        # Modify operator in BinaryOperation
        node.operator = Subtract()

        # Act
        result = visitor.visit_BinaryOperation_operator(node)

        # Assert
        assert result is None
