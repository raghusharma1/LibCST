import pytest
from _typed_visitor import leave_And_whitespace_after
from libcst._nodes.op import And
from typing import Optional, TYPE_CHECKING, Union

class Test_CstTypedBaseFunctionsLeaveAndWhitespaceAfter:
    @pytest.mark.regression
    def test_leave_and_whitespace_after_handling(self):
        try:
            sample_and_node = And()
            leave_And_whitespace_after(self=optional, node=sample_and_node)
        except Exception as e:
            pytest.fail(f"Test failed due to: {e}")

    @pytest.mark.valid
    def test_leave_and_whitespace_after_with_other_inputs(self):
        with pytest.raises(TypeError):
            sample_non_and_node = None  # TODO: Replace None with a node of any type other than And
            leave_And_whitespace_after(self=optional, node=sample_non_and_node)

    @pytest.mark.valid
    def test_leave_and_whitespace_after_without_input(self):
        with pytest.raises(TypeError):
            leave_And_whitespace_after(self=optional, node=None)
