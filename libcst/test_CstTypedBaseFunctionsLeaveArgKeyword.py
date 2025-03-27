import pytest
from _typed_visitor import leave_Arg_keyword
from libcst._nodes.expression import Arg


class Test_CstTypedBaseFunctionsLeaveArgKeyword: 
    @pytest.mark.smoke 
    def test_no_Args_provided(self):
        # Arrange
        instance = CSTTypedBaseFunctions()
        # Act
        # this will cause an error if any unexpected arguments are passed
        result = instance.leave_Arg_keyword()
        # Assert
        assert result is None
    
    @pytest.mark.regression
    def test_multiple_Args_provided(self):
        # Arrange
        instance = CSTTypedBaseFunctions()
        arg1 = Arg('arg1')
        arg2 = Arg('arg2')
        # Act
        instance.leave_Arg_keyword(arg1)
        instance.leave_Arg_keyword(arg2)
        # Assert
        # since the function doesn't have a return statement
        # we are just asserting that no error was raised
        assert True  
    
    @pytest.mark.regression 
    def test_special_character_Args(self):
        # Arrange
        instance = CSTTypedBaseFunctions()
        special_arg = Arg('@#$')
        # Act
        instance.leave_Arg_keyword(special_arg)
        # Assert
        # since the function doesn't have a return statement
        # we are just asserting that no error was raised
        assert True
    
    @pytest.mark.regression 
    def test_keyword_Arg(self):
        # Arrange
        instance = CSTTypedBaseFunctions()
        keyword_arg = Arg('class')
        # Act
        instance.leave_Arg_keyword(keyword_arg)
        # Assert
        # since the function doesn't have a return statement
        # we are just asserting that no error was raised
        assert True
