import pytest
from libcst._nodes.statement import AnnAssign
from _typed_visitor import visit_AnnAssign_semicolon

class Test_CstTypedBaseFunctionsVisitAnnAssignSemicolon:

    @pytest.mark.regression
    def test_pass_AnnAssign_node(self):
      ann_assign_node = AnnAssign()
      try:
          visit_AnnAssign_semicolon(ann_assign_node)
      except Exception as ex:
          pytest.fail(f"visit_AnnAssign_semicolon failed with exception: {ex}")
     
    @pytest.mark.regression
    def test_method_idempotent(self):
      ann_assign_node = AnnAssign()
      try:
          initial_state = str(ann_assign_node)
          for _ in range(5):
              visit_AnnAssign_semicolon(object_to_process)
              state_after_execution = str(ann_assign_node)
              assert initial_state == state_after_execution, f"visit_AnnAssign_semicolon mutated the argument"
      except Exception as ex:
          pytest.fail(f"visit_AnnAssign_semicolon failed with exception: {ex}")

    @pytest.mark.negative
    @pytest.mark.regression
    def test_method_handle_none(self):
      try:
          visit_AnnAssign_semicolon(None)
      except Exception as ex:
          pytest.fail(f"visit_AnnAssign_semicolon failed with exception: {ex}")
