import pytest
from libcst._nodes.op import BitAndAssign
from _typed_visitor import visit_BitAndAssign
from typing import Optional

class Test_CstTypedBaseFunctionsVisitBitAndAssign:

    @pytest.mark.parametrize("node", [BitAndAssign()])
    def test_visit_bit_and_assign_node(self, node):
        """
        Test 'visit_BitAndAssign' when passed a BitAndAssign node
        """
        try:
            visit_BitAndAssign(node)
        except Exception as error:
            pytest.fail(f"visit_BitAndAssign() raised an error unexpectedly, the error: {error}")

    @pytest.mark.parametrize("node", [1, "string", 0.1])
    def test_visit_bit_and_assign_non_node(self, node):
        """
        Test 'visit_BitAndAssign' when passed a non-BitAndAssign node
        """
        try:
            visit_BitAndAssign(node)
        except Exception as error:
            pytest.fail(f"visit_BitAndAssign() raised an error unexpectedly, the error: {error}")

    @pytest.mark.parametrize("node", [None])
    def test_visit_bit_and_assign_non_node_with_none(self, node):
        """
        Test 'visit_BitAndAssign' when passed a None value
        """
        try:
            visit_BitAndAssign(node)
        except Exception as error:
            pytest.fail(f"visit_BitAndAssign() raised an error unexpectedly, the error: {error}")
