import pytest
from _typed_visitor import visit_Attribute_dot
from libcst._nodes.expression import Attribute
from libcst._nodes.module import Module
from libcst._nodes.whitespace import SimpleWhitespace

class Test_CstTypedBaseFunctionsVisitAttributeDot:

   def test_valid_attribute_instance_execution(self):
        # Arrange
        attribute = Attribute(
            value=Module(header=[], body=[], footer=[]),
            attr=SimpleWhitespace(value=" "),
            dot=SimpleWhitespace(value=".")
        )
        # Act & Assert
        try:
            visit_Attribute_dot(attribute)
        except Exception:
            pytest.fail("visit_Attribute_dot raised an exception unexpectedly!")

    def test_function_does_nothing(self):
        # Arrange
        attribute = Attribute(
            value=Module(header=[], body=[], footer=[]),
            attr=SimpleWhitespace(value=" "),
            dot=SimpleWhitespace(value=".")
        )

        attribute_copy = attribute.deep_clone()

        # Act
        visit_Attribute_dot(attribute)

        # Assert
        assert attribute_copy == attribute, "visit_Attribute should not mutate the passed object but it did!"

    def test_passing_non_attribute_instance(self):
        # Arrange
        non_attribute_instance = SimpleWhitespace(value=" ")

        # Act & Assert
        with pytest.raises(TypeError):
            visit_Attribute_dot(non_attribute_instance)
