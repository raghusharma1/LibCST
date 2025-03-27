import pytest
from _typed_visitor import leave_AugAssign_value
from libcst._nodes.statement import AugAssign
from libcst._nodes.op import Add, AddAssign
from libcst._nodes.expression import Name, Integer

class Test_CstTypedBaseFunctionsLeaveAugAssignValue:
    
    class Tester:
        def leave_AugAssign_value(self, node: "AugAssign") -> None:
            return leave_AugAssign_value(self, node)

    @pytest.mark.parametrize("node", [(AugAssign(Name("x"), Add(), Integer(1)))])
    def test_leave_AugAssign_value_no_operation(self, node):
        tester = self.Tester()
        try:
            node_before = node.deep_clone()
            tester.leave_AugAssign_value(node)
            assert node == node_before, "leave_AugAssign_value altered the AugAssign node"
        except Exception as e:
            pytest.fail(f"leave_AugAssign_value raised an exception unexpectedly: {str(e)}", False)

    @pytest.mark.parametrize("node", [(AugAssign(Name("x"), AddAssign(), Integer(2)))])
    def test_leave_AugAssign_value_invocation(self, node):
        tester = self.Tester()
        try:
            tester.leave_AugAssign_value(node)
        except Exception as e:
            pytest.fail(f"leave_AugAssign_value raised an exception unexpectedly: {str(e)}", False)

    @pytest.mark.parametrize("node", [(AugAssign(Name("x"), Add(), Integer(3)))])
    def test_leave_AugAssign_value_input_type(self, node):
        tester = self.Tester()
        try:
            tester.leave_AugAssign_value(node)
        except Exception as e:
            pytest.fail(f"leave_AugAssign_value raised an exception unexpectedly: {str(e)}", False)
