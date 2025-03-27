import pytest
from libcst._nodes.statement import AnnAssign
from _typed_visitor import visit_AnnAssign_equal

class Test_CstTypedBaseFunctionsVisitAnnAssignEqual:
    @pytest.mark.valid
    def test_unchanged_node_after_visit(self):
        # Arrange
        node = AnnAssign()
        original_node = deepcopy(node)
        
        # Act
        visit_AnnAssign_equal(node)
        
        # Assert
        assert node == original_node, "The node has been modified after visit_AnnAssign_equal"
        
    @pytest.mark.invalid
    def test_node_type_accepted(self):
        # Arrange
        node = "Invalid Node"
        
        # Act and Assert
        with pytest.raises(TypeError): # we expect a TypeError because node is not of type AnnAssign
            visit_AnnAssign_equal(node)
            
    @pytest.mark.negative
    def test_handle_none_input(self):
        # Act and Assert
        with pytest.raises(Exception):
            visit_AnnAssign_equal(None)
