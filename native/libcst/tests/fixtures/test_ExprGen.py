import pytest
from expr import gen

class Test_ExprGen:
    @pytest.mark.parametrize("subkey, type_args", [("1", [int]), ("string", ["int"])])
    def test_gen_returns_false(self, subkey, type_args):
        generator = gen()
        generator.send(None)
        result = generator.send((subkey, type_args))
        assert result is False, "Mismatched type should result in False"

    @pytest.mark.parametrize("values", [[1, 2, 3], ["a", "b", "c"], []])
    def test_gen_with_out_of_scope_generator(self, values):
        generator = gen()
        generator.send(None)
        generated_values = list(generator.send((values, [])))
        assert generated_values == values, "Values from outside_of_generator should be the same as rendered by gen"

    @pytest.mark.parametrize("inputs", [[1, 2, 3], ["a", "b", "c"], []])
    def test_gen_with_yield_a_b_c(self, inputs):
        generator = gen()
        generator.send(None)
        generated_values = [generator.send(([], [val])) for val in inputs]
        assert generated_values == inputs, "`a`, `b` and `c` should receive input values correctly"
