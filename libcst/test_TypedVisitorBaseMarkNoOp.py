import pytest
from typing import Any, Callable, cast, TypeVar
from _typed_visitor_base import mark_no_op

F = TypeVar('F', bound=Callable)

class Test_TypedVisitorBaseMarkNoOp:

    @pytest.mark.smoke
    def test_mark_no_op_verification(self):
        def sample_func():
            return "I am a simple function."

        marked_func = mark_no_op(sample_func)

        assert getattr(marked_func, "_is_no_op") == True, "The function wasn't marked as no-op."

    @pytest.mark.regression
    def test_mark_no_op_no_func_change(self):
        def sample_func():
            return "I am a simple function."

        marked_func = mark_no_op(sample_func)

        assert marked_func() == "I am a simple function.", "The function's behaviour is changed after marking."

    @pytest.mark.negative
    def test_mark_no_op_invalid_function(self):
        invalid_func = "I am a string, not a function."

        with pytest.raises(TypeError):
            mark_no_op(invalid_func)
