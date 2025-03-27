import pytest
from _typed_visitor import visit_BitAnd_whitespace_before
from libcst._nodes.op import BitAnd, Add, AssignEqual

class Test_CstTypedBaseFunctionsVisitBitAndWhitespaceBefore:

    @pytest.mark.regression
    def test_visit_BitAnd_whitespace_before_basic(self):
        bitand_node = BitAnd() # Initialize the BitAnd node
        try:
            visit_BitAnd_whitespace_before(bitand_node) # Invoke the visit_BitAnd_whitespace_before method passing the BitAnd node as a parameter
        except Exception:
            pytest.fail("visit_BitAnd_whitespace_before raised an exception unexpectedly!")
    
    @pytest.mark.regression
    def test_visit_BitAnd_whitespace_before_different_node(self):
        add_node = Add() # Initialize other type of node
        assignequal_node = AssignEqual() # Initialize other type of node
        try:
            visit_BitAnd_whitespace_before(add_node) # Invoke the visit_BitAnd_whitespace_before method passing the initialized node as a parameter
            visit_BitAnd_whitespace_before(assignequal_node) # Invoke the visit_BitAnd_whitespace_before method passing the initialized node as a parameter
        except Exception:
            pytest.fail("visit_BitAnd_whitespace_before raised an exception unexpectedly!")
    
    @pytest.mark.negative
    def test_visit_BitAnd_whitespace_before_no_parameters(self):
        try:
            visit_BitAnd_whitespace_before() # Invoke the visit_BitAnd_whitespace_before method without any parameters
        except Exception:
            pytest.fail("visit_BitAnd_whitespace_before raised an exception unexpectedly!")
