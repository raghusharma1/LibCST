# Import necessary standard libraries and class methods
import pytest
from _typed_visitor import leave_Asynchronous_whitespace_after
from libcst._nodes.expression import Asynchronous

# Define Test_CstTypedBaseFunctionsLeaveAsynchronousWhitespaceAfter class
class Test_CstTypedBaseFunctionsLeaveAsynchronousWhitespaceAfter:
  
    @pytest.mark.valid
    def test_valid_operation_leave_Asynchronous_whitespace_after(self):
        # Arrange
        node = Asynchronous()

        # Act and Assert
        try:
            leave_Asynchronous_whitespace_after(node)
        except Exception as e:
            pytest.fail(f"Test failed due to unexpected error: {e}")

        assert True, "Test passed!"

    @pytest.mark.invalid
    def test_non_asynchronous_node_handling(self):
        # Arrange
        node = "Not An Asynchronous Node"

        # Act and Assert
        try:
            leave_Asynchronous_whitespace_after(node)
        except Exception as e:
            pytest.fail(f"Test failed due to unexpected error: {e}")

        assert True, "Test passed despite not an Asynchronous node!"

    @pytest.mark.regression
    def test_multiple_sequential_calls(self):
        # Arrange
        node = Asynchronous()

        # Act and Assert
        for _ in range(10):
            try:
                leave_Asynchronous_whitespace_after(node)
            except Exception as e:
                pytest.fail(f"Test failed in iteration due to unexpected error: {e}")

        assert True, "Test passed for multiple sequential calls!"
