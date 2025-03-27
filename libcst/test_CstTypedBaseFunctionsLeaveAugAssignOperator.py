import pytest
from libcst._nodes.op import AddAssign
from libcst._nodes.statement import AugAssign
from libcst._nodes.expression import Name
from _typed_visitor import leave_AugAssign_operator

# Define the test class
class Test_CstTypedBaseFunctionsLeaveAugAssignOperator:
    
    # Scenario 1: Testing function invocation with an instance of AugAssign node
    @pytest.mark.regression
    def test_leave_AugAssign_operator_with_AugAssign_instance(self):
        # Arrangement
        aug_assign_instance = AugAssign(target=Name("a"), operator=AddAssign(), value=Name("b"))
        
        # Act and Assert
        try:
            leave_AugAssign_operator(aug_assign_instance)
        except Exception as e:
            pytest.fail(f"Test failed due to unexpected error: {str(e)}")
    
    # Scenario 2: Testing function invocation with null node
    @pytest.mark.invalid
    def test_leave_AugAssign_operator_with_null(self):
        # Act and Assert
        with pytest.raises(TypeError):
            leave_AugAssign_operator(None)

    # Scenario 3: Testing function invocation with non-AugAssign instances
    @pytest.mark.regression
    def test_leave_AugAssign_operator_with_non_AugAssign_instance(self):
        # Arrangement
        non_aug_assign_node = Name("z")
        # Act and Assert
        with pytest.raises(TypeError):
            leave_AugAssign_operator(non_aug_assign_node)
