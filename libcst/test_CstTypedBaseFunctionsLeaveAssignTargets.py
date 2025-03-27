import pytest
from _typed_visitor import leave_Assign_targets
from libcst._nodes.statement import Assign
from libcst._nodes.expression import Dict

class Test_CstTypedBaseFunctionsLeaveAssignTargets:

    @pytest.mark.smoke
    def test_leave_assign_targets_with_assign_node(self):
        # Arrange
        node = Assign()

        # Act and Assert
        try:
            leave_Assign_targets(self, node)
        except Exception as e:
            pytest.fail(f"leave_Assign_targets failed with exception {e}")

    @pytest.mark.regression
    def test_leave_assign_targets_with_nonassign_node(self): 
        # Arrange
        dict_node = Dict()

        # Act
        result = leave_Assign_targets(self, dict_node)

        # Assert
        assert result is None, "Expecting leave_Assign_targets to return None for non-Assign nodes"

    @pytest.mark.smoke
    def test_leave_assign_targets_with_none(self): 
        # Arrange there is nothing to initialize in this case.

        # Act
        result = leave_Assign_targets(self, None)

        # Assert
        assert result is None, "Expecting None when passing None to leave_Assign_targets"
