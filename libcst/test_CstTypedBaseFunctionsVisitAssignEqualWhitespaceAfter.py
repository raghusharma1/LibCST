import pytest
from _typed_visitor import visit_AssignEqual_whitespace_after
from libcst._nodes.op import AssignEqual
from libcst._nodes.expression import Name


@pytest.mark.parametrize("assign_equal", [AssignEqual()])
def test_visit_AssignEqual_whitespace_after(assign_equal):
    try:
        visit_AssignEqual_whitespace_after(assign_equal)
    except Exception as e:
        pytest.fail(f"Test failed with error: {e}")


@pytest.mark.parametrize("name", [Name('test_name')])
def test_inappropriate_node(name):
    try:
        visit_AssignEqual_whitespace_after(name)
    except Exception as e:
        pytest.fail(f"Test failed with error: {e}")


def test_no_node():
    try:
        visit_AssignEqual_whitespace_after()
    except Exception as e:
        pytest.fail(f"Test failed with error: {e}")
