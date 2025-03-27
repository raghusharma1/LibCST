import pytest
from libcst._nodes.expression import Attribute
from _typed_visitor import visit_Attribute_value

class Test_CstTypedBaseFunctionsVisitAttributeValue:

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.performance
    @pytest.mark.valid
    def test_visit_Attribute_value_with_dot(self):
        # Arrange
        attribute_with_dot = Attribute("Hello.World")

        # Act
        try:
            visit_Attribute_value(attribute_with_dot)

        # Assert
        except Exception as error:
            pytest.fail(f'visit_Attribute_value method failed with error: {error}')

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.performance
    @pytest.mark.valid
    def test_visit_Attribute_value_with_instance_variable(self):
        # Arrange
        instance_variable = Attribute("self.attr")

        # Act
        try:
            visit_Attribute_value(instance_variable)

        # Assert
        except Exception as error:
            pytest.fail(f'visit_Attribute_value method failed with error: {error}')


    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.performance
    @pytest.mark.valid
    def test_visit_Attribute_value_with_number(self):
        # Arrange
        attribute_with_number = Attribute("attr1")

        # Act
        try:
            visit_Attribute_value(attribute_with_number)

        # Assert
        except Exception as error:
            pytest.fail(f'visit_Attribute_value method failed with error: {error}')


    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.performance
    @pytest.mark.valid
    def test_visit_Attribute_value_with_empty_attribute(self):
        # Arrange
        empty_attribute = Attribute()

        # Act
        try:
            visit_Attribute_value(empty_attribute)

        # Assert
        except Exception as error:
            pytest.fail(f'visit_Attribute_value method failed with error: {error}')
