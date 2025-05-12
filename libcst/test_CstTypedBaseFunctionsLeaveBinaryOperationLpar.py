import pytest
from libcst._nodes.expression import BinaryOperation
from libcst._typed_visitor import CSTTypedBaseFunctions

class Test_CstTypedBaseFunctionsLeaveBinaryOperationLpar:
    
    @pytest.mark.regression
    def test_leave_BinaryOperation_lpar_with_param(self):

        # Arrange
        binary_operation_node = BinaryOperation()

        # Act
        try:
            CSTTypedBaseFunctions().leave_BinaryOperation_lpar(binary_operation_node)
            exception_raised = False
        except Exception:
            exception_raised = True
        
        # Assert
        assert not exception_raised

    @pytest.mark.negative
    def test_leave_BinaryOperation_lpar_without_param(self):

        # Act and Assert
        with pytest.raises(TypeError):
            CSTTypedBaseFunctions().leave_BinaryOperation_lpar()

    @pytest.mark.regression
    def test_leave_BinaryOperation_lpar_with_non_binary_operation_param(self):

        # Arrange
        non_binary_operation_node = object()

        # Act
        try:
            CSTTypedBaseFunctions().leave_BinaryOperation_lpar(non_binary_operation_node)
            exception_raised = False
        except Exception:
            exception_raised = True

        # Assert
        assert not exception_raised
