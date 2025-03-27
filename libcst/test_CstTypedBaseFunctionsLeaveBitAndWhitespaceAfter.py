# Import required libraries
import pytest
from _typed_visitor import leave_BitAnd_whitespace_after
from libcst._nodes.op import BitAnd
from libcst import Module
from libcst.metadata import MetadataWrapper

# Define the test class
class Test_CstTypedBaseFunctionsLeaveBitAndWhitespaceAfter:
    
    # Test Scenario 1
    def test_leave_BitAnd_whitespace_after_intact_node(self):
        # arrange
        bitand_node = BitAnd()
        # act
        leave_BitAnd_whitespace_after(bitand_node)
        # assert
        assert bitand_node == BitAnd()

    # Test Scenario 2
    def test_leave_BitAnd_whitespace_after_non_BitAnd_handling(self):
        # Test data structures should be declared within Test functions
        # arrange
        non_bitand_node = "SomeString"
        original_non_bitand_node = non_bitand_node
        # act
        leave_BitAnd_whitespace_after(non_bitand_node)
        # assert
        assert non_bitand_node == original_non_bitand_node

    # Test Scenario 3
    def test_leave_BitAnd_whitespace_after_in_actual_code(self):
        # arrange
        script = "10 & 20"
        node = Module.parse(script).body[0]
        original_node = node
        # act
        leave_BitAnd_whitespace_after(node)
        # assert
        assert node == original_node
