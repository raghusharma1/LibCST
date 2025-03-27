import pytest
import sys
import io
from fun_with_func_defs import say_hello

class Test_FunWithFuncDefsSayHello:
    
    def test_say_hello_with_valid_string_user(self):
        sys.stdout = io.StringIO()
        user = "Python Programmer"
        say_hello(user)
        output = sys.stdout.getvalue()
        assert output == "Hello Python Programmer\n", "The message is not correct."
        
    def test_say_hello_with_special_string_user(self):
        sys.stdout = io.StringIO()
        user = " Python   Programmer 23! "
        say_hello(user)
        output = sys.stdout.getvalue()
        assert output == "Hello  Python   Programmer 23! \n", "The message is not correct."
        
    def test_say_hello_with_empty_string_user(self):
        sys.stdout = io.StringIO()
        user = ""
        say_hello(user)
        output = sys.stdout.getvalue()
        assert output == "Hello \n", "The message is not correct."
