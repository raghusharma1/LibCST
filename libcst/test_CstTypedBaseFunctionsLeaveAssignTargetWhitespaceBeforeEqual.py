import pytest
from _typed_visitor import leave_AssignTarget_whitespace_before_equal
from libcst import AssignTarget
from copy import deepcopy

class Test_CstTypedBaseFunctionsLeaveAssignTargetWhitespaceBeforeEqual:
  
    @pytest.mark.smoke
    def test_handle_assignTarget_object(self):
        at = AssignTarget()
        try:
            leave_AssignTarget_whitespace_before_equal(at)
        except:
            pytest.fail("Test failed: function was unable to handle AssignTarget object")

    @pytest.mark.valid
    def test_operation_performed_by_function(self):
        at = AssignTarget()
        at_copy = deepcopy(at)
        leave_AssignTarget_whitespace_before_equal(at)
        assert at == at_copy, "Test failed: function has altered the AssignTarget object"
  
    @pytest.mark.regression
    @pytest.mark.parametrize("content", [Name('random'), SimpleString("random"), Integer("1")])
    def test_function_behavior_with_different_kinds_of_AssignTarget_objects(self, content):
        at = AssignTarget(content)
        try:
            leave_AssignTarget_whitespace_before_equal(at)
        except Exception as e:
            pytest.fail(f"Test failed for input {type(content).__name__}:{str(content)}. Exception: {str(e)}")
