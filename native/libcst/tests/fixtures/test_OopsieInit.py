import pytest
from class_craziness import OOPSIE, Bar

class Test_OopsieInit:

    @pytest.mark.regression
    def test_class_initialization(self):
        oopsie = OOPSIE()
        assert isinstance(oopsie.foo, Bar), "Foo attribute is not an instance of Bar"

    @pytest.mark.valid
    def test_class_attributes(self):
        oopsie = OOPSIE()

        # // TODO : Add necessary operations on oopsie.foo according to the Bar class
        oopsie.foo.some_bar_method()

        # // TODO : Verify the operations produce expected results
        assert oopsie.foo.some_result == "expected result", "Foo attribute does not behave as expected"

    @pytest.mark.valid
    def test_default_attribute_value(self):
        oopsie = OOPSIE()

        # Assert to check if the foo attribute is initialized with an instance of Bar
        assert isinstance(oopsie.foo, Bar), "Foo attribute is not initialized with an instance of Bar"

    @pytest.mark.valid
    def test_override_default_attribute_value(self):
        oopsie = OOPSIE()

        # // TODO : Replace `new_value` with a valid value compatible with foo attribute
        new_value = Bar(new_attr = "new value")
        oopsie.foo = new_value

        assert oopsie.foo == new_value, "Foo attribute value is not overridden"
