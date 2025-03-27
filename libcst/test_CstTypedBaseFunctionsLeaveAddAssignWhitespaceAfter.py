import pytest
from _typed_visitor import CSTTypedBaseFunctions
from libcst._nodes.op import AddAssign
from libcst._nodes.expression import Integer
from unittest.mock import MagicMock

class Test_CstTypedBaseFunctionsLeaveAddAssignWhitespaceAfter:

    @pytest.mark.positive
    def test_on_AddAssign_node_exists(self):
        # Arrange
        mock_obj = CSTTypedBaseFunctions()
        add_assign_node_mock = MagicMock(spec=AddAssign)

        # Act
        try:
            mock_obj.leave_AddAssign_whitespace_after(add_assign_node_mock)
            has_error = False
        except:
            has_error = True

        # Assert
        assert not has_error, "Error occurred while processing AddAssign node"

    @pytest.mark.negative
    def test_on_incorrect_node_type(self):
        # Arrange
        mock_obj = CSTTypedBaseFunctions()
        integer_node_mock = MagicMock(spec=Integer)

        # Act
        try:
            mock_obj.leave_AddAssign_whitespace_after(integer_node_mock)
            has_error = False
        except:
            has_error = True

        # Assert
        assert has_error, "Function didn't produce an error with incorrect node type"

    @pytest.mark.negative
    def test_on_Null_node(self):
        # Arrange
        mock_obj = CSTTypedBaseFunctions()
        null_node = None

        # Act
        try:
            mock_obj.leave_AddAssign_whitespace_after(null_node)
            has_error = False
        except:
            has_error = True

        # Assert
        assert has_error, "Function didn't produce an error with Null node"
