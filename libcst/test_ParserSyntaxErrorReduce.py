import pytest
from _exceptions import ParserSyntaxError
from typing import Sequence

class Test_ParserSyntaxErrorReduce:
    @pytest.mark.smoke
    @pytest.mark.positive
    @pytest.mark.regression
    def test_basic_reduction(self):
        # Arrange
        obj = ParserSyntaxError("TestMessage", lines = ["1", "2"], raw_line = 1, raw_column = 2)
        
        # Act
        result = obj.__reduce__()

        # Assert
        assert isinstance(result, tuple)
        assert len(result) == 2
        assert result[0].__name__ == "_parser_syntax_error_unpickle"
        assert result[1][0]["message"] == "TestMessage"
        assert result[1][0]["lines"] == ["1", "2"]
        assert result[1][0]["raw_line"] == 1
        assert result[1][0]["raw_column"] == 2

    @pytest.mark.smoke
    @pytest.mark.negative
    @pytest.mark.regression
    def test_no_lines_reduction(self):
        # Arrange
        obj = ParserSyntaxError("TestMessage", raw_line=1, raw_column=2)

        # Act
        result = obj.__reduce__()

        # Assert
        assert isinstance(result, tuple)
        assert len(result) == 2
        assert result[0].__name__ == "_parser_syntax_error_unpickle"
        assert result[1][0]["message"] == "TestMessage"
        assert result[1][0]["raw_line"] == 1
        assert result[1][0]["raw_column"] == 2

    @pytest.mark.smoke
    @pytest.mark.negative
    @pytest.mark.regression
    def test_empty_lines_reduction(self):
        # Arrange
        obj = ParserSyntaxError("TestMessage", lines=[], raw_line=1, raw_column=2)

        # Act
        result = obj.__reduce__()

        # Assert
        assert isinstance(result, tuple)
        assert len(result) == 2
        assert result[0].__name__ == "_parser_syntax_error_unpickle"
        assert result[1][0]["message"] == "TestMessage"
        assert result[1][0]["lines"] == []
        assert result[1][0]["raw_line"] == 1
        assert result[1][0]["raw_column"] == 2

    @pytest.mark.smoke
    @pytest.mark.negative
    @pytest.mark.regression
    def test_negative_values_reduction(self):
        # Arrange
        obj = ParserSyntaxError("TestMessage", lines = ["1", "2"], raw_line = -1, raw_column = -2)
        
        # Act
        result = obj.__reduce__()

        # Assert
        assert isinstance(result, tuple)
        assert len(result) == 2
        assert result[0].__name__ == "_parser_syntax_error_unpickle"
        assert result[1][0]["message"] == "TestMessage"
        assert result[1][0]["lines"] == ["1", "2"]
        assert result[1][0]["raw_line"] == -1
        assert result[1][0]["raw_column"] == -2
