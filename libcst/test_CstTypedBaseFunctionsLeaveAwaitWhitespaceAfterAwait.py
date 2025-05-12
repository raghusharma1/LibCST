import pytest
from _typed_visitor import leave_Await_whitespace_after_await
from libcst._nodes.expression import Await, Name
from libcst._nodes.whitespace import SimpleWhitespace

class Test_CstTypedBaseFunctionsLeaveAwaitWhitespaceAfterAwait:

    @pytest.mark.parametrize("node, expected", [
        (Await(whitespace_after_await=SimpleWhitespace(value=' ')), None),
        (Name(value='testNode'), None)
    ])
    def test_leave_Await_whitespace_after_await_With_Await_Node(self, node, expected):
        result = leave_Await_whitespace_after_await(node)
        assert result == expected, "leave_Await_whitespace_after_await should just pass"

    @pytest.mark.parametrize("node, expected", [
        (Await(whitespace_after_await=SimpleWhitespace(value=' ')), None),
        (Name(value='testNode'), None)
    ])
    def test_leave_Await_whitespace_after_await_With_Non_Await_Node(self, node, expected):
        result = leave_Await_whitespace_after_await(node)
        assert result == expected, "leave_Await_whitespace_after_await should handle all node types"
