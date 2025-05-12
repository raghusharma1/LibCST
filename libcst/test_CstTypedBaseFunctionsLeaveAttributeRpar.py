import pytest
from libcst._nodes.expression import Attribute, BaseExpression, Name
from _typed_visitor import leave_Attribute_rpar

class Test_CstTypedBaseFunctionsLeaveAttributeRpar:
    
    @pytest.mark.positive
    def test_leave_Attribute_rpar_empty(self):
        empty_attr = Attribute()
        exception = False
        try:
            leave_Attribute_rpar(empty_attr)
        except:
            exception = True
        assert not exception

    @pytest.mark.regression
    def test_leave_Attribute_rpar_standard(self):
        standard_attr = Attribute(
            value=Name("value"),
            attr=Name("attr")
        )
        exception = False
        try:
            leave_Attribute_rpar(standard_attr)
        except:
            exception = True
        assert not exception

    @pytest.mark.performance
    def test_leave_Attribute_rpar_complex(self):
        complex_attr = Attribute(
            value=Attribute(
                value=Name("value_inner"),
                attr=Name("attr_inner")
            ),
            attr=Name("attr_outer")
        )
        exception = False
        try:
            leave_Attribute_rpar(complex_attr)
        except:
            exception = True
        assert not exception
