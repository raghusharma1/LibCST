import threading
import pytest
from _typed_visitor import visit_BitAndAssign_whitespace_after
from libcst._nodes.op import BitAndAssign

@pytest.mark.parametrize("CurrentEnvironment, CurrentVariables", [(dict(), dict())])
def test_NoSideEffect(CurrentEnvironment, CurrentVariables):
    BeforeEnvironment = CurrentEnvironment.copy()
    visit_BitAndAssign_whitespace_after()
    assert CurrentEnvironment == BeforeEnvironment, "Test Failed: The function has side effects!"

def test_ReturnType():
    assert visit_BitAndAssign_whitespace_after() == None, "Test Failed: The return type is not None!"

def threaded_function():
    try:
        visit_BitAndAssign_whitespace_after()
    except:
        return 1
    return 0

def test_Multithreaded():
    threads = []
    for i in range(5):
        t = threading.Thread(target=threaded_function)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    assert all([t == 0 for t in threads]), "Test Failed: The function is not safe to be called from multiple threads!"

class Subclass_BitAndAssign(BitAndAssign):
     pass

def test_SubclassBitAndAssign():
    obj = Subclass_BitAndAssign()
    try:
        visit_BitAndAssign_whitespace_after(obj)
    except:
        pytest.fail("Test Failed: Function does not handle subclasses of BitAndAssign!")
