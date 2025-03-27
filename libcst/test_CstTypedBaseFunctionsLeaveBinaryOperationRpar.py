import pytest
from _typed_visitor import leave_BinaryOperation_rpar
from libcst._nodes.expression import BinaryOperation, Float

class Test_CstTypedBaseFunctionsLeaveBinaryOperationRpar:
    @pytest.mark.regression
    def test_normal_invocation(self):
        bin_op_node = BinaryOperation()

        try:
            leave_BinaryOperation_rpar(bin_op_node)
        except Exception as e:
            pytest.fail(f"Unexpected exception {e}")

        assert bin_op_node == BinaryOperation(), 'The function changes the node'


    @pytest.mark.regression
    def test_invocation_with_none(self):
        with pytest.raises(TypeError):
            leave_BinaryOperation_rpar(None)


    @pytest.mark.regression
    def test_invocation_with_sub_class(self):
        node = Float(0.0)

        old_node = node
        try:
            leave_BinaryOperation_rpar(node)
        except Exception as e:
            pytest.fail(f"Unexpected exception {e}")

        assert node == old_node, 'The function changes the node'
