import inspect
import pytest
from typing import Callable, cast, Iterable, List, Mapping, MutableMapping, Optional, TYPE_CHECKING
from libcst._metadata_dependent import MetadataDependent
from libcst._typed_visitor import CSTTypedVisitorFunctions
from libcst._visitors import CSTNodeT, CSTVisitor
from libcst._nodes.base import CSTNode
from _batched_visitor import _BatchedCSTVisitor

# Define mock visitor methods collection for tests
visitor_methods: Mapping[str, List[CSTNodeT,]] = {
    'visit_Module': [CSTNode()],
    'leave_Module': [CSTNode()],
}

# Define mock functions for before_visit and after_leave parameters
def mock_function(node: CSTNodeT) -> None:
    pass

class Test_BatchedCstVisitorInit:  
   
    def test_init_valid_visitor_methods(self):
        visitor = _BatchedCSTVisitor(visitor_methods)
        assert visitor.visitor_methods == visitor_methods
    
    def test_init_before_visit_parameter(self):
        visitor = _BatchedCSTVisitor(visitor_methods, before_visit=mock_function)
        assert visitor.before_visit == mock_function
        
    def test_init_after_leave_parameter(self):
        visitor = _BatchedCSTVisitor(visitor_methods, after_leave=mock_function)
        assert visitor.after_leave == mock_function

    def test_init_both_params(self):
        visitor = _BatchedCSTVisitor(visitor_methods, before_visit=mock_function, after_leave=mock_function)
        assert visitor.before_visit == mock_function
        assert visitor.after_leave == mock_function

    def test_init_no_params(self):
        visitor = _BatchedCSTVisitor(visitor_methods)
        assert visitor.before_visit is None
        assert visitor.after_leave is None
