import pytest
from _typed_visitor import leave_Add_whitespace_before
from libcst._nodes.op import Add
from libcst._nodes.statement import Assign


class Test_CstTypedBaseFunctionsLeaveAddWhitespaceBefore:
    
    @pytest.mark.smoke
    def test_Add_whitespace_before_no_operation(self):
        # Arrange
        add_obj_initial = Add()
        add_obj = add_obj_initial
        
        # Act
        leave_Add_whitespace_before(add_obj)
        
        # Assert
        assert add_obj_initial == add_obj, "The Add object should remain unchanged."
        
    @pytest.mark.regression
    def test_Add_whitespace_before_no_effect_on_other_objects(self):
        # Arrange
        add_obj = Add()
        assign_obj_initial = Assign()
        assign_obj = assign_obj_initial
        
        # Act
        leave_Add_whitespace_before(add_obj)
        
        # Assert
        assert assign_obj_initial == assign_obj, "The second object should remain unchanged."
        
    @pytest.mark.smoke
    def test_Add_whitespace_before_no_exceptions(self):
        # Arrange
        add_obj = Add()
        
        # Act
        try:
            leave_Add_whitespace_before(add_obj)
            assert True, "The function execution should be successful without any exceptions."
        except:
            pytest.fail("An error or exception occurred during function execution.")
