# content of myinvoke.py
import pytest
import sys
import os
import pathlib

os.chdir("src")

class MyPlugin:
    def pytest_sessionfinish(self):
        print("*** test run reporting finishing")


if __name__ == "__main__":
    sys.path.append(
        os.getcwd()
    )


    sys.exit(pytest.main(["-q"], plugins=[MyPlugin()]))