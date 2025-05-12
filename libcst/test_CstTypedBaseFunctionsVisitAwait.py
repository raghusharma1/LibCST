import pytest
from _typed_visitor import visit_Await
from libcst._nodes.expression import Await
from typing import Optional

class Test_CstTypedBaseFunctionsVisitAwait:

    # Test visit_Await with an Await node
    def test_visit_await_with_valid_node(self):
        # Arrange
        node = Await()

        # Act
        result = visit_Await(node)

        # Assert
        assert result == Optional[bool], "Function should correctly process Await node"

    
    # Test visit_Await with a non-Await node
    def test_visit_await_with_invalid_node(self):
        # Arrange
        node = "Not a valid Await node"

        # Act
        with pytest.raises(TypeError):
            visit_Await(node)
        # No assert needed, as exception expectation is checked with pytest.raises
            
    
    # Test visit_Await with multiple Await nodes
    def test_visit_await_with_multiple_nodes(self):
        # Arrange
        nodes = [Await(), Await(), Await()]

        # Act
        results = [visit_Await(node) for node in nodes]
        
        # Assert
        for result in results:
            assert result == Optional[bool], "Function should correctly process Await node"
        
    
    # Test visit_Await with a null value
    def test_visit_await_with_no_node(self):
        # Arrange: No arrangement is needed in this scenario

        # Act
        with pytest.raises(TypeError):
            visit_Await(None)
        # No assert needed, as exception expectation is checked with pytest.raises
