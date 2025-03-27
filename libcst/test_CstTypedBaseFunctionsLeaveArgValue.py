import pytest
from _typed_visitor import leave_Arg_value
from libcst._nodes.expression import Arg

# Creating a custom object for testing
class CustomObject:
    def __init__(self):
        self.value = "I'm a custom object"

class Test_CstTypedBaseFunctionsLeaveArgValue:

    def test_leave_Arg_value_none(self):
        try:
            leave_Arg_value(None)
        except Exception as e:
            pytest.fail(f"Test failed with error: {str(e)}")

    def test_leave_Arg_value_arg_object(self):
        test_arg = Arg(
            whitespace_after_equal=SimpleWhitespace(value=" "),
            keyword=Name(value="test"),
            equal=MaybeSentinel.DEFAULT,
            value=SimpleString(value="test_value"),
        )
        
        try:
            leave_Arg_value(test_arg)
        except Exception as e:
            pytest.fail(f"Test failed with error: {str(e)}")

    def test_leave_Arg_value_custom_object(self):
        custom_obj = CustomObject()

        try:
            leave_Arg_value(custom_obj)
        except Exception as e:
            pytest.fail(f"Test failed with error: {str(e)}")

    def test_leave_Arg_value_multiple_arg_objects(self):
        args_list = [
            Arg(
                whitespace_after_equal=SimpleWhitespace(value=" "),
                keyword=Name(value="test1"),
                equal=MaybeSentinel.DEFAULT,
                value=SimpleString(value="test_value1"),
            ),
            Arg(
                whitespace_after_equal=SimpleWhitespace(value=" "),
                keyword=Name(value="test2"),
                equal=MaybeSentinel.DEFAULT,
                value=SimpleString(value="test_value2"),
            ),
        ]

        for arg_obj in args_list:
            try:
                leave_Arg_value(arg_obj)
            except Exception as e:
                pytest.fail(f"Test failed with error: {str(e)}")
