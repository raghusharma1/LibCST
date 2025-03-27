import os
import pytest
import tempfile
from tool import _recursive_find
from typing import List, Tuple

class Test_ToolRecursiveFind:

    @pytest.mark.positive
    def test_recursive_find_valid_case(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            # Arrange: Prepare the directory structure
            sub_dir = os.path.join(temp_dir, 'sub_dir')
            os.mkdir(sub_dir)
            with open(os.path.join(temp_dir, 'test1.py'), 'w') as _:
                pass
            with open(os.path.join(sub_dir, 'test2.py'), 'w') as _:
                pass

            # Act: Call _recursive_find
            modules: List[Tuple[str, object]] = _recursive_find(temp_dir, 'temp_dir')

            # Assert: Function should correctly identify Python files in dir and its subdirs
            module_names = [module_name for module_name, _ in modules]
            assert '.test1' in module_names
            assert 'sub_dir.test2' in module_names

    @pytest.mark.negative
    def test_recursive_find_invalid_case(self):
        # Act and Assert: Function should not crash when supplied with invalid dir path
        with pytest.raises(FileNotFoundError):
            _recursive_find('/nonexisting_directory/', 'non_existing_module')

    @pytest.mark.performance
    def test_recursive_find_performance(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            # Arrange: Create large quantity of Python files in the directory
            for i in range(50000):
                with open(os.path.join(temp_dir, f'test{i}.py'), 'w') as _:
                    pass

            # Act: Monitor function execution using timeit
            runtime = pytest.approx(_recursive_find(temp_dir, 'temp_dir'), 50000, rel=1e-6)

            # Assert: Function should execute in a reasonable time
            assert runtime > 0 and runtime <= 2.0
