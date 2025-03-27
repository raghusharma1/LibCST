import pytest
from _typed_visitor import CSTTypedBaseFunctions, leave_AssignEqual_whitespace_after
from libcst._nodes.op import AssignEqual

class Test_CstTypedBaseFunctionsLeaveAssignEqualWhitespaceAfter:

    def test_AssignEqual_leave_whitespace_after(self):
        cst_functions = CSTTypedBaseFunctions()
        assignequal_node = AssignEqual()

        # No assertion as the function returns None and is expected to always complete successfully
        cst_functions.leave_AssignEqual_whitespace_after(assignequal_node)


    def test_AssignEqual_Node_accepted(self):
        cst_functions = CSTTypedBaseFunctions()
        not_assignequal_node = 'Not AssignEqual Node'   # a node which is not of type AssignEqual

        # Assert that TypeError is raised as the mock node is not of type AssignEqual 
        with pytest.raises(TypeError):
            cst_functions.leave_AssignEqual_whitespace_after(not_assignequal_node)


    def test_AssignEqual_leave_whitespace_after_idempotence(self):
        cst_functions = CSTTypedBaseFunctions()
        assignequal_node = AssignEqual()

        # Assert that the function is idempotent
        for _ in range(10):   # invoke function multiple times
            cst_functions.leave_AssignEqual_whitespace_after(assignequal_node)
        # No assertion as the function has no side effects and is expected to always complete successfully
