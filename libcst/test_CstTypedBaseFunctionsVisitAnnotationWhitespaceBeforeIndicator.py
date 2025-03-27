import pytest
from _typed_visitor import visit_Annotation_whitespace_before_indicator
from libcst._nodes.expression import Annotation, Attribute
from libcst._nodes.module import Module
from libcst._nodes.statement import Import, Assign

class Test_CstTypedBaseFunctionsVisitAnnotationWhitespaceBeforeIndicator:

    @pytest.mark.smoke
    def test_visit_Annotation_whitespace_before_indicator_default_behavior(self):
        # Arrange
        node = Annotation()

        # Act
        visit_Annotation_whitespace_before_indicator(node)

        # Assert
        assert node == Annotation()
    

    @pytest.mark.regression
    def test_visit_Annotation_whitespace_before_indicator_with_non_annotation_nodes(self):
        # Arrange
        node_attribute = Attribute()
        node_module = Module()
        node_import = Import()
        node_assign = Assign()

        node_objects = [node_attribute, node_module, node_import, node_assign]

        # Act and Assert
        for node_obj in node_objects:
            visit_Annotation_whitespace_before_indicator(node_obj)

            # Assertion with respective node object
            assert node_obj == type(node_obj)()

    @pytest.mark.negative
    def test_visit_annotation_whitespace_before_indicator_with_none(self):
        # Arrange
        node=None

        # Act
        visit_Annotation_whitespace_before_indicator(node)

        # Assert
        assert node == None
