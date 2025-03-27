import pytest
import inspect
from _metadata_dependent import MetadataDependent, get_inherited_dependencies



@pytest.mark.valid
class Test_MetadataDependentGetInheritedDependencies:
    class A(MetadataDependent):
        METADATA_DEPENDENCIES = {"test"}

    class B(A):
        METADATA_DEPENDENCIES = {"test1"}

    class C(B):
        METADATA_DEPENDENCIES = {"test2"}

    class D:

        METADATA_DEPENDENCIES = {"test3"} 

    def test_inherited_metadata_functionality(self):
        result = get_inherited_dependencies(Test_MetadataDependentGetInheritedDependencies.C)
        assert result == {"test", "test1", "test2"}

    def test_inherited_metadata_caching(self):
        get_inherited_dependencies(Test_MetadataDependentGetInheritedDependencies.C)
        assert Test_MetadataDependentGetInheritedDependencies.C._INHERITED_METADATA_DEPENDENCIES_CACHE == {"test", "test1", "test2"}

        result = get_inherited_dependencies(Test_MetadataDependentGetInheritedDependencies.C)
        assert result == {"test", "test1", "test2"}

    def test_non_metadata_dependent_class(self):
        result = get_inherited_dependencies(Test_MetadataDependentGetInheritedDependencies.D)
        assert result == set()

    def test_duplicate_metadata_dependencies(self):
        class E(MetadataDependent):
            METADATA_DEPENDENCIES = {"test"}

        class F(E):
            METADATA_DEPENDENCIES = {"test"}

        result = get_inherited_dependencies(F)
        assert result == {"test"}

