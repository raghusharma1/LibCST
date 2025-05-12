import pytest
from _typed_visitor import leave_AddAssign_whitespace_before
from libcst._nodes.op import AddAssign
from libcst._nodes.expression import Integer

class Test_CstTypedBaseFunctionsLeaveAddAssignWhitespaceBefore:

    @pytest.mark.regression
    def test_leave_AddAssign_whitespace_before_AddAssign_node(self):
        # Arrange
        node = AddAssign()

        # Act & Assert
        try:
            leave_AddAssign_whitespace_before(node)
        except:
            pytest.fail("leave_AddAssign_whitespace_before function failed with AddAssign node")

    @pytest.mark.regression
    def test_leave_AddAssign_whitespace_before_non_AddAssign_node(self):
        # Arrange
        node = Integer(5)

        # Act & Assert
        try:
            leave_AddAssign_whitespace_before(node)
        except:
            pytest.fail("leave_AddAssign_whitespace_before function failed with Non-AddAssign node")
            
    @pytest.mark.regression
    @pytest.mark.parametrize("node", [1, "test", 1.2, True])
    def test_leave_AddAssign_whitespace_before_with_other_types(self, node):
        # Act & Assert
        try:
            leave_AddAssign_whitespace_before(node)
        except:
            pytest.fail(f"leave_AddAssign_whitespace_before function failed with node of type: {type(node)}")

    @pytest.mark.regression
    def test_leave_AddAssign_whitespace_before_with_null(self):
        # Act & Assert
        try:
            leave_AddAssign_whitespace_before(None)
        except:
            pytest.fail("leave_AddAssign_whitespace_before function failed with Null value")
