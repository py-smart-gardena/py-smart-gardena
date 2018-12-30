# py-smart-gardena
[![Build Status](https://travis-ci.org/grm/py-smart-gardena.svg?branch=master)](https://travis-ci.org/grm/py-smart-gardena)
[![Maintainability](https://api.codeclimate.com/v1/badges/e1931021997308c01056/maintainability)](https://codeclimate.com/github/grm/py-smart-gardena/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/e1931021997308c01056/test_coverage)](https://codeclimate.com/github/grm/py-smart-gardena/test_coverage)
[![codecov](https://codecov.io/gh/grm/py-smart-gardena/branch/master/graph/badge.svg)](https://codecov.io/gh/grm/py-smart-gardena)
[![Updates](https://pyup.io/repos/github/grm/py-smart-gardena/shield.svg)](https://pyup.io/repos/github/grm/py-smart-gardena/)
[![Python 3](https://pyup.io/repos/github/grm/py-smart-gardena/python-3-shield.svg)](https://pyup.io/repos/github/grm/py-smart-gardena/)
[![Known Vulnerabilities](https://snyk.io/test/github/grm/py-smart-gardena/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/grm/py-smart-gardena?targetFile=requirements.txt)

## Description

This library aims to provide python way to communicate with gardena smart gateway and all smart gardena systems.

## Installation

```sh
pip install py-smart-gardena
```

## Usage

```python
from gardena.gateway import Gateway
gw = Gateway(email="email@gardena.com", password="password")
gw.authenticate()

# To update locations (gérdens, ..)
gw.update_locations()
# To update devices (mower, gateway, sensor ..)
gw.update_devices()
```