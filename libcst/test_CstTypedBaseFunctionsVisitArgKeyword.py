import pytest
from typing import Optional, TYPE_CHECKING, Union
from libcst import Arg, Add, Name, Integer, Break
from _typed_visitor import visit_Arg_keyword


class Test_CstTypedBaseFunctionsVisitArgKeyword:

    def test_visit_Arg_keyword_nop(self):
        # Create an instance of "Arg"
        node_arg = Arg(Name("test"))
        # We call the function with our Arg instance
        visit_Arg_keyword(node_arg)
        # Assert: Validate no change in Arg instance
        assert node_arg == Arg(Name("test"))

    def test_visit_Arg_keyword_only_accepts_Arg_objects(self):
        # Creating instances of different types
        add_instance = Add()
        name_instance = Name("test")
        integer_instance = Integer(5)
        break_instance = Break()

        # Assert: Validate TypeError when function is invoked with an instance of a different type
        with pytest.raises(TypeError):
            visit_Arg_keyword(add_instance)
        with pytest.raises(TypeError):
            visit_Arg_keyword(name_instance)
        with pytest.raises(TypeError):
            visit_Arg_keyword(integer_instance)
        with pytest.raises(TypeError):
            visit_Arg_keyword(break_instance)

    def test_visit_Arg_keyword_with_specific_Arg_classes(self):
        # Create multiple "Arg" instances using different constructors, attributes or methods from Arg class
        arg_node = Arg(Name("test_arg_node"), Name("test_arg_node2"), Arg(name="test_arg_node3"))

        # Invoke "visit_Arg_keyword" function with "Arg" instances
        visit_Arg_keyword(arg_node)

        # Assert: Validate that no changes were made to the arg instances
        assert arg_node == Arg(Name("test_arg_node"), Name("test_arg_node2"), Arg(name="test_arg_node3"))
