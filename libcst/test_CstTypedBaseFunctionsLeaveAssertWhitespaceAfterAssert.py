import pytest
from libcst._nodes.statement import Assert
from libcst._nodes.whitespace import SimpleWhitespace
from _typed_visitor import leave_Assert_whitespace_after_assert

class Test_CstTypedBaseFunctionsLeaveAssertWhitespaceAfterAssert:

    @pytest.mark.smoke
    def test_default_behavior(self):
        test_assert = Assert(test=SimpleWhitespace(value=''))
        assert leave_Assert_whitespace_after_assert(test_assert) == None

    @pytest.mark.regression
    def test_assert_contains_whitespace(self):
        test_assert = Assert(test=SimpleWhitespace(value=' '))
        original_assert = test_assert
        leave_Assert_whitespace_after_assert(test_assert)
        assert test_assert == original_assert

    @pytest.mark.regression
    def test_handling_of_subclass(self):
        class SubAssert(Assert):
            pass

        test_assert = SubAssert(test=SimpleWhitespace(value=''))
        original_assert = test_assert
        leave_Assert_whitespace_after_assert(test_assert)
        assert test_assert == original_assert
        assert leave_Assert_whitespace_after_assert(test_assert) == None
