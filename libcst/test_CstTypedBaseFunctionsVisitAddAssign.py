import pytest
from typing import Optional
from _typed_visitor import visit_AddAssign
from libcst._nodes.op import AddAssign

class Test_CstTypedBaseFunctionsVisitAddAssign:
    @pytest.mark.valid
    def test_valid_node_passed(self):
        valid_Node = AddAssign()
        result = visit_AddAssign(valid_Node)
        assert result is not None, "Function should return non-None value"

    @pytest.mark.invalid
    def test_non_AddAssign_node_passed(self):
        non_AddAssign_node = 'Test Node'
        with pytest.raises(TypeError):
            visit_AddAssign(non_AddAssign_node)

    @pytest.mark.negative
    def test_null_Node_passed(self):
        null_Node = None
        with pytest.raises(TypeError):
            visit_AddAssign(null_Node)

    @pytest.mark.negative
    def test_no_node_passed(self):
        with pytest.raises(TypeError):
            visit_AddAssign()
