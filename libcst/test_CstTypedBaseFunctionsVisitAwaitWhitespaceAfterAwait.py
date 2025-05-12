import pytest
from _typed_visitor import visit_Await_whitespace_after_await
from libcst._nodes.expression import Await
from unittest.mock import Mock
import time

class Test_CstTypedBaseFunctionsVisitAwaitWhitespaceAfterAwait:

    @pytest.mark.default_behavior
    def test_default_behavior(self):
        # Arrange: We need to first initialize an "Await" node
        mock_node = Await(Whitespace(" "))

        # Act: The function visit_Await_whitespace_after_await is then called
        visit_Await_whitespace_after_await(mock_node)

        # Assert: The status of the Await node should remain unchanged
        assert mock_node == Await(Whitespace(" "))


    @pytest.mark.null_node_handling
    def test_null_node_handling(self):
        # Arrange: No preparation is required as we'll be passing in a null node

        # Act & Assert: No exceptions should be thrown
        try:
            visit_Await_whitespace_after_await(None)
            
        except Exception as e:
            pytest.fail(f"Test failed due to exception: {e}")


    @pytest.mark.performance
    def test_response_time(self):
        # Arrange: Initialization of a timer before invoking the function is required
        start_time = time.time()

        # Act: The function visit_Await_whitespace_after_await with a dummy Await node
        visit_Await_whitespace_after_await(Await(Whitespace(" ")))

        # Assert: The timer stops right after the function execution to calculate the function response time
        end_time = time.time()
        execution_time = end_time - start_time
        assert execution_time < 0.001, "Test failed because it took more than 1 millisecond to execute."
