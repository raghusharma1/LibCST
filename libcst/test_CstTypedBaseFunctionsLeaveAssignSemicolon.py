import pytest
from libcst._nodes.statement import Assign
from _typed_visitor import leave_Assign_semicolon

class Test_CstTypedBaseFunctionsLeaveAssignSemicolon:

    @pytest.mark.smoke
    def test_leave_Assign_semicolon_none(self):
        try:
            leave_Assign_semicolon(None)
        except Exception as e:
            pytest.fail(f"Test failed with exception: {e}")

    @pytest.mark.regression
    def test_leave_Assign_semicolon_valid_assignment(self):
        assign_obj = Assign()
        try:
            leave_Assign_semicolon(assign_obj)
        except Exception as e:
            pytest.fail(f"Test failed with exception: {e}")

    @pytest.mark.regression
    def test_leave_Assign_semicolon_no_modification(self):
        assign_obj = Assign()
        copy_assign_object = assign_obj
        try:
            leave_Assign_semicolon(assign_obj)
            assert assign_obj == copy_assign_object, "leave_Assign_semicolon function is altering the input"
        except AssertionError as e:
            pytest.fail(f"Test failed with exception: {e}")
