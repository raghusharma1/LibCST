import pytest
from libcst import AsName, SimpleWhitespace
from _typed_visitor import visit_AsName_whitespace_before_as

class Test_CstTypedBaseFunctionsVisitAsNameWhitespaceBeforeAs:
    
    @pytest.mark.smoke
    def test_visit_AsName_whitespace_before_as_with_valid_node(self):
        valid_node = AsName("name", leading_lines=' ', whitespace_before_as=' ')
        try:
            visit_AsName_whitespace_before_as(valid_node)
        except Exception as e:
            pytest.fail(f"Test failed: {e.args[0]}")

    @pytest.mark.regression
    def test_visit_AsName_whitespace_before_as_with_whitespace_node(self):
        whitespace_node = AsName("name", SimpleWhitespace(" "), SimpleWhitespace(" "))
        try:
            visit_AsName_whitespace_before_as(whitespace_node)
        except Exception as e:
            pytest.fail(f"Test failed: {e.args[0]}")

    @pytest.mark.regression
    def test_visit_AsName_whitespace_before_as_with_varied_nodes(self):
        varied_nodes = [
            AsName("name", SimpleWhitespace(" ")),
            AsName("name", leading_lines=' ', whitespace_before_as=' '),
            AsName("name"),
        ]
        for node in varied_nodes:
            try:
                visit_AsName_whitespace_before_as(node)
            except Exception as e:
                pytest.fail(f"Test failed with node {node}: {e.args[0]}")

    @pytest.mark.regression
    def test_visit_AsName_whitespace_before_as_idempotency(self):
        idempotent_node = AsName("name", leading_lines=' ', whitespace_before_as=' ')
        try:
            node_initial = idempotent_node
            visit_AsName_whitespace_before_as(idempotent_node)
            visit_AsName_whitespace_before_as(idempotent_node)
            node_final = idempotent_node
            assert node_initial == node_final
        except Exception as e:
            pytest.fail(f"Test failed: {e.args[0]}")
