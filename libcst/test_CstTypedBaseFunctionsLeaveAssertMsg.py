import pytest
from libcst._nodes.statement import Assert
from libcst._visitors import CSTTypedBaseFunctions
from libcst._nodes.expression import SimpleString
from _typed_visitor import leave_Assert_msg

class Test_CstTypedBaseFunctionsLeaveAssertMsg:

  @pytest.mark.regression
  def test_leave_assert_msg_with_message(self):
    # Arrange
    node = Assert(test=SimpleString(value='"This is a test"'))

    cstTypedBaseFunctions = CSTTypedBaseFunctions()
    
    # Act
    try:
      cstTypedBaseFunctions.leave_Assert_msg(node)

    # Assert
    except Exception as e:
      pytest.fail(f"leave_Assert_msg() method failed with error: {e}")

  @pytest.mark.regression
  def test_leave_assert_msg_no_message(self):
    # Arrange
    node = Assert(test=SimpleString(value=''))

    cstTypedBaseFunctions = CSTTypedBaseFunctions()
    
    # Act
    try:
      cstTypedBaseFunctions.leave_Assert_msg(node)

    # Assert
    except Exception as e:
      pytest.fail(f"leave_Assert_msg() method failed with error: {e}")

  @pytest.mark.regression
  def test_leave_assert_msg_whitespace(self):
    # Arrange
    node = Assert(test=SimpleString(value=' \t  \n '))

    cstTypedBaseFunctions = CSTTypedBaseFunctions()
    
    # Act
    try:
      cstTypedBaseFunctions.leave_Assert_msg(node)

    # Assert
    except Exception as e:
      pytest.fail(f"leave_Assert_msg() method failed with error: {e}")
