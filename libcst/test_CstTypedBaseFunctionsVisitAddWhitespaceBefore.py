import pytest
from _typed_visitor import visit_Add_whitespace_before
from libcst._nodes.op import Add, Subtract
from typing import Union

class Test_CstTypedBaseFunctionsVisitAddWhitespaceBefore:

    @pytest.mark.parametrize("node", [Add()])
    @pytest.mark.valid
    @pytest.mark.regression
    def test_add_node(self, node: Union[Add, Subtract]):
        # Act
        try:
            visit_Add_whitespace_before(node)
            result = True
        except:
            result = False
        # Assert
        assert result == True, "visit_Add_whitespace_before function is expected to run without errors or exceptions with 'Add' node"

    @pytest.mark.parametrize("node", [Subtract()])
    @pytest.mark.valid
    @pytest.mark.regression
    def test_non_add_node(self, node: Union[Add, Subtract]):
        # Act
        try:
            visit_Add_whitespace_before(node)
            result = True
        except:
            result = False
        # Assert
        assert result == True, "visit_Add_whitespace_before function is expected to run without errors or exceptions with non-'Add' node"

    @pytest.mark.valid
    @pytest.mark.regression
    def test_null_node(self):
        # Act
        try:
            visit_Add_whitespace_before(None)
            result = True
        except:
            result = False
        # Assert
        assert result == True, "visit_Add_whitespace_before function is expected to run without errors or exceptions when passed 'null'"
