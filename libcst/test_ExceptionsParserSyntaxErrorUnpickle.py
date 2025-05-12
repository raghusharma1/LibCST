import pytest
from _exceptions import _parser_syntax_error_unpickle

class Test_ExceptionsParserSyntaxErrorUnpickle:
    @pytest.mark.valid
    def test_unpickle_with_valid_kwargs(self):
        kwargs = {
            "description": 'Syntax Error',
            "index": 10,
            "line": 5,
            # add more valid kwargs based on ParserSyntaxError attributes
        }
        output = _parser_syntax_error_unpickle(kwargs)
        assert isinstance(output, ParserSyntaxError)
        
    @pytest.mark.invalid
    def test_unpickle_with_missing_kwargs(self):
        kwargs = {
            "description": 'Syntax Error',
            # "index" attribute is missing
            "line": 5,
            # add or remove kwargs based ParserSyntaxError attributes
        }
        with pytest.raises(TypeError):
            _parser_syntax_error_unpickle(kwargs)

    @pytest.mark.valid
    def test_unpickle_with_extra_kwargs(self):
        kwargs = {
            "description": 'Syntax Error',
            "index": 10,
            "line": 5,
            "extra": "extra attribute",  # extra unwanted attribute
            # add or remove kwargs based ParserSyntaxError attributes
        }
        output = _parser_syntax_error_unpickle(kwargs)
        assert isinstance(output, ParserSyntaxError)
        assert not hasattr(output, "extra")

    @pytest.mark.invalid
    def test_unpickle_with_incorrect_data_types(self):
        kwargs = {
            "description": 'Syntax Error',
            "index": "incorrect data type",  # index supposed to be int
            "line": 5,
            # add or remove kwargs based ParserSyntaxError attributes
        }
        with pytest.raises(TypeError):
            _parser_syntax_error_unpickle(kwargs)
