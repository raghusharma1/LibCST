import json
import os
from pathlib import Path
from subprocess import run
from libcst.metadata import TypeInferenceProvider
from unittest import mock
from unittest.mock import call
from regenerate_fixtures import main # assuming the method is in a module `regenerate_fixtures`
from typing import Any
import pytest

class MockPathObj(Path):
    def __init__(self, /, *args: StrArg):
        ...

    def with_suffix(self, suffix: str) -> 'Path':
        ...

    def write_text(self, data: StrPath, /, encoding=None, errors=None) -> int:
        ...

    def as_posix(self) -> str:
        ...

class Test_RegenerateFixturesMain:

    def test_function_main_normal_working(self, mocker):
        mocked_os = mocker.patch("os")
        mocked_run = mocker.patch("subprocess.run")
        mocked_chdir = mocker.patch("os.chdir")
        mocked_gen_cache = mocker.patch("libcst.metadata.TypeInferenceProvider.gen_cache")
        mocked_test_root = mocker.patch("pathlib.Path.glob")
        mocked_test_root.return_value = [MockPathObj('.py'), MockPathObj('.py')]

        main()

        calls = mocked_chdir.call_args_list

        assert calls == [call(mocked_test_root), call(mocked_os)]
        assert mocked_run.call_count == 2
        assert mocked_gen_cache.call_count == 2

    def test_function_main_failure_pyre_start(self, mocker):
        mocked_os = mocker.patch("os")
        mocked_run = mocker.patch("subprocess.run")
        mocked_run.side_effect = Exception('Mocked pyre start failure')
        mocked_chdir = mocker.patch("os.chdir")
        
        with pytest.raises(Exception):
            main()

        assert mocked_chdir.call_args_list == [call(mocked_os)]

    def test_function_main_no_python_file(self, mocker):
        mocked_os = mocker.patch("os")
        mocked_run = mocker.patch("subprocess.run")
        mocked_chdir = mocker.patch("os.chdir")
        mocked_test_root = mocker.patch("pathlib.Path.glob")
        mocked_test_root.return_value = [] 

        main()

        assert mocked_chdir.call_args_list == [call(mocked_test_root), call(mocked_os)]
        assert mocked_run.call_count == 2

    def test_function_main_json_file_generation_failure(self, mocker):
        mocked_os = mocker.patch("os")
        mocked_run = mocker.patch("subprocess.run")
        mocked_chdir = mocker.patch("os.chdir")
        mocked_gen_cache = mocker.patch("libcst.metadata.TypeInferenceProvider.gen_cache")
        mocked_gen_cache.side_effect = Exception('Mocked JSON generation failure')
        mocked_test_root = mocker.patch("pathlib.Path.glob")
        mocked_test_root.return_value = [MockPathObj('.py'), MockPathObj('.py')]

        with pytest.raises(Exception):
            main()

        calls = mocked_chdir.call_args_list

        assert calls == [call(mocked_test_root), call(mocked_os)]
        assert mocked_run.call_count == 1
