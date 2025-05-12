import pytest
from libcst._nodes.op import BitAnd
from libcst._typed_visitor_base import CSTTypedBaseFunctions
from _typed_visitor import leave_BitAnd_whitespace_before

class Test_CstTypedBaseFunctionsLeaveBitAndWhitespaceBefore:

    @pytest.mark.parametrize("node", [BitAnd()])
    def test_leave_BitAnd_whitespace_before_with_BitAnd_node(self, node):
        cst = CSTTypedBaseFunctions()
        assert cst.leave_BitAnd_whitespace_before(node) is None

    @pytest.mark.parametrize("node", [1, "string", 1.0])
    def test_leave_BitAnd_whitespace_before_with_non_BitAnd_node(self, node):
        cst = CSTTypedBaseFunctions()
        with pytest.raises(Exception):
            cst.leave_BitAnd_whitespace_before(node)

    @pytest.mark.parametrize("node", [None])
    def test_leave_BitAnd_whitespace_before_with_None(self, node):
        cst = CSTTypedBaseFunctions()
        with pytest.raises(Exception):
            cst.leave_BitAnd_whitespace_before(node)
