import pytest
import sys
from io import StringIO
from tool import _invalid_command

def mock_parser():
    class MockParser:
        def print_help(self, stream=None):
            print("Mock Help Message", file=stream)
    return MockParser()

@pytest.fixture(autouse=True)
def patch_parser(monkeypatch):
    monkeypatch.setattr('tool.parser', mock_parser())

class Test_ToolInvalidCommand:

    def test_invalid_command_no_proc_and_no_arg(self):
        # Arrange
        proc_name = ""
        command_args = []
        expected_output = "Please specify a command!\nMock Help Message\n"
        sys.stderr = StringIO()

        # Act
        result = _invalid_command(proc_name, command_args)

        # Assert
        assert result == 1
        assert sys.stderr.getvalue() == expected_output

    def test_invalid_command_with_proc_no_arg(self):
        # Arrange
        proc_name = "TestProc"
        command_args = []
        expected_output = "Please specify a command!\nMock Help Message\n"
        sys.stderr = StringIO()

        # Act
        result = _invalid_command(proc_name, command_args)

        # Assert
        assert result == 1
        assert sys.stderr.getvalue() == expected_output

    def test_invalid_command_with_proc_and_arg(self):
        # Arrange
        proc_name = "TestProc"
        command_args = ["arg1", "arg2"]
        expected_output = "Please specify a command!\nMock Help Message\n"
        sys.stderr = StringIO()

        # Act
        result = _invalid_command(proc_name, command_args)

        # Assert
        assert result == 1
        assert sys.stderr.getvalue() == expected_output
