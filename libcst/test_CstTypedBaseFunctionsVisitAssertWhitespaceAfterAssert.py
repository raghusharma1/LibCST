import pytest
from _typed_visitor import visit_Assert_whitespace_after_assert
from libcst._nodes.statement import Assert, Return
from libcst._exceptions import CSTValidationError

class Test_CstTypedBaseFunctionsVisitAssertWhitespaceAfterAssert:

    def test_whitespace_after_assert_with_assert_node(self):
        test_object = Assert()
        # No Exception should be raised when a right type is provided
        try:
            visit_Assert_whitespace_after_assert(test_object)
        except Exception:
            pytest.fail("Unexpected Exception raised!")

    def test_whitespace_after_assert_with_non_existing_node(self):
        test_object = "non_existing_node"
        # An exception expected when wrong type is provided
        with pytest.raises(CSTValidationError):
            visit_Assert_whitespace_after_assert(test_object)

    def test_whitespace_after_assert_with_None(self):
        test_object = None
        try:
            visit_Assert_whitespace_after_assert(test_object)
        except Exception as err:
            pytest.fail("Unexpected Exception raised!")

    @pytest.mark.parametrize("node", [Return(), 123, "ABC", 12.34])
    def test_whitespace_after_assert_with_different_nodes(self, node):
        # Function should not raise exception for different type of nodes
        try:
            visit_Assert_whitespace_after_assert(node)
        except Exception:
            pytest.fail("Unexpected Exception raised!")
