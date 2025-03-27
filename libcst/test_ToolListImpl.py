import argparse
import importlib
import inspect
import pytest
from typing import List
from unittest.mock import patch, call
from tool import _list_impl

class Test_ToolListImpl:
    @patch('tool._find_and_load_config')
    @patch('tool._recursive_find')
    def test_list_impl_valid_codemods(self, mock_recursive_find, mock_config):
        mock_config.return_value = {"modules":["valid_module"]}
        mock_recursive_find.return_value = [("valid_module.valid_file", "valid_module")] 
        mock_codemod = type("MockCodemod", (object,), {"DESCRIPTION": ""})

        with patch('valid_module.valid_file', new=mock_codemod):
            assert _list_impl('proc_name', []) == 0

    @patch('tool._find_and_load_config')
    def test_list_impl_invalid_module(self, mock_config):
        mock_config.return_value = {"modules":["invalid_module"]}
        with pytest.raises(ImportError):
            _list_impl('proc_name', [])

    @patch('tool._find_and_load_config')
    @patch('tool._recursive_find')
    def test_list_impl_abstract_codemods(self, mock_recursive_find, mock_config):
        mock_config.return_value = {"modules":["valid_module"]}
        mock_recursive_find.return_value = [("valid_module.valid_file", "valid_module")] 
        
        class AbstractCodemod(object):
            def __init__(self):
                self.DESCRIPTION = ""

        mock_codemod = type("MockCodemod", (AbstractCodemod,), {"DESCRIPTION": ""})

        with patch('valid_module.valid_file', new=mock_codemod):
            assert _list_impl('proc_name', []) == 0

    @patch('tool._find_and_load_config')
    @patch('tool._recursive_find')
    def test_list_impl_duplicate_codemods(self, mock_recursive_find, mock_config):
        mock_config.return_value = {"modules":["valid_module1", "valid_module2"]}
        mock_recursive_find.return_value = [("valid_module1.valid_file", "valid_module1"), ("valid_module2.valid_file", "valid_module2")] 
        mock_codemod = type("MockCodemod", (object,), {"DESCRIPTION": ""})

        with patch('valid_module1.valid_file', new=mock_codemod), patch('valid_module2.valid_file', new=mock_codemod):
            assert _list_impl('proc_name', []) == 0
 