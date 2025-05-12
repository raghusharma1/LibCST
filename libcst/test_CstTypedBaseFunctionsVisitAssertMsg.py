import pytest
import libcst as cst
from _typed_visitor import visit_Assert_msg
from libcst._nodes.statement import Assert
from libcst._nodes.expression import Call

class Test_CstTypedBaseFunctionsVisitAssertMsg:

    @pytest.mark.valid
    def test_visit_Assert_no_msg_passed(self):
        empty_assert = cst.Assert(test=cst.Name("test"))
        try:
            visit_Assert_msg(empty_assert)
        except Exception as e:
            pytest.fail(f"visit_Assert_msg() failed with an exception: {str(e)}")

    @pytest.mark.valid
    def test_visit_Assert_msg_passed(self):
        mock_assert = cst.Assert(test=cst.Name("test"), msg=cst.SimpleString('assertion message'))
        try:
            visit_Assert_msg(mock_assert)
        except Exception as e:
            pytest.fail(f"visit_Assert_msg() failed with an exception: {str(e)}")

    @pytest.mark.valid
    def test_visit_Assert_non_assert_node(self):
        non_assert_node = cst.Call(func=cst.Name("dummy"))
        try:
            visit_Assert_msg(non_assert_node)
        except Exception as e:
            pytest.fail(f"visit_Assert_msg() failed with an exception: {str(e)}")

    @pytest.mark.valid
    def test_visit_Assert_null_node(self):
        try:
            visit_Assert_msg(None)
        except Exception as e:
            pytest.fail(f"visit_Assert_msg() failed with an exception: {str(e)}")
