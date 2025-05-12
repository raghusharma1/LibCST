import pytest
from smol_statements import f

class Test_SmolStatementsF:
    
    def test_assertion_with_valid_params(self):
        a_initial = 5
        result = f(True, 'bar', a_initial)
        assert result == a_initial + 2

    def test_assertion_with_invalid_params(self):
        with pytest.raises(AssertionError):
            f(False, '', 1)
            
    def test_increment_return(self):
        a_initial = 0
        result = f('foo', 'bar', a_initial)
        assert result == a_initial + 2
