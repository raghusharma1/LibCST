import pytest
from fun_with_func_defs import foo

class Test_FunWithFuncDefsFoo:

    @pytest.mark.positive
    def test_yield_sequence(self):
        bar_list = [1, 2, 3, 4, 5]
        result = []
        for i in foo(bar_list):
            result.append(i)
        assert result == bar_list

    @pytest.mark.positive
    def test_pause_resume_generator(self):
        bar_list = [1, 2, 3, 4, 5]
        generator = foo(bar_list)
        part_1 = [next(generator) for _ in range(3)]
        part_2 = [i for i in generator]
        result = part_1 + part_2
        assert result == bar_list

    @pytest.mark.negative
    def test_deplete_generator(self):
        bar_list = [1, 2, 3, 4, 5]
        generator = foo(bar_list)
        while True:
            try:
                next(generator)
            except StopIteration:
                break
        with pytest.raises(StopIteration):
            next(generator)
