import pytest
from _typed_visitor import leave_Arg_equal
from libcst._nodes.expression import Arg, Name

class Test_CstTypedBaseFunctionsLeaveArgEqual:
    # Test Scenario 1
    def test_leave_Arg_equal_with_valid_node(self):
        # Arrange
        argument_node = Arg(Name("test_arg"))
        
        # Act
        try:
            leave_Arg_equal(argument_node)
            # Assert
            assert True
        except:
            assert False

    # Test Scenario 2
    def test_leave_Arg_equal_with_invalid_node(self):
        # Arrange
        name_node = Name("test_arg")

        # Act
        try:
            leave_Arg_equal(name_node)
            assert False # should not reach this statement, as an error is expected
        except:
            # Assert
            assert True

    # Test Scenario 3
    def test_leave_Arg_equal_with_None(self):
        # Act
        try:
            leave_Arg_equal(None)
            assert False # should not reach this statement, as an error is expected
        except:
            # Assert
            assert True

