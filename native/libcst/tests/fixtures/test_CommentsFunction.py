import pytest
from unittest.mock import patch, Mock
import os.path
import sys
import a
from b.c.d.e import X
import fast
import inner_imports
import slow as fast

class Test_CommentsFunction:
    
    @pytest.mark.regression
    @patch('inner_imports.are_evil', return_value=True)
    @patch('b.c.d.e.X.method1', return_value='evil_method_called')
    def test_function_evil_imports(self, mock_method, mock_imports):
        from comments import function
        assert function() == 'evil_method_called'

    @pytest.mark.regression
    @patch('inner_imports.are_evil', return_value=False)
    def test_function_not_evil_import(self, mock_imports):
        from comments import function
        assert function('default_value') == 'default_value'
        

    @pytest.mark.regression
    @patch('inner_imports.are_evil', return_value=False)
    def test_function_no_default(self, mock_imports):
        from comments import function
        assert function() == None
