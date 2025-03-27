import pytest
from _typed_visitor import visit_Assign_value
from libcst._nodes.statement import Assign

class Test_CstTypedBaseFunctionsVisitAssignValue:

    @pytest.mark.smoke
    def test_no_input_arg_execution(self):
        # Arrange, Act & Assert: Call function without argument
        try:
            visit_Assign_value()
        except Exception:
            pytest.fail("Function failed to handle execution without argument!")

    @pytest.mark.regression
    def test_execution_with_assign_instance(self):
        # Arrange: Instantiate assign object
        assign_instance = Assign()

        # Act & Assert: Call function with object
        try:
            visit_Assign_value(assign_instance)
        except Exception:
            pytest.fail("Function failed to process with Assign instance!")

    @pytest.mark.negative
    def test_execution_with_unexpected_type_arg(self):
        # Arrange: Instantiate non-assign object
        non_assign_instance = int(3)

        # Act & Assert: Call function with unexpected data type
        try:
            visit_Assign_value(non_assign_instance)
        except Exception:
            pytest.fail("Function failed to handle execution with unexpected data type!")
