import pytest
from _typed_visitor import visit_Assign
from libcst._nodes.statement import Assign
from typing import Optional

class Test_CstTypedBaseFunctionsVisitAssign:

    # Scenario 1: Test Assign Visit Method with an Empty Node
    @pytest.mark.parametrize("node", [None])
    def test_visit_assign_method_empty_node(self, node):
        assert visit_Assign(node) is None

    # Scenario 2: Test Assign Visit Method with an Assigned Node
    @pytest.mark.parametrize("node", [Assign(targets=[], value="some_value")])
    def test_visit_assign_method_assigned_node(self, node):
        assert visit_Assign(node) is None

    # Scenario 3: Test Incorrect Node Type Passed to visit_Assign Method
    @pytest.mark.parametrize("node", ["not_a_node"])
    def test_visit_assign_method_incorrect_node(self, node):
        with pytest.raises(TypeError):
            visit_Assign(node)
