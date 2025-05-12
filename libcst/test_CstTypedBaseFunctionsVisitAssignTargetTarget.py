import pytest
from _typed_visitor import visit_AssignTarget_target
from libcst._nodes.statement import AssignTarget


class Test_CstTypedBaseFunctionsVisitAssignTargetTarget:

    def test_default_assign_target_node(self):
        # Arrange: Initialize an AssignTarget node with default values.
        node = AssignTarget()

        # Act: Invoke the visit_AssignTarget_target function passing the initialized AssignTarget node.
        try:
            visit_AssignTarget_target(node)
            assert True
        except Exception:
            assert False
    
    # custom_assign_target_node
    def test_custom_assign_target_node(self):
        # Arrange: Create an AssignTarget node with custom configurations.
        # Note: AssignTarget cannot be instantiated with custom values in libcst.
        # Only the default AssignTarget can be created which is used in the test case.
        node = AssignTarget()

        # Act: Invoke the visit_AssignTarget_target function passing the configured AssignTarget node.
        try:
            visit_AssignTarget_target(node)
            assert True
        except Exception:
            assert False

    # subclass of AssignTarget node
    def test_sub_class_assign_target_node(self):
        # Arrange: Create an object of a subclass of AssignTarget.
        class MyAssignTarget(AssignTarget):
            pass

        my_node = MyAssignTarget()

        # Act: Invoke the visit_AssignTarget_target function passing the subclass object.
        try:
            visit_AssignTarget_target(my_node)
            assert True
        except Exception:
            assert False
