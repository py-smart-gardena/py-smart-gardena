# py-smart-gardena
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.org/grm/py-smart-gardena.svg?branch=master)](https://travis-ci.org/grm/py-smart-gardena)
[![Python 3](https://pyup.io/repos/github/grm/py-smart-gardena/python-3-shield.svg)](https://pyup.io/repos/github/grm/py-smart-gardena/)
[![Maintainability](https://api.codeclimate.com/v1/badges/e1931021997308c01056/maintainability)](https://codeclimate.com/github/grm/py-smart-gardena/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/e1931021997308c01056/test_coverage)](https://codeclimate.com/github/grm/py-smart-gardena/test_coverage)
[![codecov](https://codecov.io/gh/grm/py-smart-gardena/branch/master/graph/badge.svg)](https://codecov.io/gh/grm/py-smart-gardena)
[![Updates](https://pyup.io/repos/github/grm/py-smart-gardena/shield.svg)](https://pyup.io/repos/github/grm/py-smart-gardena/)
[![Known Vulnerabilities](https://snyk.io/test/github/grm/py-smart-gardena/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/grm/py-smart-gardena?targetFile=requirements.txt)
<a href="https://github.com/ambv/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)


## Description

This library aims to provide python way to communicate with gardena smart gateway and all smart gardena systems.

## Installation

```sh
$ pip install py-smart-gardena
```

## Usage

```python
from gardena.smart_system import SmartSystem
smart_system = SmartSystem(email="email@gardena.com", password="password")
smart_system.authenticate()

# To update locations (gardens, ..)
smart_system.update_locations()

for location in smart_system.locations:
   # To update devices information for a location (mower, gateway, sensor, ..)
    location.update_devices()
    #Iterate over gateways
    for gateway in location.gateways:
        print(gateway.name + "(" + gateway.id +")")
    #Iterate over mowers
    for mower in location.mowers:
        print(mower.name + "(" + mower.id +")")

```

## Development environment

```sh
$ pip install -e .[dev]
```


## Credits

This library would not have been possible without the work of :
* DXSdata (http://www.dxsdata.com/2016/07/php-class-for-gardena-smart-system-api/)
* Gerrieg (https://www.roboter-forum.com/index.php?thread/16777-gardena-smart-system-analyse/&l=2)