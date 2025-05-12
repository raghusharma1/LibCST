import pytest
from libcst._nodes.statement import Assign, AssignTarget, Name
from libcst import Integer
from _typed_visitor import leave_Assign_value
from typing import TYPE_CHECKING


class Test_CstTypedBaseFunctionsLeaveAssignValue:
    
    @pytest.mark.regression
    def test_leave_assign_value_default_node(self):
        node = Assign(targets=[AssignTarget(target=Name("x"))], value=Integer("1"))
        try:
            leave_Assign_value(node)
        except:
            pytest.fail("leave_Assign_value threw an exception on default node")

    @pytest.mark.regression
    def test_leave_assign_value_customized_node(self):
        node = Assign(targets=[AssignTarget(target=Name("custom"))], value=Integer("2"))
        try:
            leave_Assign_value(node)
        except:
            pytest.fail("leave_Assign_value threw an exception on customized node")

    @pytest.mark.regression
    def test_leave_assign_value_empty_node(self):
        node = Assign(targets=[], value=None)
        try:
            leave_Assign_value(node)
        except:
            pytest.fail("leave_Assign_value threw an exception on empty node")
