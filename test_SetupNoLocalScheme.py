import pytest
from os import environ
import setuptools
from setuptools_rust import Binding, RustExtension
from setup import no_local_scheme

class Test_SetupNoLocalScheme:

    def test_no_local_scheme_basic(self):
        # Arrange
        version_string = '1.0.2'

        # Act
        result = no_local_scheme(version_string)

        # Assert
        assert result == '', 'Basic functionality test failed. Expected: empty string, Got: {}'.format(result)

    def test_no_local_scheme_different_inputs(self):
        # Arrange
        version_strings = ['0.1', '2.0.1', '1.2.3.4', '']

        # Act & Assert
        for version in version_strings:
            result = no_local_scheme(version)
            assert result == '', 'Functionality with different inputs test failed for version: {}. Expected: empty string, Got: {}'.format(version, result)

    def test_no_local_scheme_no_input(self):
        # Arrange & Act
        # assert for TypeError when called without any arguments
        with pytest.raises(TypeError):
            no_local_scheme()

        assert True, 'No input test failed. The function did not raise an error as expected when called without any arguments.'
