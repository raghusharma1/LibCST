# ********RoostGPT********
"""
Test generated by RoostGPT for test pythonHTest5 using AI Type Azure Open AI and AI Model roostgpt-4-32k

Test generated by RoostGPT for test pythonHTest5 using AI Type Azure Open AI and AI Model roostgpt-4-32k

ROOST_METHOD_HASH=visit_AnnAssign_equal_0171b13e54
ROOST_METHOD_SIG_HASH=visit_AnnAssign_equal_51a54744cb


Scenario 1: Verify if visit_AnnAssign_equal method does not change original node
Details:
  TestName: test_unchanged_node_after_visit
  Description: This test is intended to verify whether the function visit_AnnAssign_equal does not modify the original node.
Execution:
  Arrange: Instantiate an AnnAssign node.
  Act: Invoke the visit_AnnAssign_equal function with the instantiated AnnAssign node as argument.
  Assert: The AnnAssign node remains unmodified after the function visit_AnnAssign_equal is executed.
Validation:
  The function is expected not to modify the original node. Therefore, the test helps validate the function's adherence to this specification and ensures consistency of use.

Scenario 2: Verify the type of node visit_AnnAssign_equal method accepts
Details:
  TestName: test_node_type_accepted
  Description: This test is intended to ascertain that the visit_AnnAssign_equal function only operates on instances of the AnnAssign node.
Execution:
  Arrange: Instantiate a node of a different class from AnnAssign. 
  Act: Invoke the visit_AnnAssign_equal function with the instantiated node as argument.
  Assert: The function should raise an exception or error as it should only operate on AnnAssign nodes.
Validation:
  This test is crucial to ensure that the function operates as intended, only with AnnAssign nodes. It helps avoid unintended side effects of using this function with unsupported node types.

Scenario 3: Verify if visit_AnnAssign_equal method can handle None as input
Details:
  TestName: test_handle_none_input
  Description: This test is intended to determine if visit_AnnAssign_equal method can handle None as an input.
Execution:
  Arrange: No objects require initialization for this test.
  Act: Call visit_AnnAssign_equal function with None as an argument.
  Assert: Function handles None without raising an exception.
Validation:
  Often times, None values can occur unexpectedly. This test ensures that the function visit_AnnAssign_equal can handle None inputs gracefully without throwing an exception.
"""

# ********RoostGPT********
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
