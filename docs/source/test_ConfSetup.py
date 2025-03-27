import pytest
from conf import setup
from unittest.mock import MagicMock, call

@pytest.mark.regression
def test_autodoc_process_signature_connection():
    # Arrange
    app = MagicMock()
    
    # Act
    setup(app)

    # Assert
    assert call.connect('autodoc-process-signature', strip_class_signature) in app.mock_calls

@pytest.mark.regression
def test_autodoc_process_docstring_connection():
    # Arrange
    app = MagicMock()
    
    # Act
    setup(app)
    
    # Assert
    assert call.connect('autodoc-process-docstring', strip_class_signature_docstring) in app.mock_calls

@pytest.mark.regression
def test_custom_css_file_addition():
    # Arrange
    app = MagicMock()

    # Act
    setup(app)
    
    # Assert
    assert call.add_css_file('custom.css') in app.mock_calls
