import pytest
from libcst._nodes.expression import Attribute, Integer, Call
from _typed_visitor import visit_Attribute_rpar

class Test_CstTypedBaseFunctionsVisitAttributeRpar:

    @pytest.mark.parametrize("node", [Attribute(Name('x'), Name('y'))])
    def test_visit_Attribute_rpar_with_attribute_node(self, node):
        original_node = node.deep_clone()
        visit_Attribute_rpar(node)
        assert node == original_node, "The node should not be modified"

    @pytest.mark.parametrize("node", [Integer('5'), Call(Name('x'), [])])
    def test_visit_Attribute_rpar_with_non_attribute_node(self, node):
        original_node = node.deep_clone()
        visit_Attribute_rpar(node)
        assert node == original_node, "The node should not be modified"

    def test_visit_Attribute_rpar_with_null_node(self):
        node = None
        try:
            visit_Attribute_rpar(node)
        except Exception as e:
            pytest.fail(f"Test failed: {e}")
