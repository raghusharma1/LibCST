import pytest
from _typed_visitor import visit_Annotation_annotation
from libcst._nodes.expression import Annotation, Name
from libcst._nodes.op import Multiply

class Test_CstTypedBaseFunctionsVisitAnnotationAnnotation:

    @pytest.mark.smoke
    def test_handle_annotation_node(self):
        annot = Annotation(Name("MyClass"))
        try:
            visit_Annotation_annotation(annot)
        except Exception as e:
            pytest.fail(f"Test failed due to {e}")
              
    @pytest.mark.negative
    def test_handle_non_annotation_node(self):
        non_annot = Multiply()
        try:
            visit_Annotation_annotation(non_annot)
        except Exception as e:
            pytest.fail(f"Test failed due to {e}")
              
    @pytest.mark.negative
    def test_handle_none(self):
        try:
            visit_Annotation_annotation(None)
        except Exception as e:
            pytest.fail(f"Test failed due to {e}")
