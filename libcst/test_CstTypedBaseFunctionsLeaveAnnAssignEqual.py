import pytest
from libcst._typed_visitor import leave_AnnAssign_equal
from libcst._nodes.statement import AnnAssign, Assign, FunctionDef
from libcst._nodes.base import CSTNode

class Test_CstTypedBaseFunctionsLeaveAnnAssignEqual:

    def test_leave_AnnAssign_equal_default_execution(self):
        # Arrange
        test_node = AnnAssign()

        # Act
        # No exception should be raised
        leave_AnnAssign_equal(test_node)

    def test_leave_AnnAssign_equal_with_various_nodes(self):
        # Arrange
        test_nodes = [AnnAssign(), AnnAssign(), AnnAssign()]

        # Act and Assert
        # No exception should be raised
        for test_node in test_nodes:
            leave_AnnAssign_equal(test_node)

    def test_leave_AnnAssign_equal_with_non_AnnAssign_instances(self):
        # Arrange
        test_nodes = [Assign(), CSTNode(), FunctionDef()]

        # Act and Assert
        # Exception should be raised
        for test_node in test_nodes:
            with pytest.raises(TypeError):
                leave_AnnAssign_equal(test_node)

