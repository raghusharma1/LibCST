# Importing necessary modules and functions
import pytest
from _typed_visitor import visit_Arg_whitespace_after_arg
from libcst._nodes.expression import Arg

class Test_CstTypedBaseFunctionsVisitArgWhitespaceAfterArg:

    @pytest.mark.parametrize("default_arg", [Arg()])
    def test_visit_arg_whitespace_after_arg_with_default(self, default_arg):
        """
        Test scenario to verify visit_Arg_whitespace_after_arg function's ability to run with the default arg node
        """
        try:
            # The function call
            visit_Arg_whitespace_after_arg(default_arg)

        except Exception as e:
            pytest.fail(f"Test failed due to: {str(e)}")

    @pytest.mark.parametrize("custom_arg", [Arg(value="Hello", whitespace_before_equal=None, equal=None, whitespace_after_equal=None)])
    def test_visit_arg_whitespace_after_arg_with_custom_node(self, custom_arg):
        """
        Test scenario to verify visit_Arg_whitespace_after_arg function's ability to run with a custom arg node
        """
        try:
            # passing custom arg to the function
            visit_Arg_whitespace_after_arg(custom_arg)

        except Exception as e:
            pytest.fail(f"Test failed due to: {str(e)}")


    def test_visit_arg_whitespace_after_arg_with_none(self):
        """
        Test scenario to verify visit_Arg_whitespace_after_arg function's ability to handle None
        """
        try:
            visit_Arg_whitespace_after_arg(None)

        except Exception as e:
            pytest.fail(f"Test failed due to: {str(e)}")
