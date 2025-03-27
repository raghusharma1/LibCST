import pytest
from libcst._typed_visitor import leave_Await_rpar
from libcst import Await, FlattenSentinel, MaybeSentinel, RemovalSentinel
from libcst._nodes.module import Module
from libcst._nodes.expression import Integer

# starting class definition
class Test_CstTypedBaseFunctionsLeaveAwaitRpar:

    # Test Case for Scenario 1: Testing leave_Await_rpar function with valid Await node
    # Execution: The function should not raise any exception as the node is correct.
    def test_leave_await_rpar_correct_node(self):
        node = Await()   # Correct node Initialisation
        try:
            leave_Await_rpar(node)  # Act
        except Exception as exc:
            pytest.fail("Test failed. Unexpected Exception: {}. leave_Await_rpar should have handled it.".format(exc))
    
    # Test Case for Scenario 2: Testing leave_Await_rpar function with an incorrect node
    # Execution: Even though the node is incorrect, the function leave_Await_rpar does nothing and should pass without raising any error or exception.
    def test_leave_await_rpar_incorrect_node(self):
        node = Module()  # Incorrect node initialisation
        try:
            leave_Await_rpar(node)  # Act
        except Exception as exc:
            pytest.fail("Test failed. Unexpected Exception: {}. leave_Await_rpar should have handled it.".format(exc))

    # Test Case for Scenario 3: Testing leave_Await_rpar function with None node
    # Execution: Calling the function with None as the node. As per implementation, the function does nothing so it should not raise any error or exception for None.
    def test_leave_await_rpar_none_node(self):
        node = None
        try:
            leave_Await_rpar(node)  # Act
        except Exception as exc:
            pytest.fail("Test failed. Unexpected Exception: {}. leave_Await_rpar should have handled None.".format(exc))
    
    # Test Case for Scenario 4: Testing leave_Await_rpar function for other acceptable objects
    # Execution: Creating different nodes using acceptable objects such as FlattenSentinel, MaybeSentinel, RemovalSentinel
    # Since the function leave_Await_rpar does nothing, it should not raise any error or exception for these objects.
    def test_leave_await_rpar_other_acceptable_objects(self):
        nodes = [FlattenSentinel, MaybeSentinel, RemovalSentinel, Integer(5)] # Acceptable objects 
        for node in nodes:
            try:
                leave_Await_rpar(node)  # Act
            except Exception as exc:
                pytest.fail("Test failed for object: {}. Unexpected Exception: {}. leave_Await_rpar should have handled it.".format(node, exc))

