# Importing Required Libraries
import pytest
from libcst._nodes.expression import BinaryOperation
from _typed_visitor import leave_BinaryOperation_operator


# Define Test Class
class Test_CstTypedBaseFunctionsLeaveBinaryOperationOperator:
    
    # Scenario 1: Test when BinaryOperation instance is passed
    def test_leave_BinaryOperation_operator_with_binary_operation_instance(self):
        # Arrange
        binary_operation = BinaryOperation()

        # Act
        try:
            leave_BinaryOperation_operator(binary_operation)
            exception_raised = False
        except:
            exception_raised = True

        # Assert
        assert exception_raised == False, "The function 'leave_BinaryOperation_operator' should not raise an exception when BinaryOperation instance is passed."

    # Scenario 2: Test with no parameter passed
    def test_leave_BinaryOperation_operator_with_no_parameter(self):
        # Act Assert
        with pytest.raises(TypeError):
            leave_BinaryOperation_operator()

    # Scenario 3: Test when any other type except BinaryOperation is passed
    @pytest.mark.parametrize('non_binary_operation', ['Hello World', 1234, 58.99, [], {}])
    def test_leave_BinaryOperation_operator_with_non_binary_operation(self, non_binary_operation):
        # Act
        try:
            leave_BinaryOperation_operator(non_binary_operation)
            exception_raised = False
        except:
            exception_raised = True

        # Assert
        assert exception_raised == False, f"The function 'leave_BinaryOperation_operator' should not raise an exception when {non_binary_operation} is passed."
