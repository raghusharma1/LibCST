import pytest
from _typed_visitor import visit_AssignEqual
from libcst._nodes.op import AssignEqual
from typing import Optional


class Test_CstTypedBaseFunctionsVisitAssignEqual:

    @pytest.mark.parametrize('node', [
        AssignEqual()
    ])
    def test_normal_visit(self, node):
        # Arrangement is done in parameterize

        # Act
        result = visit_AssignEqual(node)

        # Assert
        assert result is None


    @pytest.mark.xfail(raises=Exception)
    @pytest.mark.parametrize('node, function', [
        (AssignEqual(), visit_AssignEqual)
    ])
    def test_visit_with_exception(self, node, function):
        # Arrangement is done in parameterize

        # Act
        function(node)

        # NOTE: Assertion is done in xfail


    @pytest.mark.parametrize('node', [
        AssignEqual()
    ])
    def test_immutable_visit(self, node):
        # Arrangement is done in parameterize

        # keep a copy to compare
        node_copy = node

        # Act
        visit_AssignEqual(node)

        # Assert
        assert node == node_copy


    @pytest.mark.xfail(raises=Exception)
    @pytest.mark.parametrize('node, function', [
        ('Invalid', visit_AssignEqual)
    ])
    def test_invalid_node(self, node, function):
        # Arrangement is done in parameterize

        # Act
        function(node)

        # NOTE: Assertion is done in xfail
