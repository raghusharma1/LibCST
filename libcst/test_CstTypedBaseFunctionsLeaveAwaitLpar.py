import pytest
import threading
from libcst._nodes.expression import Await, Attribute

@pytest.mark.regression
def test_leave_Await_lpar_with_generic_Await():
    from _typed_visitor import leave_Await_lpar
    # Arrange
    await_node = Await()
    # Act
    try:
        leave_Await_lpar(await_node)
    # Assert
    except Exception as e:
        pytest.fail(f"Unexpected Exception raised: {e}")

@pytest.mark.regression
def test_leave_Await_lpar_in_structure():
    from _typed_visitor import leave_Await_lpar
    # Arrange
    attribute_node = Attribute(Await(), 'value')
    await_node = attribute_node.value
    # Act
    try:
        leave_Await_lpar(await_node)
    # Assert
    except Exception as e:
        pytest.fail(f"Unexpected Exception raised: {e}")

@pytest.mark.performance
def test_leave_Await_lpar_concurrent_calls():
    from _typed_visitor import leave_Await_lpar
    # Arrange
    await_nodes = [Await() for _ in range(100)]
    # Act
    def call_function():
        try:
            for node in await_nodes:
                leave_Await_lpar(node)
        except Exception as e:
            pytest.fail(f"Unexpected Exception raised: {e}")
            
    threads = [threading.Thread(target=call_function) for _ in range(10)]
    for t in threads:
        t.start()
    # Assert
    for t in threads:
        t.join()

@pytest.mark.regression
def test_leave_Await_lpar_with_node_variants():
    from _typed_visitor import leave_Await_lpar
    # Arrange
    variants = [Await(), Attribute(Await(), 'value'), Await(), Attribute(Await(), 'value')]
    # Act
    try:
        for variant in variants:
            if isinstance(variant, Attribute):
                leave_Await_lpar(variant.value)
            else:
                leave_Await_lpar(variant)
    # Assert
    except Exception as e:
        pytest.fail(f"Unexpected Exception raised: {e}")
