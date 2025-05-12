import pytest
from _exceptions import ParserSyntaxError


class Test_ParserSyntaxErrorEditorLine:

    def test_editor_line_consistent(self):
        # Arrange
        raw_line_test = 3
        pse = ParserSyntaxError('Test Message', lines=['TestLine1', 'TestLine2'], raw_line=raw_line_test, raw_column=1)

        # Act
        editor_line_result = pse.editor_line()

        # Assert
        assert editor_line_result == raw_line_test

    @pytest.mark.parametrize('raw_line_test', [(1), (2), (3)])
    def test_editor_line_one_indexed(self, raw_line_test):
        # Arrange
        pse = ParserSyntaxError('Test Message', lines=['TestLine1', 'TestLine2'], raw_line=raw_line_test, raw_column=1)
        
        # Act
        editor_line_result = pse.editor_line()

        # Assert
        assert editor_line_result == raw_line_test
        assert isinstance(raw_line_test, int)
        assert raw_line_test >= 1  # validating one-indexed characteristic

    def test_editor_line_return_type_consistency(self):
        # Arrange
        raw_line_test = 3
        pse = ParserSyntaxError('Test Message', lines=['TestLine1', 'TestLine2'], raw_line=raw_line_test, raw_column=1)
        
        # Act
        editor_line_result = pse.editor_line()

        # Assert
        assert isinstance(editor_line_result, int)
