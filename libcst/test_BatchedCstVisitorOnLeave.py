import inspect
import pytest
from typing import Callable, cast, Iterable, List, Mapping, MutableMapping, Optional, TYPE_CHECKING
from libcst._metadata_dependent import MetadataDependent
from libcst._typed_visitor import CSTTypedVisitorFunctions
from libcst._visitors import CSTNodeT, CSTVisitor
from libcst._nodes.base import CSTNode
from unittest.mock import MagicMock
from _batched_visitor import _BatchedCSTVisitor

VisitorMethod = Callable[["CSTNode"], None]
_VisitorMethodCollection = Mapping[str, List[VisitorMethod]]

class Test_BatchedCstVisitorOnLeave:
    
    @pytest.mark.regression
    def test_appropriate_leave_method_called(self):
        # Given
        mock_nodeA = CSTNode()
        mock_visitorA = MagicMock()
        mock_visitor_methods = {'leave_CSTNode': [mock_visitorA]}
        batched_visitor = _BatchedCSTVisitor(mock_visitor_methods)

        # When
        batched_visitor.on_leave(mock_nodeA)

        # Then
        mock_visitorA.assert_called_once_with(mock_nodeA)

    @pytest.mark.regression
    def test_after_leave_called(self):
        # Given
        mock_node = CSTNode()
        mock_after_leave = MagicMock()
        mock_visitor_methods = {'leave_CSTNode': []}
        batched_visitor = _BatchedCSTVisitor(mock_visitor_methods, after_leave=mock_after_leave)

        # When
        batched_visitor.on_leave(mock_node)

        # Then
        mock_after_leave.assert_called_once_with(mock_node)

    @pytest.mark.regression
    def test_on_leave_with_empty_visitor_methods(self):
        # Given
        mock_node = CSTNode()
        mock_visitor_methods = {}
        batched_visitor = _BatchedCSTVisitor(mock_visitor_methods)

        # When
        # Then
        # Test if method run without raising an exception
        try:
            batched_visitor.on_leave(mock_node)
        except Exception as e:
            pytest.fail(f"On_leave method raised an error: {e}")

    @pytest.mark.regression
    def test_on_leave_with_unknown_node_type(self):
        # Given
        mock_node = CSTNode()
        mock_visitor_methods = {'leave_OtherNodeType': []}
        batched_visitor = _BatchedCSTVisitor(mock_visitor_methods)

        # When
        # Then
        # Test if method run without raising an exception
        try:
            batched_visitor.on_leave(mock_node)
        except Exception as e:
            pytest.fail(f"On_leave method raised an error: {e}")
