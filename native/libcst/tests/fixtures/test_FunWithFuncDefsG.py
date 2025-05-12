import pytest
from fun_with_func_defs import g
from pytest import raises

# Defining the class which will include our unit tests
class Test_FunWithFuncDefsG:

    # Test scenario 1 : Verifying the default function behavior.
    @pytest.mark.smoke
    def test_default_function_behavior(self):
        try:
            g(5)  # provide a valid value
        except Exception as e:
            pytest.fail(f"test_default_function_behavior failed with exception - {e}")

    
    # Test scenario 2 : Verifying for non valid inputs.
    @pytest.mark.negative
    def test_g_with_nonvalid_inputs(self):
        with raises(NameError):  # Expected to raise NameError as input is undefined
            g(non_existent_variable)

    # Test scenario 3 : Checking function execution timing.
    @pytest.mark.performance
    def test_g_execution_time(self):
        max_allowed_time = 2  # TODO: Set maximum allowed time as per requirements
        start_time = time.time()

        g(complex_input)  # TODO: Replace complex_input with actual input

        end_time = time.time() - start_time
        assert end_time <= max_allowed_time, f"test_g_execution_time: Function took {end_time} seconds which is more than allowed time {max_allowed_time}"
