import pytest
from libcst._nodes.expression import Arg
from libcst._typed_visitor import CSTTypedBaseFunctions


class Test_CstTypedBaseFunctionsLeaveArgWhitespaceAfterStar:
    """Tests for the CSTTypedBaseFunctions class, specifically testing the leave_Arg_whitespace_after_star function."""

    @pytest.mark.parametrize("arg_node", [
        Arg(),
        Arg(
            value=Name('foo'),
            star='*',
            whitespace_after_star=SimpleWhitespace(' ')
        ),
        Arg(
            value=Name('bar'),
            star='*',
            whitespace_after_star=SimpleWhitespace('  ')
        ),
    ])
    def test_leave_arg_whitespace_after_star_with_valid_arg_node(self, arg_node):
        """Tests leave_Arg_whitespace_after_star with a valid Arg node."""
        cst = CSTTypedBaseFunctions()
        result = cst.leave_Arg_whitespace_after_star(arg_node)
        assert result is None

    def test_leave_arg_whitespace_after_star_with_arg_node_having_trailing_whitespaces(self):
        """Tests leave_Arg_whitespace_after_star with an Arg node containing trailing whitespaces after the star."""
        cst = CSTTypedBaseFunctions()
        
        arg_node = Arg(
            value=Name('foo'),
            star='*',
            whitespace_after_star=SimpleWhitespace(' ')
        )

        result = cst.leave_Arg_whitespace_after_star(arg_node)
        assert arg_node.whitespace_after_star is SimpleWhitespace(' ')
        assert result is None

    def test_leave_arg_whitespace_after_star_with_multiple_arg_nodes(self):
        """Tests leave_Arg_whitespace_after_star with various Arg nodes."""
        cst = CSTTypedBaseFunctions()
        
        arg_nodes = [
            Arg(
                value=Name('foo'),
                star='*',
                whitespace_after_star=SimpleWhitespace(' ')
            ),
            Arg(
                value=Name('bar'),
                star='*',
                whitespace_after_star=SimpleWhitespace('  ')
            ),
            Arg(
                value=Name('baz'),
                star='*',
                whitespace_after_star=SimpleWhitespace('')
            ),
        ]

        for arg in arg_nodes:
            result = cst.leave_Arg_whitespace_after_star(arg)
            assert result is None
