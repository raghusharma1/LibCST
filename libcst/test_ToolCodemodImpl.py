import pytest
import argparse
from unittest.mock import call, patch, mock_open
import sys
from tool import _codemod_impl
import os


def test_command_class_loading():
    # Prepare the test command class
    class TestCommand:
        pass

    config_mock = {
        "modules": ["test_module_1", "test_module_2", "test_module_3"],
        "other_config_data": "Sample data"
    }
    with patch.object(sys, "modules", {
        "test_module_1.test_command": TestCommand,
    }), patch.object(sys, 'stderr', new=mock_open()) as m:
        assert _codemod_impl("test_codemod_tool", ["test_command"]) == 0
        m.assert_not_called()


def test_command_class_loading_from_external():
    # Prepare the test command class
    class TestCommand:
        pass

    with patch.object(sys, "modules", {
        "test_module.test_command": TestCommand,
    }), patch.object(sys, 'stderr', new=mock_open()) as m:
        assert _codemod_impl("test_codemod_tool", ["-x", "TestCommand"]) == 0
        m.assert_not_called()


def test_codemod_transformation_on_files():
    class TestCommand:
        pass

    test_files = ["test_file_1.py", "test_file_2.py", "test_file_3.py"]
    
    with patch.object(sys, 'stderr', new=mock_open()) as m_stder, \
         patch('tool.gather_files', return_value=test_files) as m_gather_files, \
         patch('tool.parallel_exec_transform_with_prettyprint', return_value={'successes': 3, 'failures': 3}) as m_transform:
        assert _codemod_impl("test_codemod_tool", ["TestCommand", *test_files]) == 0
        m_gather_files.assert_called_once_with(test_files, include_stubs=False)
        m_transform.assert_called_once()
        m_stder.assert_not_called()


def test_codemod_transformation_interrupt_handling():
    class TestCommand:
        pass

    with patch.object(sys, 'stderr', new=mock_open()) as m_stder, \
         patch('tool.gather_files', return_value=['test_file.py']) as m_gather_files, \
         patch('tool.parallel_exec_transform_with_prettyprint', side_effect=KeyboardInterrupt()) as m_transform:
        assert _codemod_impl("test_codemod_tool", ["TestCommand", 'test_file.py', '-p', '3.6']) == 2
        m_gather_files.assert_called_once_with(['test_file.py'], include_stubs=False)
        m_transform.assert_called_once()
        m_stder.assert_called()
