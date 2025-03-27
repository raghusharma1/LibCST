import pytest
from libcst._nodes.op import BitAndAssign, AddAssign
from _typed_visitor import leave_BitAndAssign_whitespace_after

class Test_CstTypedBaseFunctionsLeaveBitAndAssignWhitespaceAfter:

    @pytest.mark.smoke
    @pytest.mark.positive
    def test_BitAndAssign_whitespace_after_with_node_argument(self):
        # Arrange: Create a new instance of the BitAndAssign node object.
        bit_and_assign_node = BitAndAssign()

        # Act: Invoke the leave_BitAndAssign_whitespace_after function by passing in the BitAndAssign node object instance.
        # Assert: Check if the function doesn't return any value and doesn't raise any exceptions.
        assert leave_BitAndAssign_whitespace_after(bit_and_assign_node) is None

    @pytest.mark.negative
    def test_BitAndAssign_whitespace_after_with_invalid_node(self):
        # Arrange: Create an instance of a different node object type, such as AddAssign.
        add_assign_node = AddAssign()

        # Act & Assert: Try to invoke the leave_BitAndAssign_whitespace_after function by passing in the different node object instance.
        # Confirm that an appropriate exception (TypeError) is raised.        
        with pytest.raises(TypeError):
            leave_BitAndAssign_whitespace_after(add_assign_node)

    @pytest.mark.negative
    def test_BitAndAssign_whitespace_after_without_node_argument(self):
        # Act & Assert: Invoke the function leave_BitAndAssign_whitespace_after without parameters.
        # Ensure that an appropriate exception (TypeError) is raised due to the absence of the expected arguments.       
        with pytest.raises(TypeError):
            leave_BitAndAssign_whitespace_after()
