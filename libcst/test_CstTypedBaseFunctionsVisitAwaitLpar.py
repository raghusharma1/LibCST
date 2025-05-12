from libcst._typed_visitor import visit_Await_lpar
from libcst import Await
import pytest

class Test_CstTypedBaseFunctionsVisitAwaitLpar:

    @pytest.mark.smoke
    def test_visit_Await_None(self):
        # Arrange
        node = None

        # Act and Assert
        try:
            visit_Await_lpar(node)
        except Exception as e:
            pytest.fail(f"visit_Await_lpar() raised an exception with an unexpected input: {e}")

    @pytest.mark.valid
    def test_visit_Await_ValidNode(self):
        # Arrange
        node = Await()

        # Act and Assert
        try:
            visit_Await_lpar(node)
        except Exception as e:
            pytest.fail(f"visit_Await_lpar() raised an exception with a valid input: {e}")

    @pytest.mark.invalid    
    def test_visit_Await_InvalidNode(self):
        # Arrange
        node = "InvalidNode"

        # Act and Assert
        try:
            visit_Await_lpar(node)
        except Exception as e:
            pytest.fail(f"visit_Await_lpar() raised an exception with an invalid input: {e}")
