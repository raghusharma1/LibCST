import pytest
from _typed_visitor import leave_Annotation_whitespace_before_indicator
from libcst._nodes.expression import Annotation

class Test_CstTypedBaseFunctionsLeaveAnnotationWhitespaceBeforeIndicator:
    @pytest.mark.smoke
    def test_whitespace_annotation_node_empty(self):
        # Arrange
        node = Annotation()
        # Act
        try:
            leave_Annotation_whitespace_before_indicator(node)
            assert True
        except Exception as e:
            pytest.fail(f"Test failed due to unexpected Error: {e}")
        # Assert
        assert node.whitespace_before_indicator == ""
      
    @pytest.mark.regression
    def test_whitespace_annotation_node_non_empty(self):
        # Arrange
        node = Annotation(whitespace_before_indicator=" ")
        # Act
        try:
            leave_Annotation_whitespace_before_indicator(node)
            assert True
        except Exception as e:
            pytest.fail(f"Test failed due to unexpected Error: {e}")
        # Assert
        assert node.whitespace_before_indicator == " "

    @pytest.mark.negative
    def test_whitespace_annotation_node_none(self):
        # Arrange
        node = None
        # Act
        try:
            leave_Annotation_whitespace_before_indicator(node)
            assert True
        except Exception as e:
            pytest.fail(f"Test failed due to unexpected Error: {e}")
        # Assert
        assert node is None
