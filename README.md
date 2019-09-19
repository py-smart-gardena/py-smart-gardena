# py-smart-gardena

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/py-smart-gardena.svg)](https://badge.fury.io/py/py-smart-gardena)
[![Build Status](https://travis-ci.org/grm/py-smart-gardena.svg?branch=master)](https://travis-ci.org/grm/py-smart-gardena)
[![Python 3](https://pyup.io/repos/github/grm/py-smart-gardena/python-3-shield.svg)](https://pyup.io/repos/github/grm/py-smart-gardena/)
[![Maintainability](https://api.codeclimate.com/v1/badges/e1931021997308c01056/maintainability)](https://codeclimate.com/github/grm/py-smart-gardena/maintainability)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/057e00063e8848e9b8a17ba892552e9f)](https://www.codacy.com/app/grm/py-smart-gardena?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=grm/py-smart-gardena&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/057e00063e8848e9b8a17ba892552e9f)](https://www.codacy.com/app/grm/py-smart-gardena?utm_source=github.com&utm_medium=referral&utm_content=grm/py-smart-gardena&utm_campaign=Badge_Coverage)
[![Test Coverage](https://api.codeclimate.com/v1/badges/e1931021997308c01056/test_coverage)](https://codeclimate.com/github/grm/py-smart-gardena/test_coverage)
[![codecov](https://codecov.io/gh/grm/py-smart-gardena/branch/master/graph/badge.svg)](https://codecov.io/gh/grm/py-smart-gardena)
[![Updates](https://pyup.io/repos/github/grm/py-smart-gardena/shield.svg)](https://pyup.io/repos/github/grm/py-smart-gardena/)
[![Known Vulnerabilities](https://snyk.io/test/github/grm/py-smart-gardena/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/grm/py-smart-gardena?targetFile=requirements.txt)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![Downloads](https://pepy.tech/badge/py-smart-gardena)](https://pepy.tech/project/py-smart-gardena)

## Description

This library aims to provide python way to communicate with gardena smart systems and
all gardena smart equipments. Configuration of the equipement and inclusion has still
 to be done using the Gardena application or web site.
For now, this library only supports retrieving information, it should soon be able ot
 interact with devices to integrate in your automation system.

## Support

**This project needs your support.**  
Gardena equipments are expensive, and I need to buy them in order to add support.
If you find this library useful and want to help me support more devices (or if you
just want to reward me for my spent time), you are very welcome !   
Your help is very much appreciated.

Here are the links if you want to show your support :  
<span class="badge-paypal"><a href="https://paypal.me/grmklein" title="Donate to this project using Paypal"><img src="https://img.shields.io/badge/paypal-donate-yellow.svg" alt="PayPal donate button" /></a></span>

## Requirements

*   **Python 3.6+**

## Supported devices

For now, only few devices are supported. I may add new ones in the future :  
*   Gateway
*   Smart Mower (not tested yet)
*   Smart water control
*   Smart sensor
*   Power plugs

## Installation

```sh
$ pip install py-smart-gardena
```

## Usage

### Data model

The entrypoint of the library is the the SmartSytem class (in gardena.smart_system
package).
From there, you can get all locations from your account, and for each of these
locations, get the declared devices.

All communications are not done directly with the gateway. This library uses a websocket in order
to communicate with gardena systems in order to avoid throttling. There is only one connection to authenticate,
and two connections to revoke tokens, everything else is done through websockets.

### Authentication

You need to authenticate with your email and passwords created on this [site]
(https://developer.1689.cloud/apis) or the IOS/Android application.
The library manages the token for you then.
An exception is raised if authentication fails.

```python
from gardena.smart_system import SmartSystem

smart_system = SmartSystem(email="email@gmail.com", password="my_password", client_id="client_id")
smart_system.authenticate()

```
Once authentication is successful, infromations are sent asynchronously
from Gardena system to this library.

### Locations

Locations are the places where the devices are connected. It can be used to manage
 different gardens or different places from one garden, or both.
 Locations are

Here is the list of the current available fields and methods :

```python

for location in smart_system.locations.values():
    print("location : " + location.data["name"] + "(" + location.data["id"] + ")")

```

### Devices

Devices are automatically retrieved from the Websocket.

```python
    for location in smart_system.locations["location_id"].devices.values():
        locations.update_devices()
```

## Development environment

To install the dev environment, you just have to do, in the source code directory :

```sh
$ pip install -e .[dev]
```
