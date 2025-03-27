import pytest
from _typed_visitor import CSTTypedBaseFunctions
from libcst._nodes.statement import Assign

class Test_CstTypedBaseFunctionsVisitAssignSemicolon:
    @pytest.mark.smoke
    def test_visit_Assign_semicolon_execution(self):
        # Arrange
        cst_typed_base = CSTTypedBaseFunctions()
        assign_inst = Assign()

        # Act
        try:
            cst_typed_base.visit_Assign_semicolon(assign_inst)
            # Assert
            assert True
        except:
            assert False

    @pytest.mark.regression
    def test_visit_Assign_semicolon_modification(self):
        # Arrange
        cst_typed_base = CSTTypedBaseFunctions()
        assign_inst = Assign()

        orig_assign_inst = assign_inst

        # Act
        cst_typed_base.visit_Assign_semicolon(assign_inst)

        # Assert
        assert orig_assign_inst == assign_inst

    @pytest.mark.valid
    def test_visit_Assign_semicolon_return(self):
        # Arrange
        cst_typed_base = CSTTypedBaseFunctions()
        assign_inst = Assign()

        # Act
        result = cst_typed_base.visit_Assign_semicolon(assign_inst)

        # Assert
        assert result is None

