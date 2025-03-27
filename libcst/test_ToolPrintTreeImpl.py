import pytest
import sys
import io
import os
from tool import _print_tree_impl

class Test_ToolPrintTreeImpl:

    @pytest.mark.smoke
    def test_python_version_argument_handling(self):
        python_test_file = "test_file.py"
        with open(python_test_file, 'w') as f:
            f.write("") # TODO: put some python 3.8 code here
        command_args = [python_test_file, "-p", "3.8"]
        assert _print_tree_impl("proc_test", command_args) == 0
        os.remove(python_test_file)

    @pytest.mark.regression
    def test_stdin_parsing(self, monkeypatch):
        code = 'print("Hello, World!")\n'
        monkeypatch.setattr('sys.stdin', io.StringIO(code))

        command_args = ['-']
        assert _print_tree_impl("proc_test", command_args) == 0

    @pytest.mark.regression
    def test_graphviz_format(self):
        python_test_file = "test_file.py"
        with open(python_test_file, 'w') as f:
            f.write("print('Hello, World!')\n")
        command_args = [python_test_file, "--graphviz"]
        assert _print_tree_impl("proc_test", command_args) == 0
        os.remove(python_test_file)

    @pytest.mark.negative
    def test_nonexisting_input_file_error_handling(self):
        command_args = ["nonexisting_file.py"]
        with pytest.raises(FileNotFoundError):
            _print_tree_impl("proc_test", command_args)

    @pytest.mark.negative
    def test_invalid_python_code_handling(self):
        python_test_file = "test_file.py"
        with open(python_test_file, 'w') as f:
            f.write("invalid python code")
        command_args = [python_test_file]
        with pytest.raises(Exception):
            _print_tree_impl("proc_test", command_args)
        os.remove(python_test_file)
