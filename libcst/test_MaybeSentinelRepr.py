import pytest
from enum import auto, Enum

# Assuming _maybe_sentinel is the mention class and its file
from _maybe_sentinel import MaybeSentinel

class Test_MaybeSentinelRepr:
    
    class CustomObj:
        def __repr__(self):
            return 'CustomObj()'
    
    class EnumObj(Enum):
        TEST = auto()
    
    @pytest.mark.regression
    def test_repr_for_normal_object(self):
        # Arrange
        normal_object = MaybeSentinel()
        
        # Act
        result = repr(normal_object)
        
        # Assert
        assert result == str(normal_object)
        
    @pytest.mark.regression
    def test_repr_for_enum_object(self):
        # Arrange
        enum_object = self.EnumObj.TEST
        
        # Act
        result = repr(enum_object)
        
        # Assert
        assert result == 'EnumObj.TEST'
        
    @pytest.mark.regression
    def test_repr_for_object_with_own_repr(self):
        # Arrange
        custom_object = self.CustomObj()
        
        # Act
        result = repr(custom_object)
        
        # Assert
        assert result == 'CustomObj()'
