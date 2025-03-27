import pytest
from _exceptions import get_expected_str
from libcst._parser.parso.python.token import PythonTokenTypes
from libcst._parser.types.token import Token, EOFSentinel

class Test_ExceptionsGetExpectedStr:

    @pytest.mark.parametrize("single_token", ['EOF'])
    def test_get_expected_str_with_single_token(self, single_token):
        encountered = EOFSentinel()
        expected = EOFSentinel()
        actual = get_expected_str(encountered, expected)
        expected_output = "Encountered EOF, but expected EOF."
        assert expected_output == actual, f"For test input {single_token}, Expected: {expected_output} but got: {actual}"

    @pytest.mark.parametrize("multiple_tokens", ['INDENT', 'ENDMARKER', 'EOF'])
    def test_get_expected_str_with_indent_token_and_multiple_expected(self, multiple_tokens):
        token = PythonTokenTypes[multiple_tokens]
        encountered = Token(type=token, string='  ')
        expected = [PythonTokenTypes.ENDMARKER, PythonTokenTypes.INDENT, PythonTokenTypes.EOF]
        actual = get_expected_str(encountered, expected)
        assert actual, f"For test input {multiple_tokens}, Expected some output but got: {actual}"

    @pytest.mark.parametrize("large_expected_tokens", ['NAME'])
    def test_get_expected_str_with_regular_token_and_large_expected_list(self, large_expected_tokens):
        token = PythonTokenTypes[large_expected_tokens]
        encountered = Token(type=token, string='name_of_token')
        expected = [PythonTokenTypes[type] for type in dir(PythonTokenTypes) if not type.startswith('_')] * 2 # Duplicate the list to ensure it has more than 10 elements
        actual = get_expected_str(encountered, expected)
        expected_output = "Unexpectedly encountered 'name_of_token'."
        assert expected_output == actual, f"For test input {large_expected_tokens}, Expected: {expected_output} but got: {actual}"

    @pytest.mark.parametrize("non_special_token", ['NAME'])
    def test_get_expected_str_with_single_non_special_token(self, non_special_token):
        token = PythonTokenTypes[non_special_token]
        encountered = Token(type=token, string='name_of_token')
        expected = token
        actual = get_expected_str(encountered, [expected])
        expected_output = "Encountered 'name_of_token', but expected 'NAME'."
        assert expected_output == actual, f"For test input {non_special_token}, Expected: {expected_output} but got: {actual}"
