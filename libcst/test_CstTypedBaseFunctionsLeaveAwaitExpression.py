import pytest
from unittest.mock import Mock
from _typed_visitor import leave_Await_expression
from libcst._nodes.expression import Await

class Test_CstTypedBaseFunctionsLeaveAwaitExpression:
    @pytest.mark.noop
    def test_leave_Await_expression_noop(self):
        mock_node = Mock(spec=Await)
        try:
            result = leave_Await_expression(mock_node)
            assert result is None
        except Exception as e:
            pytest.fail(f"Test failed due to {e}")

    def test_leave_Await_expression_with_type_Await(self):
        mock_node = Mock(spec=Await)
        try:
            result = leave_Await_expression(mock_node)
            assert result is None
        except Exception as e:
            pytest.fail(f"Test failed due to {e}")

    def test_leave_Await_expression_with_non_Await_type(self):
        mock_node = Mock()
        with pytest.raises(TypeError):
            result = leave_Await_expression(mock_node)
