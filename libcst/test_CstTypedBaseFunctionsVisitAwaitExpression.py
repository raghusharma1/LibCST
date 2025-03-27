# Importing required libraries
from _typed_visitor import visit_Await_expression
from libcst._nodes.expression import Await
from typing import Optional, TYPE_CHECKING
import pytest

# Test_CstTypedBaseFunctionsVisitAwaitExpression class definition containing the unit test methods
class Test_CstTypedBaseFunctionsVisitAwaitExpression:

    # Test case for visit_Await_expression successful execution
    @pytest.mark.positive
    def test_visit_await_expression_function_positive(self):

        # Arrange
        await_node_instance = Await()

        # Act and Assert: Check if it is possible to call the function using an Await node instance
        assert visit_Await_expression(await_node_instance) == None, "Function did not execute successfully with Await node"
       
    # Test case for visit_Await_expression function with None node
    @pytest.mark.negative
    def test_visit_await_expression_function_none_node(self):

        # Arrange
        none_node = None

        # Act and Assert: Checking if an exception is raised when a None node is passed
        with pytest.raises(TypeError):
            visit_Await_expression(none_node)

    # Test case for visit_Await_expression with non-await node
    @pytest.mark.negative
    def test_visit_await_expression_non_await_node(self):

        # Arrange
        non_await_node = "This is not an Await Node"

        # Act and Assert: Check if it is possible to call the function using a non-await node instance
        assert visit_Await_expression(non_await_node) == None, "Function did not execute successfully with non-await node"
