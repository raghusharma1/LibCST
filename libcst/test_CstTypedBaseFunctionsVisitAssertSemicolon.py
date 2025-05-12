import pytest
from libcst._nodes.statement import Assert, If
from _typed_visitor import visit_Assert_semicolon

class Test_CstTypedBaseFunctionsVisitAssertSemicolon:

    @pytest.mark.regression
    def test_visit_Assert_semicolon_nothing_done(self):
        assert_instance = Assert()
        original_assert_instance = assert_instance
        visit_Assert_semicolon(assert_instance)
        assert assert_instance == original_assert_instance, "visit_Assert_semicolon function altered the original Assert instance"

    @pytest.mark.smoke
    @pytest.mark.security
    def test_visit_Assert_semicolon_type(self):
        assert_instance = Assert()
        if_instance = If()
        
        # Expected to run without exceptions
        visit_Assert_semicolon(assert_instance)

        # Expected to raise TypeError
        with pytest.raises(TypeError):
            visit_Assert_semicolon(if_instance)

    @pytest.mark.regression
    def test_visit_Assert_semicolon_multiple_invocations(self):
        assert_instances = [Assert() for _ in range(3)]
        original_assert_instances = assert_instances.copy()
        
        for assert_instance in assert_instances:
            visit_Assert_semicolon(assert_instance)
            
        for i in range(len(assert_instances)):
            assert assert_instances[i] == original_assert_instances[i], \
            f"visit_Assert_semicolon function altered the original Assert instance at index {i}"
