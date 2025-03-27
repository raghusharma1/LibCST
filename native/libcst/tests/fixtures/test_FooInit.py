# Test module for Foo Class Initialization
import pytest
import os.path
import sys
from b.c.d.e import X
import fast
import inner_imports

# Import the class under test
from comments import Foo

# Using pytest to create a test class for Foo Initialization
class Test_FooInit:
    # Marker for Initialization with default state test
    @pytest.mark.regression
    @pytest.mark.valid
    def test_initialization_default(self):
        my_foo = Foo()
        assert my_foo.qux == 3
        assert my_foo.spam == 4

    # Marker for Effect of modifying object's attributes test
    @pytest.mark.regression
    @pytest.mark.valid
    def test_modify_attributes(self):
        my_foo = Foo()
        my_foo.qux = 5
        my_foo.spam = 6
        assert my_foo.qux == 5
        assert my_foo.spam == 6

    # Marker for test_reset_to_default
    @pytest.mark.regression
    @pytest.mark.valid
    def test_reset_to_default(self):
        my_foo = Foo()
        my_foo.qux = 5
        my_foo.spam = 6   
        my_foo.__init__()
        assert my_foo.qux == 3
        assert my_foo.spam == 4
