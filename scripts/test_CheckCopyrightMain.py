import pytest
import re
import sys
from pathlib import Path
from subprocess import run
from typing import Iterable, List, Pattern
from check_copyright import main

class Test_CheckCopyrightMain:

    @pytest.mark.parametrize("files, expected", [
        (["file1.txt", "file2.txt", "file3.txt"], 0),
    ])
    def test_files_with_expected_headers(self, files, expected):
        for file in files:
            path = Path(file)
            path.write_text(EXPECTED_HEADER)
        assert main() == expected

    @pytest.mark.parametrize("files_with_header, files_without_header, expected", [
        (["file1.txt", "file2.txt"], ["file3.txt", "file4.txt"], 1),
    ])
    def test_files_without_expected_headers(self, files_with_header, files_without_header, expected):
        for file in files_with_header + files_without_header:
            path = Path(file)
            if file in files_with_header:
                path.write_text(EXPECTED_HEADER)
            else:
                path.write_text("This is not the header")
        assert main() == expected       

    @pytest.mark.parametrize("files, expected", [
        (["empty1.txt", "empty2.txt", "empty3.txt"], 1),
    ])
    def test_empty_files(self, files, expected):
        for file in files:
            path = Path(file)
            path.write_text('')
        assert main() == expected

    @pytest.mark.skip(reason="These type of tests require a performance testing approach")
    @pytest.mark.parametrize("files, expected", [
        (["file1.txt", "file2.txt", "file3.txt"], 0),
    ])
    def test_large_number_files(self, files, expected):
        for i in range(10000):
            file = "file" + str(i) + ".txt"
            files.append(file)
        for file in files:
            path = Path(file)
            path.write_text(EXPECTED_HEADER)
        assert main() == expected

    @pytest.mark.parametrize("expected", [
        (0),
    ])
    def test_no_tracked_files(self, expected):
        assert main() == expected
