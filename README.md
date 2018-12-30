# py-smart-gardena
<a href="https://codeclimate.com/github/grm/py-smart-gardena/maintainability"><img src="https://api.codeclimate.com/v1/badges/e1931021997308c01056/maintainability" /></a>
<a href="https://codeclimate.com/github/grm/py-smart-gardena/test_coverage"><img src="https://api.codeclimate.com/v1/badges/e1931021997308c01056/test_coverage" /></a>
[![Updates](https://pyup.io/repos/github/grm/py-smart-gardena/shield.svg)](https://pyup.io/repos/github/grm/py-smart-gardena/)
[![Python 3](https://pyup.io/repos/github/grm/py-smart-gardena/python-3-shield.svg)](https://pyup.io/repos/github/grm/py-smart-gardena/)


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