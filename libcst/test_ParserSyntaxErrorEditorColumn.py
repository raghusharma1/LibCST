import pytest
from _exceptions import ParserSyntaxError
from _tabs import expand_tabs

class Test_ParserSyntaxErrorEditorColumn:

    @pytest.mark.smoke
    def test_editor_column_without_tabs(self):
        # Arrange
        parser_error = ParserSyntaxError("Test error", lines=["error at char 5"], raw_line=1, raw_column=5)
        expected_column = 6

        # Act
        actual_column = parser_error.editor_column()

        # Assert
        assert actual_column == expected_column, f"Expected column {expected_column} but got {actual_column}"

    @pytest.mark.regression
    def test_editor_column_with_tabs(self):
        # Arrange
        parser_error = ParserSyntaxError("Test error", lines=["\terror at\tchar 5"], raw_line=1, raw_column=10)
        expected_column = len(expand_tabs("\terror at\tchar 5")) + 1

        # Act
        actual_column = parser_error.editor_column()

        # Assert
        assert actual_column == expected_column, f"Expected column {expected_column} but got {actual_column}"

    @pytest.mark.positive
    def test_editor_column_with_empty_string(self):
        # Arrange
        parser_error = ParserSyntaxError("Test error", lines=[""], raw_line=1, raw_column=0)
        expected_column = 1

        # Act
        actual_column = parser_error.editor_column()

        # Assert
        assert actual_column == expected_column, f"Expected column {expected_column} but got {actual_column}"

    @pytest.mark.negative
    def test_editor_column_with_non_ASCII(self):
        # Arrange
        parser_error = ParserSyntaxError("Test error", lines=["あいうえ char 5"], raw_line=1, raw_column=10)
        expected_column = len(expand_tabs("あいうえ char 5"))

        # Act
        actual_column = parser_error.editor_column()

        # Assert
        assert actual_column == expected_column, f"Expected column {expected_column} but got {actual_column}"
