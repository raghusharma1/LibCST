import inspect
from typing import Callable, cast, Iterable, List, Mapping, MutableMapping, Optional, TYPE_CHECKING
from libcst._metadata_dependent import MetadataDependent
from libcst._typed_visitor import CSTTypedVisitorFunctions
from libcst._visitors import CSTNodeT, CSTVisitor
from libcst._nodes.base import CSTNode

if TYPE_CHECKING:
    from libcst._nodes.base import CSTNode

VisitorMethod = Callable[["CSTNode"], None]
_VisitorMethodCollection = Mapping[str, List[VisitorMethod]]

# Importing the actual class/method that needs to be tested
from _batched_visitor import get_visitors, BatchableCSTVisitor

# Required imports for testing
import pytest
from unittest.mock import Mock

class Test_BatchableCstVisitorGetVisitors:
    def test_get_visitors(self):
        class TestCSTVisitor(BatchableCSTVisitor):
            def visit_TestNode(self):
                pass
            def leave_TestNode(self):
                pass
            def visit_TestNode_no_op(self):
                pass
		# annotating with '_is_no_op' as True which should be excluded
            visit_TestNode_no_op._is_no_op = True

        visitor = TestCSTVisitor()
        res = visitor.get_visitors()

        assert 'visit_TestNode' in res
        assert 'leave_TestNode' in res
        assert 'visit_TestNode_no_op' not in res

    def test_get_visitors_no_valid_methods(self):
        class TestCSTVisitor(BatchableCSTVisitor):
            def visit_TestNode_no_op(self):
                pass
		# annotating with '_is_no_op' as True which should be excluded	
            visit_TestNode_no_op._is_no_op = True

        visitor = TestCSTVisitor()
        res = visitor.get_visitors()
        assert len(res) == 0

    def test_get_visitors_invalid_refs(self):
        class InvalidNode:  # this is not a valid node class
            pass

        class TestCSTVisitor(BatchableCSTVisitor):
            def visit_InvalidNode(self):  # this method does not reference a valid node class
                pass

        visitor = TestCSTVisitor()
        res = visitor.get_visitors()

	# Currently the code does not handle this scenario, so we are just ensuring the test setup is correct
        assert 'visit_InvalidNode' in res
