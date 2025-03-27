import pytest
from tool import _default_config

class Test_ToolDefaultConfig:
    @pytest.mark.regression
    @pytest.mark.valid
    def test_default_config_values(self):
        """
        Validate Default Configuration.
        """
        expected_config = {
            "generated_code_marker": "@generated",
            "formatter": ["black", "-"],
            "blacklist_patterns": [],
            "modules": ["libcst.codemod.commands"],
            "repo_root": ".",
        }
        assert _default_config() == expected_config

    @pytest.mark.security
    @pytest.mark.valid
    def test_default_config_immutability(self):
        """
        Validate Immutability.
        """
        config_1 = _default_config()
        config_1["repo_root"] = "./new_root"
        config_2 = _default_config()
        assert config_1 != config_2

    @pytest.mark.regression
    @pytest.mark.invalid
    def test_default_config_keys(self):
        """
        Validate the Key Integrity.
        """
        expected_keys = ["generated_code_marker", "formatter", "blacklist_patterns", "modules", "repo_root"]
        config = _default_config()
        for key in expected_keys:
            assert key in config.keys()
