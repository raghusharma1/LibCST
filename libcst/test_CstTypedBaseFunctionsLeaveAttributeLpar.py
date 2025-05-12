import pytest
from _typed_visitor import leave_Attribute_lpar
from libcst._nodes.expression import Attribute, Call


class Test_CstTypedBaseFunctionsLeaveAttributeLpar:
    @pytest.mark.parametrize("node", [None])
    def test_leave_Attribute_lpar_no_node(self, node):
        with pytest.raises(TypeError):
            leave_Attribute_lpar(node)

    @pytest.mark.parametrize("node", [Call()])
    def test_leave_Attribute_lpar_with_non_attribute_node(self, node):
        try:
            leave_Attribute_lpar(node)
        except Exception as exp:
            pytest.fail(f"Test failed due to unexpected error: {exp}")

    @pytest.mark.parametrize("node", [Attribute()])
    def test_leave_Attribute_lpar_with_attribute_node(self, node):
        try:
            leave_Attribute_lpar(node)
        except Exception as exp:
            pytest.fail(f"Test failed due to unexpected error: {exp}")
