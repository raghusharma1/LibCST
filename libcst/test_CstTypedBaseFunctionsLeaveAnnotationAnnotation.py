import pytest
from _typed_visitor import leave_Annotation_annotation
from libcst._nodes.expression import Annotation
from libcst._nodes.op import Star
from libcst._nodes.statement import NameItem
from libcst._nodes.module import Module
from libcst._parser.errors import ParserSyntaxError

class Test_CstTypedBaseFunctionsLeaveAnnotationAnnotation:

    @pytest.mark.regression
    def test_leave_annotation_no_op(self):
        # Arrange: Create a dummy "Annotation" node
        dummy_annotation = Annotation(NameItem('TypeA'), Module('dummy_module'))
        
        # Act: Invoke the leave_Annotation_annotation function
        result = leave_Annotation_annotation(dummy_annotation)
        
        # Assert: Check returned node equal to original node (no operation performed)
        assert result == dummy_annotation, "The function leave_Annotation_annotation did not work as a no-op."

    @pytest.mark.regression
    def test_leave_annotation_no_return_value(self):
        # Arrange: Create a dummy "Annotation" node
        dummy_annotation = Annotation(NameItem('TypeB'), Module('dummy_module'))
        
        # Act: Invoke the leave_Annotation_annotation function and capture return value
        result = leave_Annotation_annotation(dummy_annotation)
        
        # Assert: Check returned value is None (no return value expected)
        assert result is None, "The function leave_Annotation_annotation returned a value. It is not expected to return a value."

    @pytest.mark.regression
    @pytest.mark.parametrize("dummy_annotation", [
        (Annotation(NameItem('TypeC'), Module('dummy_module'))),
        (Annotation(Star(), Module('dummy_module'))),
        (Annotation(None, Module('dummy_module'))),
    ])
    def test_leave_annotation_node_compatibility(self, dummy_annotation):
        # Act and Assert: Invoke the function and expect no exception raised
        try:
            leave_Annotation_annotation(dummy_annotation)
        except Exception as e:
            pytest.fail(f"The function leave_Annotation_annotation raised an exception with message: {str(e)}")
