import pytest
from typing import Tuple, List, Dict
from fun_with_func_defs import stars

class Test_FunWithFuncDefsStars:
    @pytest.mark.smoke
    def test_stars_no_args(self):
        # Act
        result = stars()

        # Assert
        assert result == (True, [], (), {})
    
    
    @pytest.mark.regression
    def test_stars_only_positional_args(self):
        # Arrange
        args = (False, [True, False, True])

        # Act
        result = stars(*args)

        # Assert
        assert result[0] == args[0]
        assert result[1] == args[1]
        assert result[2] == ()
        assert result[3] == {}
    
    
    @pytest.mark.regression
    def test_stars_only_keyword_args(self):
        # Arrange
        kwargs = {"kw1": 1, "kw2": 2}
        
        # Act
        result = stars(**kwargs)

        # Assert
        assert result[0] == True
        assert result[1] == []
        assert result[2] == ()
        assert result[3] == kwargs
    
    
    @pytest.mark.performance
    def test_stars_full_args(self):
        # Arrange
        args = (False, [True, False, True])
        kwargs = {"kw1": 1, "kw2": 2}

        # Act
        result = stars(*args, **kwargs)
        
        # Assert
        assert result[0] == args[0]
        assert result[1] == args[1]
        assert result[2] == ()
        assert result[3] == kwargs
