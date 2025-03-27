import pytest
from _typed_visitor import visit_Assert_test
from libcst._nodes.statement import Assert, ClassDef, FunctionDef

class Test_CstTypedBaseFunctionsVisitAssertTest:
  
  @pytest.mark.smoke
  def test_empty_node_handling(self):
    # Arrange: Create an empty Assert node
    node = Assert()

    # Act and Assert: Function executes without raising any exceptions
    try:
        visit_Assert_test(node)
        assert True, "visit_Assert_test accepted an empty Assert node without exceptions"
    except Exception as e:
        pytest.fail(f"visit_Assert_test raised an exception with an empty Assert node: {e}")
        
  @pytest.mark.security
  def test_node_param_ignored(self):
    # Arrange: Create Assert nodes with different types
    nodes = [
        Assert(Parse("2 == 2")),
        Assert(Parse("3 < 4")),
        Assert(Parse("True is not False"))
    ]

    # Act and Assert: Function executes without raising any exceptions
    for node in nodes:
        try:
            visit_Assert_test(node)
            assert True, "visit_Assert_test executed successfully regardless of node value"
        except Exception as e:
            pytest.fail(f"visit_Assert_test raised an exception with node value: {e}")
        
  @pytest.mark.regression
  def test_non_assert_node(self):
    # Arrange: Create an instance of a non-Assert node
    nodes = [
        ClassDef("class_name"),
        FunctionDef(name="func_name", params=[], body=[])
    ]
  
    # Act and Assert: Function executes without any errors
    for node in nodes:
        try:
            visit_Assert_test(node)
            assert True, "visit_Assert_test executed successfully with a non-Assert node"
        except Exception as e:
            pytest.fail(f"visit_Assert_test raised an exception with a non-Assert node: {e}")
  
  @pytest.mark.performance
  def test_multiple_calls(self):
    # Arrange: Create a list of Assert nodes
    nodes = [Assert() for _ in range(10)]
  
    # Act and Assert: All iterations of the loop run without raising exceptions
    for node in nodes:
        try:
            visit_Assert_test(node)
            assert True, "visit_Assert_test executed successfully in multiple consecutive calls"
        except Exception as e:
            pytest.fail(f"visit_Assert_test raised an exception on multiple calls: {e}")
