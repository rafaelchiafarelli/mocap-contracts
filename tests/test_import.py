from importlib.metadata import version

import mocap_contracts


def test_package_imports_with_installed_version():
    assert mocap_contracts.__version__ == version("mocap-contracts") == "0.0.1"
