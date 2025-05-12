import pytest
from libcst._nodes.statement import Assert
from _typed_visitor import leave_Assert_semicolon

# The test class
class Test_CstTypedBaseFunctionsLeaveAssertSemicolon:
    def test_assert_invocation(self):
        # Arrange
        assert_node = Assert()

        # Act and Assert  
        # No exceptions are expected to be raised
        try:
            leave_Assert_semicolon(assert_node)
        except Exception:
            assert False, "Test failed: leave_Assert_semicolon() throws an exception unexpectedly."
        
    def test_assert_no_return(self):
        # Arrange
        assert_node = Assert()
        
        # Act
        result = leave_Assert_semicolon(assert_node)

        # Assert
        assert result is None, "Test failed: leave_Assert_semicolon() returned a result. No return value was expected."
    
    def test_assert_none_argument(self):
        # Act and Assert  
        # No exceptions are expected to be raised  
        try:
            leave_Assert_semicolon(None)
        except Exception:
            assert False, "Test failed: leave_Assert_semicolon() throws an exception unexpectedly."

    def test_assert_incorrect_data_type(self):
        # Arrange
        not_assert_node = "Not assert node"

        # Act and Assert  
        # TypeError is expected to be raised
        with pytest.raises(TypeError):
            leave_Assert_semicolon(not_assert_node)
