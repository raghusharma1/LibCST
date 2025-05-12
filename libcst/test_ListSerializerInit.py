import pytest
from tool import _ListSerializer

class Test_ListSerializerInit:
    
    @pytest.mark.valid
    def test_newlines_false(self):
        # Arrange: Initialize arbitrary comment string.
        comment = 'test comment'
        
        # Act: Create an instance of the class, passing the comment string as an argument and setting newlines as False.
        list_serializer = _ListSerializer(comment, newlines=False)
        
        # Assert: Assert if instance variables 'comment' and 'newlines' are correctly set.
        assert list_serializer.comment == comment 
        assert list_serializer.newlines == False 

    @pytest.mark.valid
    def test_newlines_true(self):
        # Arrange: Initialize arbitrary comment string.
        comment = 'test comment'
        
        # Act: Create an instance of the class, passing the comment string as an argument and setting newlines as True.
        list_serializer = _ListSerializer(comment, newlines=True)
        
        # Assert: Assert if instance variables 'comment' and 'newlines' are correctly set.
        assert list_serializer.comment == comment 
        assert list_serializer.newlines == True

    @pytest.mark.valid
    def test_no_newlines_parameter(self):
        # Arrange: Initialize arbitrary comment string.
        comment = 'test comment'
        
        # Act: Create an instance of the class, passing the comment string as an argument only.
        list_serializer = _ListSerializer(comment)
        
        # Assert: Assert if instance variables 'comment' and 'newlines' are correctly set.
        assert list_serializer.comment == comment 
        assert list_serializer.newlines == False 
