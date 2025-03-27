import pytest
from libcst import Attribute
from _typed_visitor import leave_Attribute_value

class Test_CstTypedBaseFunctionsLeaveAttributeValue():

    @pytest.mark.smoke
    def test_leave_Attribute_value_do_nothing(self):
        test_node = Attribute('Test_Node')
        before_calling_function = test_node.__dict__
        leave_Attribute_value(test_node)
        after_calling_function = test_node.__dict__
        assert before_calling_function == after_calling_function, "The function modified the Attribute node"

    @pytest.mark.regression
    @pytest.mark.parametrize("test_input", [
        (1234),
        ('abcd'),
        (1.748),
        (True),
        (['test', 'array']),
        (('test', 'tuple')),
        ({'key': 'value'}),
    ])
    def test_leave_Attribute_value_with_different_objects(self, test_input):
        original_object = test_input
        leave_Attribute_value(test_input)
        assert original_object == test_input, "The function modified the original object"

    @pytest.mark.negative
    def test_leave_Attribute_value_with_None(self):
        test_input = None
        try:
            leave_Attribute_value(test_input)
        except Exception as e:
            pytest.fail(f"The function threw an exception: {e}")
