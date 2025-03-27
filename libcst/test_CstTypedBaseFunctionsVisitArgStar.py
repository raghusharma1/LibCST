import pytest
from _typed_visitor import visit_Arg_star
from libcst._nodes.expression import Arg

class Test_CstTypedBaseFunctionsVisitArgStar:
    
    @pytest.mark.smoke
    def test_visit_Arg_star_no_op(self):
        # Arrange
        arg_object = Arg(value="Initial Value")

        # Act
        visit_Arg_star(arg_object)

        # Assert
        assert arg_object.value == "Initial Value", "The Arg object was modified"

    @pytest.mark.negative
    def test_visit_Arg_star_None_input(self):
        # Act and Assert
        try:
            visit_Arg_star(None)
        except Exception as e:
            pytest.fail(f"visit_Arg_star failed with None input: {e}")

    @pytest.mark.valid
    def test_visit_Arg_star_Immutable(self):
        # Arrange
        arg_object = Arg(value="Immutable Value")
        initial_value = arg_object.value

        # Act
        visit_Arg_star(arg_object)
        final_value = arg_object.value

        # Assert
        assert initial_value == final_value, "The Arg object was modified"

    @pytest.mark.regression
    @pytest.mark.parametrize("arg_input", ["value1", "value2", "value3"])
    def test_visit_Arg_star_with_diff_Arg_inputs(self, arg_input):
        # Arrange
        arg_object = Arg(value=arg_input)

        # Act
        visit_Arg_star(arg_object)
        
        # Assert
        assert arg_object.value == arg_input, "The Arg object was modified"
