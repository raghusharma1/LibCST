# Here are your tests:
import pytest
from libcst._nodes.op import BitAnd
from libcst._nodes.expression import Name
from _typed_visitor import visit_BitAnd_whitespace_after

class Test_CstTypedBaseFunctionsVisitBitAndWhitespaceAfter:
    def test_visit_BitAnd_whitespace_after_no_op(self):
        # Arrange
        node = BitAnd()
        original_id = id(node)

        # Act
        visit_BitAnd_whitespace_after(node)

        # Assert
        assert id(node) == original_id

    def test_visit_BitAnd_whitespace_after_with_non_BitAnd_input(self):
        # Arrange
        node = Name()

        # Act and assert
        try:
            visit_BitAnd_whitespace_after(node)
            assert True, "The function should not throw an exception"
        except Exception:
            pytest.fail("The function should not throw an exception")

    def test_visit_BitAnd_whitespace_after_chain_no_disruption(self):
        # Arrange
        node = BitAnd()

        # Define a chain of functions that are supposed to alter the initial list
        functions_to_apply = [
            lambda x: [1].append(x),
            visit_BitAnd_whitespace_after,
            lambda x: [2].append(x)
        ]

        # Act
        list_after_transformation = node
        for function in functions_to_apply:
            list_after_transformation = function(list_after_transformation)

        # Assert
        assert list_after_transformation == [1, 2]
