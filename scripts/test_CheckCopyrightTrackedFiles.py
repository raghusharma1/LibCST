import pytest
import re
import sys
from pathlib import Path
from subprocess import run, CalledProcessError
from typing import Iterable, List, Pattern
from unittest.mock import patch, Mock

# Importing the module
from check_copyright import tracked_files

class Test_CheckCopyrightTrackedFiles:
    
    @pytest.mark.regression
    def test_tracked_files_empty_repository(self):
        with patch.object(Path, 'is_file', return_value=False):
            assert list(tracked_files()) == []

    @pytest.mark.regression
    def test_tracked_files_various_extensions(self):
        with patch('subprocess.run') as mocked_run:
            mocked_run.return_value.stdout='test_file.py\ntest_file1.sh\ntest_file2.txt\ntest_file3.md'
            assert list(tracked_files()) == ['test_file.py', 'test_file1.sh']

    @pytest.mark.regression
    def test_tracked_files_with_exception_patterns(self):
        with patch('subprocess.run') as mocked_run:
            mocked_run.return_value.stdout = '^native/libcst/tests/fixtures/test_file1.py\n^libcst/_add_slots\\.pytest\n'
            assert list(tracked_files()) == []

    @pytest.mark.regression
    def test_tracked_files_non_existent_paths(self):
        with patch.object(Path, 'is_file', return_value=False):
            assert list(tracked_files()) == []

    @pytest.mark.regression
    def test_tracked_files_git_error(self):
        with patch('subprocess.run', side_effect=CalledProcessError(1, cmd=[])):   
            with pytest.raises(CalledProcessError):
                list(tracked_files())
