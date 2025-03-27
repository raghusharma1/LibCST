import pytest
from libcst import AugAssign, AssignTarget, Name, Plus
from libcst._typed_visitor import visit_AugAssign_semicolon
from unittest.mock import MagicMock

class Test_CstTypedBaseFunctionsVisitAugAssignSemicolon:

    #Test Scenario 1: Callback functionality while visiting AugAssign_semicolon node 
    def test_visit_AugAssign_semicolon_callback_functionality(self):
        #Arrange: Prepare a 'AugAssign' node. Initialize a callback function for when the 'AugAssign' node is visited.
        node = AugAssign(target=AssignTarget(target=Name("a")), operator=Plus(), value=Name("b"), semicolon=MaybeSentinel.DEFAULT)
        cb = MagicMock()
        
        #Act: Call the function 'visit_AugAssign_semicolon' with the initialized node and the callback function.
        visit_AugAssign_semicolon(node, cb)
        
        #Assert: Check if the callback function was invoked during the visit.
        cb.assert_called_with(node)

    #Test Scenario 2: No callback functionality for Non-'AugAssign' node
    def test_visit_AugAssign_semicolon_for_non_AugAssign_nodes(self):
        #Arrange: Prepare a non-'AugAssign' node. Initialize a callback function for when an 'AugAssign' node is visited.
        node = Name("a") # An Example of a non-'AugAssign' node
        cb = MagicMock()
        
        #Act: Call the function 'visit_AugAssign_semicolon' with the non-'AugAssign' node and the callback function.
        visit_AugAssign_semicolon(node, cb)
        
        #Assert: Check whether the callback function was not called during the visit.
        cb.assert_not_called()

    #Test Scenario 3: Multiple 'AugAssign' nodes in tree
    def test_visit_AugAssign_semicolon_for_multiple_AugAssign_nodes(self):
        #Arrange: Prepare a tree with multiple 'AugAssign' nodes. Initialize a callback function to be triggered for each 'AugAssign' node visited.
        node1 = AugAssign(target=AssignTarget(target=Name("a")), operator=Plus(), value=Name("b"), semicolon=MaybeSentinel.DEFAULT)
        node2 = AugAssign(target=AssignTarget(target=Name("x")), operator=Plus(), value=Name("y"), semicolon=MaybeSentinel.DEFAULT)
        cb = MagicMock()

        tree = [node1, node2]
        expected_calls = [call(node1), call(node2)] # callback is expected to be called on both nodes
        
        #Act: Call the function 'visit_AugAssign_semicolon' with the prepared tree and the callback function.
        for node in tree:
            visit_AugAssign_semicolon(node, cb)
        
        #Assert: Verify that the callback function is triggered for each 'AugAssign' node.
        cb.assert_has_calls(expected_calls, any_order=False)
