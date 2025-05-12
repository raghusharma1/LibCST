import pytest
from libcst import AssignTarget
from _typed_visitor import CSTTypedBaseFunctions

class Test_CstTypedBaseFunctionsLeaveAssignTargetTarget:

    @pytest.mark.parametrize('name_value', ['valid_node', 'other_name'])
    def test_leave_AssignTarget_target_with_valid_node(self, name_value):
        """
        Scenario 1: Check if the function runs with a valid "AssignTarget" node
        """
        cst_typed_base = CSTTypedBaseFunctions()
        valid_node = AssignTarget(Name(name_value))
        try:
            cst_typed_base.leave_AssignTarget_target(valid_node)
        except Exception as e:
            pytest.fail(f"Test failed with exception: {e}")

    @pytest.mark.parametrize('attr_value', ['attribute_a', 'attribute_b'])
    def test_leave_AssignTarget_target_with_node_with_attributes(self, attr_value):
        """
        Scenario 2: Test with an "AssignTarget" node having attributes
        """
        cst_typed_base = CSTTypedBaseFunctions()
        node_with_attributes = AssignTarget(Attribute(Name('node'), Name(attr_value)))
        try:
            cst_typed_base.leave_AssignTarget_target(node_with_attributes)
        except Exception as e:
            pytest.fail(f"Test failed with exception: {e}")
        
    @pytest.mark.parametrize('method_value', ['.methodOne()', '.methodTwo()'])
    def test_leave_AssignTarget_target_with_node_with_method_parts(self, method_value):
        """
        Scenario 3: Test with "AssignTarget" node having method parts
        """
        cst_typed_base = CSTTypedBaseFunctions()
        node_with_method_parts = AssignTarget(Attribute(Name('node') + method_value, Name('attr')))
        try:
            cst_typed_base.leave_AssignTarget_target(node_with_method_parts)
        except Exception as e:
            pytest.fail(f"Test failed with exception: {e}")
