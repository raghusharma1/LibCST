import inspect
from abc import ABC
from contextlib import contextmanager
from typing import Callable, cast, ClassVar, Collection, Generic, Iterator, Mapping, Type, TYPE_CHECKING, TypeVar, Union
from libcst._nodes.base import CSTNode
from libcst.metadata.base_provider import BaseMetadataProvider, ProviderT
from libcst.metadata.wrapper import MetadataWrapper
import pytest
from _metadata_dependent import __init__

class Test_LazyValueInit:

    def test_default_provider_init_valid_callable(self):
        def test_func():
            return "valid"
        
        provider = __init__(test_func)
        assert provider.callable == test_func
        assert provider.return_value == "valid"

    def test_default_provider_init_invalid_callable(self):
        test_var = "this is not callable"
        with pytest.raises(TypeError):
            provider = __init__(test_var)

    def test_default_provider_init_callable_with_params(self):
        def test_func_with_params(param):
            return param

        with pytest.raises(TypeError):
            provider = __init__(test_func_with_params)

    def test_default_provider_init_callable_no_return(self):
        def test_func_no_return():
            pass

        provider = __init__(test_func_no_return)
        assert provider.return_value == None

    def test_default_provider_init_callable_optional_param(self):
        def test_func_optional_param(param="optional"):
            return param

        provider = __init__(test_func_optional_param)
        assert provider.callable == test_func_optional_param
        assert provider.return_value == "optional"

