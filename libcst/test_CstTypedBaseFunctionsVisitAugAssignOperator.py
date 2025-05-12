import pytest
from _typed_visitor import visit_AugAssign_operator
from libcst._nodes.statement import AugAssign
from libcst._nodes.op import AddAssign
from libcst._nodes.expression import Name

class Test_CstTypedBaseFunctionsVisitAugAssignOperator:

    @pytest.mark.regression
    def test_visit_AugAssign_operator_no_op(self):
        name = Name(value="x")
        operator = AddAssign()
        aug_assign = AugAssign(target=name, operator=operator, value=name)
        visit_AugAssign_operator(aug_assign)
        assert aug_assign == AugAssign(target=name, operator=operator, value=name)

    @pytest.mark.negative
    def test_visit_AugAssign_operator_None(self):
        try:
            visit_AugAssign_operator(None)
            assert True
        except Exception as e:
            pytest.fail(f"Test failed: {e}")

    @pytest.mark.regression
    @pytest.mark.parametrize("assign_operator", [AddAssign(), SubtractAssign(), MultiplyAssign()])
    def test_visit_AugAssign_operator_diff_params(self, assign_operator):
        name = Name(value="x")
        aug_assign = AugAssign(target=name, operator=assign_operator, value=name)
        visit_AugAssign_operator(aug_assign)
        assert aug_assign == AugAssign(target=name, operator=assign_operator, value=name)
