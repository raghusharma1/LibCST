# pytest
import pytest
import argparse
import os
import yaml
from unittest import mock
from tool import _initialize_impl

@pytest.fixture
def init_arg_parser(request):
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    return parser.parse_args(request.param)

class Test_ToolInitializeImpl:
    @pytest.mark.parametrize('init_arg_parser',['./test_dir'], indirect=True)
    def test_initialize_impl_successful(self, init_arg_parser, monkeypatch, tmpdir):
        with monkeypatch.context() as m:
            m.setattr(yaml, 'safe_load', lambda x: 'dummy_config')
            m.setattr(os, 'path', tmpdir)
            open(tmpdir + '/.libcst.codemod.yaml', 'w').close()
            assert _initialize_impl('test', ['./test_dir']) == 0
            with open(tmpdir + '/.libcst.codemod.yaml', 'r') as f:
                assert f.readlines() == ['dummy_config']

    @pytest.mark.parametrize('init_arg_parser',['./test_dir'], indirect=True)
    def test_initialize_impl_serialize_validity(self, init_arg_parser, monkeypatch, tmpdir):
        with monkeypatch.context() as m:
            m.setattr(yaml, 'safe_load', lambda x: 'default_config')
            m.setattr(os, 'path', tmpdir)
            open(tmpdir + '/.libcst.codemod.yaml', 'w').close()
            _initialize_impl('test', ['./test_dir'])
            with open(tmpdir + '/.libcst.codemod.yaml', 'r') as f:
                file_content = f.readlines()
                yaml_content = yaml.safe_load(file_content)
                assert yaml_content == 'default_config'

    @pytest.mark.parametrize('init_arg_parser',['./test_dir'], indirect=True)
    def test_initialize_impl_invalid_serialization(self, init_arg_parser, monkeypatch, tmpdir):
        with monkeypatch.context() as m:
            m.setattr(yaml, 'safe_load', lambda x: 'invalid_config')
            m.setattr(os, 'path', tmpdir)
            open(tmpdir + '/.libcst.codemod.yaml', 'w').close()
            with pytest.raises(Exception) as excinfo:
                _initialize_impl('test', ['./test_dir'])
            assert str(excinfo.value) == 'Logic error, serialization is invalid!'

    @pytest.mark.parametrize('init_arg_parser',['./test_dir'], indirect=True)
    def test_initialize_impl_abs_path_configuration(self, init_arg_parser, monkeypatch, tmpdir):
        with monkeypatch.context() as m:
            m.setattr(yaml, 'safe_load', lambda x: 'default_config')
            m.setattr(os, 'path', tmpdir)
            open(tmpdir + '/.libcst.codemod.yaml', 'w').close()
            _initialize_impl('test', ['./test_dir'])
            assert os.path.isabs(tmpdir)
        
    @pytest.mark.parametrize('init_arg_parser',['./test_dir'], indirect=True)
    def test_initialize_impl_write_operation(self, init_arg_parser, monkeypatch, tmpdir):
        with monkeypatch.context() as m:
            m.setattr(yaml, 'safe_load', lambda x: 'write_test_config')
            m.setattr(os, 'path', tmpdir)
            open(tmpdir + '/.libcst.codemod.yaml', 'w').close()
            _initialize_impl('test', ['./test_dir'])
            with open(tmpdir + '/.libcst.codemod.yaml', 'r') as f:
                file_content = f.readlines()
                assert file_content == ['write_test_config']
