import pytest
from _exceptions import ParserSyntaxError

class Test_ParserSyntaxErrorStr:
    @pytest.mark.regular
    def test_str_with_context(self):
        error = ParserSyntaxError("This is a syntax error.", lines=[], raw_line=2, raw_column=2)
        expected_output = "Syntax Error @ 2:2.\nThis is a syntax error.\n\n[]"
        assert str(error) == expected_output

    @pytest.mark.regular
    def test_str_without_context(self):
        error = ParserSyntaxError("Another syntax error.")
        expected_output = "Syntax Error @ 2:2.\nAnother syntax error."
        assert str(error) == expected_output

    @pytest.mark.regular
    def test_str_with_error_inputs(self):
        error_messages = ["Error1", "Error2", "Error3"]
        for message in error_messages:
            error = ParserSyntaxError(message)
            assert message in str(error)

    @pytest.mark.regional
    def test_str_line_and_column(self):
        lines_and_columns = [(1,1), (2,2), (3,3)]
        for line, column in lines_and_columns:
            error = ParserSyntaxError("Syntax Error", lines=[""], raw_line=line, raw_column=column)
            expected_output = f"Syntax Error @ {line}:{column}.\nSyntax Error\n\n['']"
            assert str(error) == expected_output
