"""Configuration for the pytest test suite."""
pytest_plugins = [
    "tests.gardena.infrastructure.api.gardena.fixtures",
]

# import sys
# import os
# sys.path.append(os.path.abspath('../src'))
#
# from setuptools import find_packages, setup
#
#
# setup(
#     package_dir={'': 'src'},
#     packages=find_packages(where='src'),
# )
