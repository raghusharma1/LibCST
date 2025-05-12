import pytest
from typing import Optional
from _typed_visitor import visit_Add
from libcst._nodes.op import Add, Divide

class Test_CstTypedBaseFunctionsVisitAdd:

    @pytest.mark.positive
    def test_visit_Add_with_Add_object(self):
        # Arrange
        add_obj = Add()

        # Act
        try:
            result = visit_Add(add_obj)
            # Assert That no Exception is thrown
            assert True
        except:
            assert False

    @pytest.mark.negative
    def test_visit_Add_with_non_Add_object(self):
        # Arrange
        divide_obj = Divide()

        # Act
        with pytest.raises(TypeError) as exc:
            result = visit_Add(divide_obj)

        # Assert
        assert str(exc.value) == 'visit_Add function expects a Add type object'
    
    @pytest.mark.regression
    def test_visit_Add_return_type(self):
        # Arrange
        add_obj = Add()

        # Act
        result = visit_Add(add_obj)

        # Assert
        assert isinstance(result, (type(None), bool)), 'The return type is not Optional[bool]'

