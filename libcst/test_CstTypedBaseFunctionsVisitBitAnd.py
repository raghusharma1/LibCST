import pytest
from _typed_visitor import visit_BitAnd
from libcst._nodes.op import BitAnd, Add

class Test_CstTypedBaseFunctionsVisitBitAnd:

    # Scenario 1: Check if the visit_BitAnd function returns None
    def test_visit_BitAnd_returns_none(self):
        bit_and_object = BitAnd()
        result = visit_BitAnd(bit_and_object)
        assert result is None, "The visit_BitAnd should return None"

    # Scenario 2: The function visit_BitAnd is invoked with a non-"BitAnd" type object
    def test_visit_BitAnd_with_non_BitAnd_object(self):
        non_bit_and_object = Add()
        result = visit_BitAnd(non_bit_and_object)
        assert result is None, "The visit_BitAnd called with non-BitAnd object should return None"
        
    # Scenario 3: The function visit_BitAnd is called without parameters
    def test_visit_BitAnd_without_parameters(self):
        with pytest.raises(TypeError):
            visit_BitAnd()
