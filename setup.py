import setuptools
from os.path import splitext, basename
from glob import glob
from subprocess import check_output

import versioneer

with open("README.md", "r") as fh:
    long_description = fh.read()

tests_require = ["pytest>=3.6", "coverage", "pytest-cov", "requests_mock"]


setuptools.setup(
    name="py-smart-gardena",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Jérémie Klein",
    author_email="grm.klein@gmail.com",
    description="This library aims to provide python way to communicate "
    "with gardena smart gateway and all smart gardena systems.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/grm/py-smart-gardena",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    install_requires=["requests", "oauthlib", "requests_oauthlib", "websocket-client"],
    setup_requires=["pytest-runner"],
    tests_require=tests_require,
    extras_require={"dev": ["pre-commit"]},
    py_modules={splitext(basename(path))[0] for path in glob("src/*py")},
    license="MIT",
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
