import pytest
from _typed_visitor import leave_AnnAssign_target
from libcst._nodes.statement import AnnAssign
from libcst import AnnAssign, Name, Assign, Integer
from copy import deepcopy

class Test_CstTypedBaseFunctionsLeaveAnnAssignTarget:

    @pytest.mark.regression
    def test_leave_AnnAssign_target_NoOp(self):
        ann_assign_node = AnnAssign(Name('test_var'), Assign(), Integer(10))
        result_node = deepcopy(ann_assign_node)
        leave_AnnAssign_target(ann_assign_node)
        assert ann_assign_node == result_node, "No-Op property of leave_AnnAssign_target failed."

    @pytest.mark.error_handling
    def test_leave_AnnAssign_target_NoneArgument(self):
        try:
            leave_AnnAssign_target(None)
        except Exception as e:
            pytest.fail(f"leave_AnnAssign_target should not raise exceptions. Encountered {e}")

    @pytest.mark.repeated_call
    def test_leave_AnnAssign_target_MultipleCalls(self):
        ann_assign_node = AnnAssign(Name('test_var'), Assign(), Integer(10))
        leave_AnnAssign_target(ann_assign_node)
        post_first_call_node = deepcopy(ann_assign_node)
        for _ in range(3):
            leave_AnnAssign_target(ann_assign_node)
        assert ann_assign_node == post_first_call_node, "Repeated calls to leave_AnnAssign_target cause mutation."

    @pytest.mark.dynamic_node
    def test_leave_AnnAssign_target_DynamicNodes(self):
        dynamic_node = AnnAssign(Name(f'test_var_{i}'), Assign(), Integer(i)) for i in range(5)
        for node in dynamic_node:
            original_node = deepcopy(node)
            leave_AnnAssign_target(node)
            assert node == original_node, "Dynamically created nodes are not handled properly by leave_AnnAssign_target."
