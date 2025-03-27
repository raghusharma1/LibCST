import pytest
from _typed_visitor import visit_Attribute_attr
from libcst._nodes.expression import Attribute


class Test_CstTypedBaseFunctionsVisitAttributeAttr:

    @pytest.mark.regression
    def test_visitAttributeAttr_withAttribute(self):
        try:
            node = Attribute("value")
            visit_Attribute_attr(node)
        except Exception as e:
            pytest.fail(f"Test failed with exception {e}")

    @pytest.mark.regression
    def test_visitAttributeAttr_withNull(self):
        try:
            node = None
            visit_Attribute_attr(node)
        except Exception as e:
            pytest.fail(f"Test failed with exception {e}")

    @pytest.mark.regression
    def test_visitAttributeAttr_withNonAttribute(self):
        try:
            node = "NonAttributeNode"
            visit_Attribute_attr(node)
        except Exception as e:
            pytest.fail(f"Test failed with exception {e}")

    @pytest.mark.regression
    def test_visitAttributeAttr_withAttributeWithContent(self):
        try:
            attr_value = "TestContentInAttribute"
            node = Attribute(attr_value)
            visit_Attribute_attr(node)
        except Exception as e:
            pytest.fail(f"Test failed with exception {e}")
