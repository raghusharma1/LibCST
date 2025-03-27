import pytest
from libcst._nodes.statement import AugAssign
from _typed_visitor import visit_AugAssign_target
from typing import Optional

class Test_CstTypedBaseFunctionsVisitAugAssignTarget:

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_visit_AugAssign_target_Empty(self):
        try:
            visit_AugAssign_target()
            assert True
        except:
            assert False
  
    @pytest.mark.regression
    @pytest.mark.negative
    def test_visit_AugAssign_target_ValidType(self):
        test_values = [1, "string", None, ["test"], {"key": "value"}]
        for value in test_values:
            try:
                visit_AugAssign_target(value)
                assert True
            except:
                assert False

    @pytest.mark.performance
    @pytest.mark.positive
    def test_visit_AugAssign_target_Performance(self):
        large_AugAssign_node = AugAssign(Optional[LeftParen()]*1_000_000)
        try:
            visit_AugAssign_target(large_AugAssign_node)
            assert True
        except:
            assert False
