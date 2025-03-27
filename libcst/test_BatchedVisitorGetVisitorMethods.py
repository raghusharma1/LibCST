#Importing necessary libraries
import pytest
import inspect
from typing import Callable, cast, Iterable, List, Mapping, MutableMapping, Optional, TYPE_CHECKING
from libcst._metadata_dependent import MetadataDependent
from libcst._typed_visitor import CSTTypedVisitorFunctions
from libcst._visitors import CSTNodeT, CSTVisitor
from libcst._nodes.base import CSTNode

#Importing the function to be tested
from _batched_visitor import _get_visitor_methods

#Test Class
class Test_BatchedVisitorGetVisitorMethods:

    @pytest.mark.parametrize('batchable_visitors', [{}])
    def test_empty_batchable_visitors(self, batchable_visitors):
        #Act: Call function with empty list as input.
        output = _get_visitor_methods(batchable_visitors)
        
        #Assert: check returned value is an empty dict
        assert output == {}, "Expected an empty dictionary"

    @pytest.mark.parametrize('batchable_visitors', [{
        'batchable_visitor1': ['methodA', 'methodB', 'methodC'],
    }])
    def test_single_batchable_visitors_multiple_methods(self, batchable_visitors):
        #Act: Call function with single batchable_visitor with multiple methods
        output = _get_visitor_methods(batchable_visitors)
        
        #Assert: Check returned dictionary has keys equal to visitor methods and values as respective methods
        assert len(output.keys()) == 3, "Expected 3 keys in output dictionary"
        assert 'methodA' in output.keys() and 'methodB' in output.keys() and 'methodC' in output.keys(), 'Expected methods in keys of result'

    @pytest.mark.parametrize('batchable_visitors', [{
        'batchable_visitor1': ['methodA'],
        'batchable_visitor2': ['methodB'],
        'batchable_visitor3': ['methodC'],
    }])
    def test_multiple_batchable_visitors_single_method(self, batchable_visitors):
        #Act: Invoke function with multiple batchable_visitors with single method each
        output = _get_visitor_methods(batchable_visitors)
        
        #Assert: Check returned dictionary has keys as visitor methods from each batchable_visitor
        assert len(output.keys()) == 3, "Expected 3 keys in output dictionary"
        assert 'methodA' in output.keys() and 'methodB' in output.keys() and 'methodC' in output.keys(), 'Expected methods in keys of r    esult'

    @pytest.mark.parametrize('batchable_visitors', [{
        'batchable_visitor1': ['visit_A', 'leave_A'],
        'batchable_visitor2': ['visit_B', 'leave_B'],
    }])
    def test_mixed_methods_in_batchable_visitors(self, batchable_visitors):
        #Act: Invoke function with batchable_visitors having mixture of visit and leave methods
        output = _get_visitor_methods(batchable_visitors)
        
        #Assert: Check returned dictionary has keys as mixture of visit and leave methods from batchable_visitors
        assert len(output.keys()) == 4, "Expected 4 keys in output dictionary"
        assert 'visit_A' in output.keys() and 'leave_A' in output.keys() and 'visit_B' in output.keys() and 'leave_B' in output.keys(), 'Expected methods in keys of result'
