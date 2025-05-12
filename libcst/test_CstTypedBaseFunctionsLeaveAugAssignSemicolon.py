# Importing all necessary libraries for test execution
import pytest
from _typed_visitor import leave_AugAssign_semicolon
from libcst._nodes.expression import Name, Integer
from libcst._nodes.op import AddAssign
from libcst._nodes.statement import AugAssign

# Test_class to group all the test_cases
class Test_CstTypedBaseFunctionsLeaveAugAssignSemicolon:

    # Assert on successful execution as no return value or side effects are expected
    @pytest.mark.smoke
    def test_leave_aaugassign_semicolon_with_augassign_node(self):
        # Arrange: Instantiate a AugAssign node and instance of class containing function
        node = AugAssign(target=Name("foo"), operator=AddAssign(), value=Integer("5"))
        obj = leave_AugAssign_semicolon()
        
        # Act: Invoke the function by passing the node as parameter
        try:
            obj.leave_AugAssign_semicolon(node)

        # Assert: If no exception is raised then consider it as pass
        except Exception as e:
            pytest.fail(f"Test failed due to:{str(e)}")

    # Assert on successful execution as no return value or side effects are expected
    @pytest.mark.negative
    def test_leave_aaugassign_semicolon_with_non_augassign_node(self):
        # Arrange: Instantiate a non AugAssign node and instance of class containing function
        node = Name("foo")
        obj = leave_AugAssign_semicolon()

        # Act: Invoke the function by passing the node as parameter
        try:
            obj.leave_AugAssign_semicolon(node)

        # Assert: If no exception is raised then consider it as pass
        except Exception as e:
            pytest.fail(f"Test failed due to:{str(e)}")

    # Assert on successful execution as no return value or side effects are expected
    @pytest.mark.negative
    def test_leave_aaugassign_semicolon_with_empty_node(self):
        # Arrange: Instantiate an empty node and instance of class containing function
        node = AugAssign(target=None, operator=None, value=None)
        obj = leave_AugAssign_semicolon()

        # Act: Invoke the function by passing the empty node as parameter
        try:
            obj.leave_AugAssign_semicolon(node)

        # Assert: If no exception is raised then consider it as pass
        except Exception as e:
            pytest.fail(f"Test failed due to:{str(e)}")
