import pytest
import sys
from libcst._types import CSTNodeT_co
if sys.version_info < (3, 9):
    from typing import Iterable, Sequence
else:
    from collections.abc import Iterable, Sequence

from _flatten_sentinel import FlattenSentinel

class Test_FlattenSentinelInit:

    @pytest.mark.regression
    def test_passing_multiple_nodes_as_parameters(self):
        # Arrange
        cst_nodes = [CSTNodeT_co() for _ in range(5)]

        # Act
        flatten_sentinel_instance = FlattenSentinel(cst_nodes)

        # Assert
        assert len(flatten_sentinel_instance.nodes) == len(cst_nodes)
        assert all(isinstance(i, CSTNodeT_co) for i in flatten_sentinel_instance.nodes)

    @pytest.mark.regression
    def test_passing_single_node_as_parameter(self):
        # Arrange
        cst_node = CSTNodeT_co()

        # Act
        flatten_sentinel_instance = FlattenSentinel([cst_node])

        # Assert
        assert len(flatten_sentinel_instance.nodes) == 1
        assert all(isinstance(i, CSTNodeT_co) for i in flatten_sentinel_instance.nodes)

    @pytest.mark.regression
    def test_passing_no_nodes_as_parameters(self):
        # Arrange
        cst_nodes = []

        # Act
        flatten_sentinel_instance = FlattenSentinel(cst_nodes)

        # Assert
        assert len(flatten_sentinel_instance.nodes) == 0
