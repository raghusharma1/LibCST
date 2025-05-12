import pytest
import threading
from _typed_visitor import visit_AssignTarget_whitespace_after_equal
from libcst._nodes.statement import AssignTarget
from libcst._nodes.whitespace import SimpleWhitespace


class Test_CstTypedBaseFunctionsVisitAssignTargetWhitespaceAfterEqual:
    
    @pytest.mark.regression
    def test_function_with_typical_AssignTarget(self):
        test_assign_target = AssignTarget(target=Name("demo"), whitespace_after_equal=SimpleWhitespace(" "))
        
        try:
            visit_AssignTarget_whitespace_after_equal(test_assign_target)
        except Exception:
            pytest.fail("The function threw an unexpected exception.")
            
    @pytest.mark.regression
    def test_function_with_empty_AssignTarget(self):
        empty_assign_target = AssignTarget()

        try:
            visit_AssignTarget_whitespace_after_equal(empty_assign_target)
        except Exception:
            pytest.fail("The function threw an unexpected exception with an empty assign target.")

    @pytest.mark.performance
    def test_function_with_large_sized_AssignTarget(self):
        large_assign_target = AssignTarget(
            target=Name("a" * 10000), whitespace_after_equal=SimpleWhitespace(" ")
        )

        try:
            visit_AssignTarget_whitespace_after_equal(large_assign_target)
        except Exception:
            pytest.fail("The function threw an unexpected exception with a large-sized assign target.")

    @pytest.mark.regression
    def test_function_acceptability_different_AST(self):
        complex_assign_target = AssignTarget(
            target=Tuple(
                [
                    Name("a"),
                    Tuple([Name("b"), Name("c")]),
                    Name("d"),
                ]
            ),
            whitespace_after_equal=SimpleWhitespace(" "),
        )

        try:
            visit_AssignTarget_whitespace_after_equal(complex_assign_target)
        except Exception:
            pytest.fail("The function threw an unexpected exception when navigating complex nodes in the abstract syntax tree (AST).")

    @pytest.mark.performance
    def test_function_concurrent_execution(self):
        test_assign_target = AssignTarget(
            target=Name("demo"), whitespace_after_equal=SimpleWhitespace(" ")
        )

        threads = []
        for i in range(10):
            threads.append(
                threading.Thread(target=visit_AssignTarget_whitespace_after_equal, args=(test_assign_target,))
            )

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        for thread in threads:
            assert not thread.is_alive(), "Not all threads completed successfully."
