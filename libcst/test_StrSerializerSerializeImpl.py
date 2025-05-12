import pytest
from tool import _serialize_impl

class Test_StrSerializerSerializeImpl:
    
    @pytest.mark.parametrize("key,value,expected_output",[("%#@!*&","+123?","'%#@!*&': '+123?'"),("?><:!/@|","[1,2,3]","'><:!/@|': '[1,2,3]'")])
    def test_serialize_impl_non_alnum_key(self, key, value, expected_output):
        output = _serialize_impl(key, value)
        assert output == expected_output, f"For non alphanumeric key {key} and value {value}, expected output is {expected_output} but got {output}"

    @pytest.mark.parametrize("key,value,expected_output",[("Key1",[1,2,3],"Key1: [1,2,3]"),("Key2",(1,2),"Key2: (1,2)"),("Key3",{'abc':123},"Key3: {'abc': 123}")])
    def test_serialize_impl_with_different_datatypes_value(self, key, value, expected_output):
        output = _serialize_impl(key, value)
        assert output == expected_output, f"For key {key} and non-primitive data type value {value}, expected output is {expected_output} but got {output}"

    @pytest.mark.parametrize("key,value,expected_output",[("Key1",None,"Key1: None")])
    def test_serialize_impl_with_null_value(self, key, value, expected_output):
        output = _serialize_impl(key, value)
        assert output == expected_output, f"For key {key} and NULL value, expected output is {expected_output} but got {output}"

    @pytest.mark.parametrize("key,value,expected_output",[("JSON","",'JSON': ''')])
    def test_serialize_impl_with_empty_string_value(self, key, value, expected_output):
        output = _serialize_impl(key, value)
        assert output == expected_output, f"For key {key} and emtpy string value, expected output is {expected_output} but got {output}"
