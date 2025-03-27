import pytest
from libcst._nodes.op import Add
from libcst._typed_visitor_base import mark_no_op
from _typed_visitor import visit_Add_whitespace_after

class Test_CstTypedBaseFunctionsVisitAddWhitespaceAfter:

    @pytest.mark.smoke
    def test_visit_Add_whitespace_after_return_behavior(self):
        # Arrange
        add_node = Add()
        
        # Act
        result = visit_Add_whitespace_after(add_node)

        # Assert
        assert result is None, "Function should return None."

    @pytest.mark.regression
    def test_argument_functionality(self):
        # Arrange
        add_node = Add()
        
        # Act
        exception = False
        try:
            visit_Add_whitespace_after(add_node)
        except Exception:
            exception = True
            
        # Assert
        assert exception is False, "Function should not raise an exception."

    @pytest.mark.negative
    def test_non_add_argument_acceptance(self):
        # Arrange
        non_add_argument = 5
        
        # Act & Assert
        with pytest.raises(TypeError):
            visit_Add_whitespace_after(non_add_argument)
