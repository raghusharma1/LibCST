import pytest
import copy
from libcst._nodes.statement import AsName
from _typed_visitor import leave_AsName_whitespace_after_as

class Test_CstTypedBaseFunctionsLeaveAsNameWhitespaceAfterAs:
    
    @pytest.mark.regression
    def test_leave_AsName_whitespace_after_as_valid_node(self):
        as_name_node = AsName()
        try:
            leave_AsName_whitespace_after_as(as_name_node)
        except Exception as e:
            pytest.fail(f"Unexpected error occurred: {e}")
    
    @pytest.mark.regression
    def test_leave_AsName_whitespace_after_as_no_effect(self):
        as_name_node = AsName()
        as_name_node_copy = copy.deepcopy(as_name_node)
        
        leave_AsName_whitespace_after_as(as_name_node)
        
        assert as_name_node == as_name_node_copy, "The AsName node was modified by the function call"

    @pytest.mark.regression
    def test_leave_AsName_whitespace_after_as_idempotency(self):  
        as_name_node = AsName()
        initial_as_name_node = copy.deepcopy(as_name_node)
        
        # Invoke function multiple times
        for _ in range(10):
            leave_AsName_whitespace_after_as(as_name_node)
        
        assert as_name_node == initial_as_name_node, "The AsName node was modified by the function call"
