import pytest
from libcst._nodes.expression import BinaryOperation
from _typed_visitor import visit_BinaryOperation_lpar

class Test_CstTypedBaseFunctionsVisitBinaryOperationLpar:
  
    @pytest.mark.smoke
    def test_visit_BinaryOperation_lpar_success(self):
        # Arrange
        node_obj = BinaryOperation()
        # Act and Assert
        assert visit_BinaryOperation_lpar(node_obj) == None

    @pytest.mark.regression
    def test_visit_BinaryOperation_lpar_state_persistence(self):
        # Arrange
        node_obj1 = BinaryOperation()
        node_obj2 = BinaryOperation()
        # Act 
        visit_BinaryOperation_lpar(node_obj1)
        state_after_first_call = node_obj1.__dict__
        visit_BinaryOperation_lpar(node_obj2)
        state_after_second_call = node_obj2.__dict__
        # Assert
        assert state_after_first_call == state_after_second_call

    @pytest.mark.negative
    def test_visit_BinaryOperation_lpar_none_handling(self):
        # Act and Assert
        assert visit_BinaryOperation_lpar(None) == None

    @pytest.mark.positive
    def test_visit_BinaryOperation_lpar_idempotency(self):
        # Arrange
        node_obj = BinaryOperation()
        # Act
        first_call_result = visit_BinaryOperation_lpar(node_obj)
        second_call_result = visit_BinaryOperation_lpar(node_obj)
        # Assert
        assert first_call_result == second_call_result
