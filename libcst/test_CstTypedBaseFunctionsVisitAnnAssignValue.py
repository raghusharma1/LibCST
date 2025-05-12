import pytest
from libcst._nodes.statement import AnnAssign
from libcst._typed_visitor_base import mark_no_op

# Assuming the function is in a class named CSTTypedBaseFunctions in _typed_visitor module
from _typed_visitor import CSTTypedBaseFunctions  

class Test_CstTypedBaseFunctionsVisitAnnAssignValue:

    @pytest.mark.regression
    def test_visit_AnnAssign_value_no_operation(self):
        cbf = CSTTypedBaseFunctions()
        test_node = AnnAssign()  
        before_test_node_state = test_node.__dict__.copy()  # get state of object before function call
        cbf.visit_AnnAssign_value(test_node)
        assert test_node.__dict__ == before_test_node_state  # ensure state is unchanged

    @pytest.mark.regression
    @pytest.mark.parametrize("input_annassign", [AnnAssign(), AnotherSubclass()])  # Replace AnotherSubclass() with actual subclasses 
    def test_visit_AnnAssign_value_diff_subclasses(self, input_annassign):
        cbf = CSTTypedBaseFunctions()
        try:
            cbf.visit_AnnAssign_value(input_annassign)
        except Exception as e:
            pytest.fail(f"visit_AnnAssign_value raised exception {e} unexpectedly!")

    @pytest.mark.negative
    def test_visit_AnnAssign_value_with_no_param(self):
        cbf = CSTTypedBaseFunctions()
        with pytest.raises(TypeError):
            cbf.visit_AnnAssign_value()
