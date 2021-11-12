# content of myinvoke.py
import os
import sys

import pytest

os.chdir("cbaxter1988_utils")


class MyPlugin:
    def pytest_sessionfinish(self):
        print("*** test run reporting finishing")


if __name__ == "__main__":
    sys.path.append(
        os.getcwd()
    )

    sys.exit(pytest.main(["-q"], plugins=[MyPlugin()]))
