import pytest
from libcst._nodes.expression import Arg
from _typed_visitor import leave_Arg_whitespace_after_arg

class Test_CstTypedBaseFunctionsLeaveArgWhitespaceAfterArg:
    
    @pytest.mark.regression
    def test_leave_Arg_whitespace_after_arg_no_modification(self):
        # Arrange
        arg_object = Arg()
        initial_representation = repr(arg_object)
        
        # Act
        leave_Arg_whitespace_after_arg(arg_object)
        
        # Assert
        assert repr(arg_object) == initial_representation, "The function has modified the 'Arg' object"

    @pytest.mark.negative
    def test_leave_Arg_whitespace_after_arg_accepts_only_Arg(self):
        # Arrange
        bool_object = True

        # Act and Assert
        with pytest.raises(TypeError):
            leave_Arg_whitespace_after_arg(bool_object)

    @pytest.mark.valid
    def test_leave_Arg_whitespace_after_arg_no_return_value(self):
        # Arrange
        arg_object = Arg()

        # Act
        result = leave_Arg_whitespace_after_arg(arg_object)
        
        # Assert
        assert result is None, "The function is returning a value while it should not"
