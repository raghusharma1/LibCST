import os
import pytest
from tool import _ListSerializer

class Test_ListSerializerSerializeImpl:
    @pytest.mark.negative
    def test_serialize_impl_non_list(self):
        non_list_serializer = _ListSerializer('Test Comment')
        with pytest.raises(Exception) as e_info:
            non_list_serializer._serialize_impl('test_key', 'not_a_list')
        assert str(e_info.value) == "Can only serialize lists!"

    @pytest.mark.positive
    def test_serialize_impl_list_newlines_true(self):
        list_serializer = _ListSerializer('Test Comment', newlines=True)
        result = list_serializer._serialize_impl('test_key', ['a', 'b', 'c'])
        expected_output = f"test_key:{os.linesep}- 'a'{os.linesep}- 'b'{os.linesep}- 'c'"
        assert result == expected_output, 'The function does not correctly serialize lists when newlines is true.'

    @pytest.mark.positive
    def test_serialize_impl_list_newlines_false(self):
        list_serializer = _ListSerializer('Test Comment', newlines=False)
        result = list_serializer._serialize_impl('test_key', ['x', 'y', 'z'])
        expected_output = "test_key: ['x', 'y', 'z']"
        assert result == expected_output, 'The function does not correctly serialize lists when newlines is false.'
