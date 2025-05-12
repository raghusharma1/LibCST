import pytest
from _typed_visitor import visit_AnnAssign_target
from libcst._nodes.statement import AnnAssign, AssignTarget, Name, SimpleWhitespace
from libcst import MaybeSentinel

class Test_CstTypedBaseFunctionsVisitAnnAssignTarget:

    def test_visit_annassign_target(self):
        # Arrange
        empty_node = AnnAssign(target=AssignTarget(Name("")), annotation=MaybeSentinel.DEFAULT, value=None)

        # Act
        try:
            visit_AnnAssign_target(empty_node)

        # Assert
        except:
            pytest.fail("visit_AnnAssign_target raised an exception on empty node")

    def test_visit_annassign_target_non_empty(self):
        # Arrange
        non_empty_node = AnnAssign(target=AssignTarget(Name("x")), annotation=MaybeSentinel.DEFAULT, value=None)

        # Act
        original_node = non_empty_node.deep_clone()
        visit_AnnAssign_target(non_empty_node)

        # Assert
        assert non_empty_node == original_node, "Node changed after function execution"

    def test_visit_annassign_target_instances(self):
        # Arrange
        nodes = [AnnAssign(target=AssignTarget(Name(chr(i))), annotation=MaybeSentinel.DEFAULT, value=None) for i in range(97, 123)]

        # Act
        results = [visit_AnnAssign_target(node) for node in nodes]

        # Assert
        assert all(result is None for result in results), "Function did not return None for all instances"
