import pytest
from _exceptions import PartialParserSyntaxError

class Test_PartialParserSyntaxErrorInit:
    def test_init_with_string_msg(self):
        # Setup
        test_message = "This is a test message"

        # Execute
        test_exception = PartialParserSyntaxError(test_message)

        # Assert
        assert test_exception.message == test_message, "Test with normal string message failed."

    @pytest.mark.negative
    def test_init_with_empty_string_msg(self):
        # Setup
        test_message = ""

        # Execute
        test_exception = PartialParserSyntaxError(test_message)

        # Assert
        assert test_exception.message == test_message, "Test with empty string message failed."

    @pytest.mark.negative
    def test_init_with_non_string_input(self):
        # Setup
        test_message = 123456

        # Assert
        with pytest.raises(TypeError):
            # Execute
            test_exception = PartialParserSyntaxError(test_message)

    @pytest.mark.negative
    def test_init_with_null_input(self):
        # Setup
        test_message = None

        # Assert
        with pytest.raises(TypeError):
            # Execute
            test_exception = PartialParserSyntaxError(test_message)
