import pytest
from fun_with_func_defs import second

@pytest.mark.regression
@pytest.mark.smoke
def test_second_with_none():
    """
    Verify that the function `second` handles the `None` input correctly.
    """
    with pytest.raises(TypeError):
        second(None)


@pytest.mark.regression
def test_second_with_common_inner_type():
    """
    Verify how the function `second` handles a list.
    """
    def inner_func():
        pass

    assert second(inner_func) is None, "The function second should always return None"


@pytest.mark.regression
@pytest.mark.smoke
def test_second_with_empty_input():
    """
    Ensure the function `second` handles empty input correctly.
    """
    empty_list = []

    assert second(empty_list) is None, "The function second should always return None"


@pytest.mark.regression
def test_second_with_nested_sequences():
    """
    Ensure the function `second` works correctly when the input is a nested sequence.
    """
    nested_sequences = [[1,2,3], [4,5,6], [7,8,9]]

    assert second(nested_sequences) is None, "The function second should always return None"
