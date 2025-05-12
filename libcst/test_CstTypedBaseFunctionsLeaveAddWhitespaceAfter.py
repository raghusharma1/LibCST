# Test class
import pytest
from _typed_visitor import leave_Add_whitespace_after
from libcst._nodes.op import Add, Multiply, Subtract
from typing import TYPE_CHECKING

class Test_CstTypedBaseFunctionsLeaveAddWhitespaceAfter:

    @pytest.mark.smoke
    def test_leave_add_whitespace_behavior(self):
        # Arrange
        add_node = Add()
        try:
            # Act
            leave_Add_whitespace_after(add_node)
            # Assert
            assert True  # if it reaches here, it means no errors were thrown
        except Exception as e:
            pytest.fail(f"Unexpected error: {str(e)}")

    @pytest.mark.regression
    def test_pass_behavior_leave_add_whitespace(self):
        # Arrange
        add_node_initial_state = Add()
        # Act
        leave_Add_whitespace_after(add_node_initial_state)
        add_node_final_state = Add()
        # Assert
        assert add_node_initial_state == add_node_final_state, "The state of Add node should not be altered"

    @pytest.mark.negative
    def test_handle_different_object_type(self):
        # Arrange
        multiple_node = Multiply()
        try:
            # Act
            leave_Add_whitespace_after(multiple_node)  # not the intended type
            # Assert
            assert True
        except Exception as e:
            pytest.fail(f"Unexpected error: {str(e)}")

    @pytest.mark.negative
    def test_no_parameter_invocation(self):
        # Arrange
        # Act
        try:
            leave_Add_whitespace_after()  # no params
            pytest.fail("The leave_Add_whitespace_after function should throw error when called without parameters")
        # Assert
        except:
            assert True
