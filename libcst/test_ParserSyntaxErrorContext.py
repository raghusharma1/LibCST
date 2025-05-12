import pytest
from _exceptions import ParserSyntaxError
from libcst._tabs import expand_tabs

@pytest.mark.regression
def test_context_for_non_empty_line_after():
    parser_err = ParserSyntaxError(
        message='Syntax Error occurred',
        lines=['print("Hello")', '', '1print'], 
        raw_line=3,
        raw_column=1
    )
    
    assert parser_err.context() == f'{expand_tabs(parser_err._lines[0])}\n^'
    

@pytest.mark.regression
def test_context_for_blank_file():
    parser_err = ParserSyntaxError(
        message='Syntax Error occurred',
        lines=['', '', ''], 
        raw_line=3,
        raw_column=1
    )

    assert parser_err.context() == None
    
    
@pytest.mark.regression
def test_context_for_non_empty_line_on_error_line():
    parser_err = ParserSyntaxError(
        message='Syntax Error occurred',
        lines=['print("Hello")', '1print'], 
        raw_line=2,
        raw_column=1
    )
    
    assert parser_err.context() == f'{expand_tabs(parser_err._lines[1])}\n^'
