import pytest
from _typed_visitor import visit_Await_rpar
from libcst._nodes.expression import Await, ParamStar, LeftParen

@pytest.mark.unit
class Test_CstTypedBaseFunctionsVisitAwaitRpar:
    @pytest.mark.positive
    def test_visit_Await_rpar_with_Await_node(self):
        await_node = Await()
        # Achieve: No exception should be thrown. Function should not return a value
        try:
            visit_Await_rpar(await_node)
        except Exception as e:
            pytest.fail(f"visit_Await_rpar() raised an exception {e} unexpectedly!")

    @pytest.mark.negative
    def test_visit_Await_rpar_with_non_Await_node(self):
        # Arrange
        # Initialize non-await type node
        paramStar_node = ParamStar()
        leftParen_node = LeftParen()
        # Achieve: No exception should be thrown. Function should not return a value
        # Act & Assert for ParamStar node
        try:
            visit_Await_rpar(paramStar_node)
        except Exception as e:
            pytest.fail(f"visit_Await_rpar() raised an exception {e} unexpectedly!")
        # Act & Assert for LeftParen node
        try:
            visit_Await_rpar(leftParen_node)
        except Exception as e:
            pytest.fail(f"visit_Await_rpar() raised an exception {e} unexpectedly!")

    @pytest.mark.negative
    def test_visit_Await_rpar_without_node(self):
        # Act & Assert
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'node'"):
            visit_Await_rpar()  # This function call should raise a TypeError
