import pytest
from _typed_visitor import visit_And_whitespace_before
from libcst._nodes.op import And, Or

class Test_CstTypedBaseFunctionsVisitAndWhitespaceBefore:

    @pytest.mark.valid
    def test_And_node_execution(self):
        and_node_instance = And()
        try:
            visit_And_whitespace_before(and_node_instance)
        except Exception as e:
            pytest.fail(f"visit_And_whitespace_before({and_node_instance}) raised {type(e).__name__} unexpectedly!")
    
    @pytest.mark.valid
    def test_non_And_nodes(self):
        or_node_instance = Or()
        try:
            visit_And_whitespace_before(or_node_instance)
        except Exception as e:
            pytest.fail(f"visit_And_whitespace_before({or_node_instance}) raised {type(e).__name__} unexpectedly!")
            
    @pytest.mark.negative
    def test_null_input(self):
        try:
            visit_And_whitespace_before(None)
        except Exception as e:
            pytest.fail(f"visit_And_whitespace_before(None) raised {type(e).__name__} unexpectedly!")
