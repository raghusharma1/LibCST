import os
import textwrap
import pytest
from tool import _SerializerBase

class Test_SerializerBaseSerialize:

    @pytest.mark.positive
    def test_serialize_with_valid_input():
        serializer = _SerializerBase("Valid comment.")
        key, value = "TestKey", "TestValue"
        expected_output = "# Valid comment.\nTestKey: TestValue\n"
        assert serializer.serialize(key, value) == expected_output

    @pytest.mark.positive
    def test_serialize_with_multiline_comment():
        multiline_comment = "This comment string is long enough to be wrapped into multiple lines."
        serializer = _SerializerBase(multiline_comment)
        key, value = "TestKey", "TestValue"
        wrapped_comments = os.linesep.join(f"# {comment}" for comment in textwrap.wrap(multiline_comment))
        expected_output = f"{wrapped_comments}\n{key}: {value}\n"
        assert serializer.serialize(key, value) == expected_output
    
    @pytest.mark.negative
    def test_serialize_with_empty_comment():
        serializer = _SerializerBase("")
        key, value = "TestKey", "TestValue"
        expected_output = f"\n{key}: {value}\n"
        assert serializer.serialize(key, value) == expected_output

    @pytest.mark.negative
    def test_serialize_with_null_value():
        serializer = _SerializerBase("A comment with null value.")
        key, value = "TestKey", None
        expected_output = "# A comment with null value.\nTestKey: None\n"
        assert serializer.serialize(key, value) == expected_output
