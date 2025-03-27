import pytest
from libcst import Arg
from _typed_visitor import visit_Arg_value

class Test_CstTypedBaseFunctionsVisitArgValue:
    @pytest.mark.valid
    def test_arg_value_node_type(self):
        arg_node = Arg(value="test")
        try:
            visit_Arg_value(arg_node)
        except Exception as ex:
            pytest.fail(f"Test failed due to unexpected error: {ex}")

    @pytest.mark.valid
    def test_arg_value_no_side_affects(self):
        arg_node = Arg(value="test")
        arg_node_copy = arg_node.deep_clone()

        visit_Arg_value(arg_node)

        assert arg_node.deep_equals(arg_node_copy), "Test failed since the Arg node was modified"

    @pytest.mark.valid
    def test_arg_value_return_none(self):
        arg_node = Arg(value="test")
        result = visit_Arg_value(arg_node)
        assert result is None, "Test failed since the function did not return None"
