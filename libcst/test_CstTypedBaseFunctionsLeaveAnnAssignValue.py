from _typed_visitor import leave_AnnAssign_value
from libcst._nodes.statement import AnnAssign
import pytest
from typing import Callable

class Test_CstTypedBaseFunctionsLeaveAnnAssignValue:
	
    @pytest.mark.parametrize("method", [leave_AnnAssign_value])
    def test_leave_AnnAssign_value_with_node_input(self, method: Callable):
        """ Test scenario where 'leave_AnnAssign_value' function is called with a valid node instance"""
        # Arrange
        node = AnnAssign()
        # Act
        try:
            method(node)
        # Assert
        except Exception as e:
            pytest.fail(f"TestMethod {method.__name__} failed with error {e}")

    @pytest.mark.parametrize("method", [leave_AnnAssign_value])
    @pytest.mark.parametrize("invalid_input", ['', [], {}, 123])
    def test_leave_AnnAssign_value_with_non_node_input(self, method: Callable, invalid_input):
        """ Test scenario where 'leave_AnnAssign_value' function is called with a non node instance"""
        # Arrange
        # Act
        # Assert
        with pytest.raises(TypeError):
            method(invalid_input)

            

    @pytest.mark.parametrize("method", [leave_AnnAssign_value])
    def test_leave_AnnAssign_value_with_no_input(self, method: Callable):
        """ Test scenario where 'leave_AnnAssign_value' function is called with no argument"""
        # Arrange
        # Act
        # Assert
        with pytest.raises(TypeError):
            method()


