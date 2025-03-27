import pytest
from libcst._nodes.statement import AnnAssign
from _typed_visitor import leave_AnnAssign_annotation


class Test_CstTypedBaseFunctionsLeaveAnnAssignAnnotation:

    @pytest.mark.regression  # annotation for type of testing
    def test_leave_AnnAssign_annotation_with_instance(self):
        ann_assign_instance = AnnAssign()  # TODO: initialize with valid parameters
        assert leave_AnnAssign_annotation(ann_assign_instance) is None  # Function is expected to just pass without any exceptions

    
    @pytest.mark.regression  # annotation for type of testing
    def test_leave_AnnAssign_annotation_with_wrong_type(self):
        non_ann_assign_var = 10  # A Type other than AnnAssign
        assert leave_AnnAssign_annotation(non_ann_assign_var) is None  # Function should handle any type and not only AnnAssign. Thus, it should not raise any exceptions

        
    @pytest.mark.negative  # annotation for type of testing
    def test_leave_AnnAssign_annotation_with_no_args(self):
        with pytest.raises(TypeError):  # As the function expects a required parameter, not passing any should raise a TypeError
            leave_AnnAssign_annotation()

    @pytest.mark.regression  # annotation for type of testing
    def test_leave_AnnAssign_annotation_return(self):
        ann_assign_instance = AnnAssign()  # TODO: initialize with valid parameters
        assert leave_AnnAssign_annotation(ann_assign_instance) is None  # Function is expected to return None always as per its definition

