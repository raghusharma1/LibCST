import pytest
from libcst import AsName
from _typed_visitor import visit_AsName_whitespace_after_as

class Test_CstTypedBaseFunctionsVisitAsNameWhitespaceAfterAs:

    # Scenario 1: Test Function visit_AsName_whitespace_after_as With Non-empty AsName Node
    def test_visit_AsName_whitespace_non_empty_node(self):
        as_name_instance = AsName("Test AsName")
        try:
            visit_AsName_whitespace_after_as(as_name_instance)
        except Exception as e:
            pytest.fail(f"visit_AsName_whitespace_after_as() failed with non-empty AsName instance with error {str(e)}")

    # Scenario 2: Test Function visit_AsName_whitespace_after_as With Empty AsName Node
    def test_visit_AsName_whitespace_empty_node(self):
        as_name_instance = AsName("")
        try:
            visit_AsName_whitespace_after_as(as_name_instance)
        except Exception as e:
            pytest.fail(f"visit_AsName_whitespace_after_as() failed with empty AsName instance with error {str(e)}")

    # Scenario 3: Test Function visit_AsName_whitespace_after_as With Multiple Invocations
    def test_visit_AsName_whitespace_multiple_invocations(self):
        as_name_instances = [AsName("Test1"), AsName("Test2"), AsName("Test3")]
        for instance in as_name_instances:
            try:
                visit_AsName_whitespace_after_as(instance)
            except Exception as e:
                pytest.fail(f"visit_AsName_whitespace_after_as() failed on multiple invocations with AsName instance {str(instance)} with error {str(e)}")
