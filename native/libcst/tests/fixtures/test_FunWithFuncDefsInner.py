import pytest
import asyncio
from fun_with_func_defs import inner

class Test_FunWithFuncDefsInner:

    @pytest.mark.asyncio
    def test_function_completion(self):
        async def successfully_ending_coroutine():
            await asyncio.sleep(1)
            return "success"

        assert asyncio.run(inner(successfully_ending_coroutine())) == "success"

    @pytest.mark.asyncio
    def test_function_exception(self):
        async def exception_raising_coroutine():
            raise ValueError("Some error")

        with pytest.raises(ValueError):
            asyncio.run(inner(exception_raising_coroutine()))

    @pytest.mark.asyncio
    def test_function_without_Lol(self):
        with pytest.raises(TypeError):
            asyncio.run(inner())

    @pytest.mark.asyncio
    def test_function_long_execution(self):
        async def long_running_coroutine():
            await asyncio.sleep(5)
            return "success"

        with pytest.raises(asyncio.TimeoutError):
            asyncio.run(inner(long_running_coroutine()), timeout=2)
