import pytest
from libcst._nodes.statement import AssignTarget
from _typed_visitor import leave_AssignTarget_whitespace_after_equal

class Test_CstTypedBaseFunctionsLeaveAssignTargetWhitespaceAfterEqual:

    def test_should_executewith_AssingTargetNode(self):
        # Arrange
        valid_assign_target = AssignTarget(value="Test")
        
        # Act & Assert
        # if execution reaches this point without exception, the test will pass
        try:
            leave_AssignTarget_whitespace_after_equal(valid_assign_target)
        except:
            pytest.fail("Test failed, leave_AssignTarget_whitespace_after_equal throws an exception with a valid input")

    def test_NoneInput(self):
        # Act & Assert
        with pytest.raises(TypeError):
            leave_AssignTarget_whitespace_after_equal(None)

    def test_UnrelatedTypeInput(self):
        # Arrange
        unrelated_type_input = "This is an unrelated input"
        
        # Act & Assert
        with pytest.raises(TypeError) as err:
            leave_AssignTarget_whitespace_after_equal(unrelated_type_input)
        assert str(err.value) == "Incorrect type passed"
