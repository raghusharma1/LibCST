import pytest
from libcst._nodes.expression import Annotation
from _typed_visitor import leave_Annotation_whitespace_after_indicator

class Test_CstTypedBaseFunctionsLeaveAnnotationWhitespaceAfterIndicator:
    @pytest.mark.valid
    def test_leave_Annotation_whitespace_after_indicator_with_annotation(self):
        # Arrange
        annotation = Annotation()
        # Act and Assert
        try:
            leave_Annotation_whitespace_after_indicator(annotation)
        except Exception as e:
            pytest.fail(f"Test failed due to: {str(e)}")

    @pytest.mark.valid
    @pytest.mark.parametrize("annotation", [
        Annotation(),  # empty annotation instance
        Annotation(name="a"),  # with name
        Annotation(name="a", whitespace_after_indicator=SimpleWhitespace(value=" ")),  # with name and whitespace
    ])
    def test_leave_Annotation_whitespace_after_indicator_with_various_annotations(self, annotation):
        # Act and Assert
        try:
            leave_Annotation_whitespace_after_indicator(annotation)
        except Exception as e:
            pytest.fail(f"Test failed with {annotation} due to: {str(e)}")

    @pytest.mark.negative
    def test_leave_Annotation_whitespace_after_indicator_with_empty_annotation(self):
        # Arrange
        annotation = Annotation()
        # Act and Assert
        try:
            leave_Annotation_whitespace_after_indicator(annotation)
        except Exception as e:
            pytest.fail(f"Test failed due to: {str(e)}")

    @pytest.mark.negative
    def test_leave_Annotation_whitespace_after_indicator_with_null_input(self):
        # Arrange
        annotation = None
        # Act and Assert
        try:
            leave_Annotation_whitespace_after_indicator(annotation)
        except Exception as e:
            assert True 
        else:
            pytest.fail("Test failed, function should have raised an exception")
