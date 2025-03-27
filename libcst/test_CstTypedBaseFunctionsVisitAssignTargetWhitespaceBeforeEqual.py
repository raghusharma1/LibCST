import pytest
from _typed_visitor import visit_AssignTarget_whitespace_before_equal
from libcst._nodes.statement import AssignTarget


class Test_CstTypedBaseFunctionsVisitAssignTargetWhitespaceBeforeEqual:

    def test_visit_AssignTarget_whitespace_before_equal_does_nothing(self):
        # Arrange
        assign_target_instance = AssignTarget()
        initial_state = str(assign_target_instance)

        # Act
        visit_AssignTarget_whitespace_before_equal(assign_target_instance)

        # Assert
        assert str(assign_target_instance) == initial_state

    def test_visit_AssignTarget_whitespace_before_equal_accepts_assign_target(self):
        # Arrange
        assign_target_instance = AssignTarget()
        string_instance = "test"
        integer_instance = 10

        # Act and Assert
        visit_AssignTarget_whitespace_before_equal(assign_target_instance) # should not raise
        with pytest.raises(TypeError):
            visit_AssignTarget_whitespace_before_equal(string_instance)
        with pytest.raises(TypeError):
            visit_AssignTarget_whitespace_before_equal(integer_instance)

    def test_visit_AssignTarget_whitespace_before_equal_handles_null_inputs(self):
        # Arrange, Act and Assert
        # Should not raise an error
        visit_AssignTarget_whitespace_before_equal(None)
