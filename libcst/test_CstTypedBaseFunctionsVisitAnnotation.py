import pytest
from libcst import Annotation
from libcst._typed_visitor import visit_Annotation

class Test_CstTypedBaseFunctionsVisitAnnotation:

    @pytest.mark.valid
    def test_visit_Annotation_with_content(self):
        # Arrange
        node = Annotation(whitespace_before_indicator=SimpleWhitespace(value=" "), whitespace_after_indicator=SimpleWhitespace(value=" "))
        # Act
        result = visit_Annotation(node)
        # Assert
        assert node.whitespace_before_indicator.value == " "
        assert node.whitespace_after_indicator.value == " "
        assert result is None

    @pytest.mark.valid
    def test_visit_Annotation_with_empty_node(self):
        # Arrange
        node = Annotation()
        # Act
        result = visit_Annotation(node)
        # Assert
        assert node.whitespace_before_indicator is None
        assert node.whitespace_after_indicator is None
        assert result is None

    @pytest.mark.valid
    @pytest.mark.parametrize(
        "content",
        [
            SimpleWhitespace(value=" "),
            SimpleWhitespace(value="  "),
            SimpleWhitespace(value="\n")
        ],
    )
    def test_visit_Annotation_with_various_contents(self, content):
        # Arrange
        node = Annotation(whitespace_before_indicator=content, whitespace_after_indicator=content)
        # Act
        result = visit_Annotation(node)
        # Assert
        assert node.whitespace_before_indicator.value == content.value
        assert node.whitespace_after_indicator.value == content.value
        assert result is None
