import pytest
from _exceptions import ParserSyntaxError

class Test_ParserSyntaxErrorRepr:

    def test_repr_includes_all_attributes(self):
        # Arrange
        error_instance = ParserSyntaxError(message="Some error", lines=["line1", "line2"], raw_line=10, raw_column=20)
        
        # Act
        repr_result = error_instance.__repr__()
        
        # Assert
        assert "Some error" in repr_result
        assert "raw_line=10" in repr_result
        assert "raw_column=20" in repr_result

    def test_repr_with_missing_attributes(self):
        # Arrange
        error_instance = ParserSyntaxError(message="Some error")
        
        # Act
        repr_result = error_instance.__repr__()
        
        # Assert
        assert "Some error" in repr_result
        assert "raw_line" not in repr_result
        assert "raw_column" not in repr_result

    def test_repr_all_attributes_none(self):
        # Arrange
        error_instance = ParserSyntaxError(message=None, lines=None, raw_line=None, raw_column=None)
        
        # Act
        repr_result = error_instance.__repr__()
        
        # Assert
        assert "None" in repr_result
        assert "raw_line=None" in repr_result
        assert "raw_column=None" in repr_result
