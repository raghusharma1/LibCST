import pytest
from libcst._nodes.statement import AugAssign
from libcst._nodes.op import AddAssign, AssignEqual
from libcst._nodes.expression import Name
from _typed_visitor import visit_AugAssign

# Below are the pytest unit tests for different scenarios specified above.

class Test_CstTypedBaseFunctionsVisitAugAssign:

    @pytest.mark.regression
    def test_valid_AugAssign_node_visit(self):
        # Test Scenario 1: Visiting Valid AugAssign Node
        # Arrange
        valid_node = AugAssign(target=Name("x"), op=AddAssign(), value=Name("y"))
        # Act
        try:
            visit_AugAssign(valid_node)
        # Assert
        except Exception as e:
            pytest.fail(f"Test failed with error: {str(e)}")

    @pytest.mark.regression
    def test_empty_AugAssign_node_visit(self):
        # Test Scenario 2: Visiting an Empty AugAssign Node 
        # Arrange
        empty_node = AugAssign(target=None, op=None, value=None)
        # Act
        try:
            visit_AugAssign(empty_node)
        # Assert
        except Exception as e:
            pytest.fail(f"Test failed with error: {str(e)}")

    @pytest.mark.regression
    def test_nested_AugAssign_node_visit(self):
        # Test Scenario 3: Visiting AugAssign Node With Nested AugAssign Nodes
        # Arrange
        nested_node = AugAssign(
            target=Name("x"), 
            op=AddAssign(), 
            value=AugAssign(
                target=Name("y"), 
                op=AssignEqual(),
                value=Name("z"))
        )
        # Act
        try:
            visit_AugAssign(nested_node)
        # Assert
        except Exception as e:
            pytest.fail(f"Test failed with error: {str(e)}")
