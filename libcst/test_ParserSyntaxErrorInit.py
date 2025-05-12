import pytest
from _exceptions import ParserSyntaxError

class Test_ParserSyntaxErrorInit:
    @pytest.mark.positive
    def test_parser_syntax_error_instantiation_with_valid_parameters(self):
        # Arrange
        message = "Test Message"
        lines = ["Test", "Lines"]
        raw_line = 10
        raw_column = 20

        # Act
        parser_syntax_error = ParserSyntaxError(message, lines=lines, raw_line=raw_line, raw_column=raw_column)

        # Assert
        assert parser_syntax_error.message == message
        assert parser_syntax_error._lines == lines
        assert parser_syntax_error.raw_line == raw_line
        assert parser_syntax_error.raw_column == raw_column

    @pytest.mark.negative
    def test_parser_syntax_error_instantiation_with_incorrect_parameters(self):
        # Arrange
        message = 100
        lines = "Invalid lines data"
        raw_line = "Invalid raw_line data"
        raw_column = "Invalid raw_column data"

        # Assert
        with pytest.raises(TypeError):
            # Act - Attempt to create an instance with invalid data should raise a TypeError
            ParserSyntaxError(message, lines=lines, raw_line=raw_line, raw_column=raw_column)

    @pytest.mark.positive
    def test_parser_syntax_error_instance_comparison(self):
        # Arrange
        parser_syntax_error_1 = ParserSyntaxError("Message 1", lines=["Line 1"], raw_line=10, raw_column=20)
        parser_syntax_error_2 = ParserSyntaxError("Message 2", lines=["Line 2"], raw_line=30, raw_column=40)
        
        # Act (no physically act here as we are comparing instances)
        # Assert
        assert parser_syntax_error_1 != parser_syntax_error_2
