import pytest
from _typed_visitor import leave_Attribute_attr
from libcst._nodes.expression import Attribute

class Test_CstTypedBaseFunctionsLeaveAttributeAttr:

    @pytest.mark.positive
    def test_leave_Attribute_attr_called_with_proper_node(self):
        # Arrange: Initialize a proper node of type 'Attribute'.
        attribute_node = Attribute("<a random attribute>")

        # Act: Call the function 'leave_Attribute_attr' with the initialized node as the parameter.
        try:
            leave_Attribute_attr(attribute_node)
            # Assert: Check that the function successfully terminates without raising any exception.
        except Exception as e:
            pytest.fail(f"Unexpected Error occurred: {e}")

    @pytest.mark.negative
    def test_leave_Attribute_attr_called_with_improper_node(self):
        # Arrange: Initialize a node not of 'Attribute' type, for example an integer.
        integer_node = 123

        # Act: Invoke 'leave_Attribute_attr' function with this improper input
        with pytest.raises(TypeError):
            leave_Attribute_attr(integer_node)
        # Assert: An exception (like TypeError) is expected to be thrown, pytest.raises will verify it's thrown as expected.

    @pytest.mark.negative
    def test_leave_Attribute_attr_called_with_none_node(self):
        # Arrange: No arrangement needed as we're passing 'None' as input.

        # Act: Invoke function 'leave_Attribute_attr' without any input or with 'None'.
        with pytest.raises(TypeError):
            leave_Attribute_attr(None)
        # Assert: Depending on the design of the function, check if an TypeError is thrown as the function expects input.
