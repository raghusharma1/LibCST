import pytest
from libcst._nodes.statement import Assert
from _typed_visitor import leave_Assert_comma

class Test_CstTypedBaseFunctionsLeaveAssertComma:

    @pytest.mark.valid
    def test_leave_assert_comma_no_exception(self):
        test_assert_obj = Assert()  # Initialising the Assert object.
        try:
            leave_Assert_comma(test_assert_obj)
        except Exception:
            pytest.fail("Test failed: leave_Assert_comma function raises an exception")

    @pytest.mark.valid
    def test_leave_assert_comma_no_change(self):
        test_assert_obj = Assert()  # Initialising the Assert object.
        assert_obj_prop_before = vars(test_assert_obj)  # Getting its initial properties
        leave_Assert_comma(test_assert_obj)
        assert_obj_prop_after = vars(test_assert_obj)  # Getting its properties after calling the function
        assert assert_obj_prop_before == assert_obj_prop_after, "Test failed: Properties of Assert object have changed after calling leave_Assert_comma function"

    @pytest.mark.invalid
    def test_leave_assert_comma_handles_none(self):
        try:
            leave_Assert_comma(None)
        except Exception:
            pytest.fail("Test failed: leave_Assert_comma function raises an exception when None is passed as an argument")
