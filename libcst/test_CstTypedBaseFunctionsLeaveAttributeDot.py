import pytest
from libcst import Attribute
from libcst._nodes.statement import Name
from _typed_visitor import leave_Attribute_dot

class Test_CstTypedBaseFunctionsLeaveAttributeDot:
    @pytest.mark.valid
    @pytest.mark.smoke
    def test_leave_Attribute_dot_legit_node(self):
        legit_node = Attribute(value=Name('legit_node'), attr=Name('attr'))
        assert leave_Attribute_dot(legit_node) is None

    @pytest.mark.valid
    @pytest.mark.negative
    def test_leave_Attribute_dot_empty_node(self):
        empty_node = Attribute()
        with pytest.raises(TypeError):
            leave_Attribute_dot(empty_node)

    @pytest.mark.invalid
    @pytest.mark.negative
    def test_leave_Attribute_dot_incorrect_node(self):
        incorrect_node = Name('incorrect_node')
        with pytest.raises(TypeError):
            leave_Attribute_dot(incorrect_node)

    @pytest.mark.invalid
    @pytest.mark.negative
    def test_leave_Attribute_dot_null_node(self):
        null_node = None
        with pytest.raises(TypeError):
            leave_Attribute_dot(null_node)
