import pytest
from libcst._nodes.statement import AugAssign
from libcst._nodes.expression import Name, SimpleString
from libcst._nodes.op import AddAssign
from _typed_visitor import visit_AugAssign_value

class Test_CstTypedBaseFunctionsVisitAugAssignValue:

    @pytest.mark.smoke
    @pytest.mark.positive
    def test_handles_node_correctly(self):
        """Test if visit_AugAssign_value handles the node correctly"""
        node = AugAssign(Name("x"), AddAssign(), SimpleString("5"))
        assert visit_AugAssign_value(node) is None

    @pytest.mark.smoke
    @pytest.mark.negative
    def test_handles_none_argument(self):
        """Test if visit_AugAssign_value functions with a None argument"""
        with pytest.raises(TypeError):
            visit_AugAssign_value(None)

    @pytest.mark.regression
    @pytest.mark.valid
    @pytest.mark.invalid
    @pytest.mark.parametrize("node", [Name("x"), SimpleString("5")])
    def test_with_different_node_types(self, node):
        """Test visit_AugAssign_value with different types from libcst._nodes module"""
        assert visit_AugAssign_value(node) is None
