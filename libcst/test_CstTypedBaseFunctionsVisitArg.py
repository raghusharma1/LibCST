import pytest
from libcst import Arg
from _typed_visitor import visit_Arg 

class Test_CstTypedBaseFunctionsVisitArg:
    @pytest.mark.parametrize('arg', [
        Arg(value="test"),
        Arg(value=1234),
        Arg(value=555.555),
        Arg(value=False),
        Arg(value=['1', '2', '3']),
        Arg(value=('1', '2', '3')),
        Arg(value={'a': '1', 'b': '2', 'c': '3'}), 
    ]) 
    def test_visit_Arg_with_valid_node(self, arg):
        assert visit_Arg(arg) in {None, True, False}

    @pytest.mark.parametrize('arg', [
        Arg(value="test", star="*"),
        Arg(value="test", equal="="),
        Arg(value="test", comma=","), 
    ]) 
    def test_visit_Arg_with_node_containing_specific_properties(self, arg):
        assert visit_Arg(arg) in {None, True, False} 

    def test_visit_Arg_with_None(self):
        with pytest.raises(TypeError):
            visit_Arg(None)

    @pytest.mark.parametrize('arg', [
        [Arg(value="test"), Arg(value=1234), Arg(value=555.555), ],
        [Arg(value=False), Arg(value=['1', '2', '3']), Arg(value=('1', '2', '3'))],
        [Arg(value={'a': '1', 'b': '2', 'c': '3'}), Arg(value="test"), Arg(value=1234)]
    ]) 
    def test_visit_Arg_with_multiple_nodes(self, args):
        assert all(visit_Arg(arg) in {None, True, False} for arg in args)
