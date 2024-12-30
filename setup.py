import setuptools
from os.path import splitext, basename
from glob import glob

import versioneer

with open("README.md", "r") as fh:
    long_description = fh.read()

tests_require = []


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
    install_requires=["requests", "websockets", "httpx", "authlib", "backoff"],
    setup_requires=["pytest-runner"],
    tests_require=tests_require,
    py_modules={splitext(basename(path))[0] for path in glob("src/*py")},
    license="MIT",
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    extras_require={
        "test": ["pytest>=6.0", "coverage", "pytest-cov", "requests_mock"],
        "dev": ["pre-commit"]
    },
)
