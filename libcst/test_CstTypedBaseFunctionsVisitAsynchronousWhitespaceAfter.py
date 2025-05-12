import pytest
from typing import Optional
from libcst import Asynchronous, BaseParenthesizableWhitespace, SimpleWhitespace
from _typed_visitor import visit_Asynchronous_whitespace_after

class Test_CstTypedBaseFunctionsVisitAsynchronousWhitespaceAfter:

    @pytest.mark.valid
    def test_visit_Asynchronous_whitespace_after_with_valid_node(self):
        # Arrange: Create a new "Asynchronous" node.
        node = Asynchronous()
        # Act: Invoke "visit_Asynchronous_whitespace_after" function on the created "Asynchronous" node.
        # Assert: Check if the function execution does not raise any error or exceptions.
        try:
            visit_Asynchronous_whitespace_after(node)
        except Exception:
            pytest.fail("visit_Asynchronous_whitespace_after failed with valid node")

    @pytest.mark.negative
    def test_visit_Asynchronous_whitespace_after_with_none(self):
        with pytest.raises(TypeError):
            visit_Asynchronous_whitespace_after(None)

    @pytest.mark.negative
    def test_visit_Asynchronous_whitespace_after_with_different_nodes(self):
        different_nodes = [BaseParenthesizableWhitespace(), SimpleWhitespace()]
        for node in different_nodes:
            with pytest.raises(TypeError):
                visit_Asynchronous_whitespace_after(node)

    @pytest.mark.valid
    def test_visit_Asynchronous_whitespace_after_with_whitespace_node(self):
        # Arrange: Create a new "Asynchronous" node with additional whitespace.
        node = Asynchronous(whitespace_after=SimpleWhitespace(value=' '))
        # Act: Invoke "visit_Asynchronous_whitespace_after" function on the created "Asynchronous" node.
        # Assert: Check if the function execution does not lead to any error or exceptions.
        try:
            visit_Asynchronous_whitespace_after(node)
        except Exception:
            pytest.fail("visit_Asynchronous_whitespace_after failed with valid node containing whitespace")
