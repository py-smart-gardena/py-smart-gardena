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

smart_system = SmartSystem(email="test@test.com", password="password")
smart_system.authenticate()

# To update locations (gardens, ..)
smart_system.update_locations()

for location in smart_system.locations.values():
    print("location : " + location.name + "(" + location.id + ")")
    print("-> latitude : " + str(location.latitude))
    print("-> longitude : " + str(location.longitude))
    print("-> address : " + location.address)
    print("-> city : " + location.city)
    print("-> sunrise : " + location.sunrise)
    print("-> sunset : " + location.sunset)
    print("-> time zone : " + location.time_zone)
    print("-> time zone offset : " + str(location.time_zone_offset))

    # To update devices information for a location (mower, gateway, sensor, ..)
    location.update_devices()
    # Iterate over gateways
    for gateway in location.gateways.values():
        print("-> gateway : " + gateway.name + "(" + gateway.id + ")")
        print("---> category : " + gateway.category)
        print("---> description : " + gateway.description)
        print("---> is_configuration_synchronized : " + str(
            gateway.is_configuration_synchronized))
        print("---> serial number : " + gateway.serial_number)
        print("---> version : " + gateway.version)
        print("---> last time online : " + gateway.last_time_online)
        print("---> ip address : " + gateway.ip_address)
        print("---> timezone : " + gateway.timezone)
        print("---> device state : " + gateway.device_state)

    # Iterate over mowers
    for mower in location.mowers:
        print("-> mower : " + mower.name + "(" + mower.id + ")")
        print("---> category : " + mower.category)
        print("---> description : " + mower.description)
        print(
            "---> is_configuration_synchronized : " +
            str(mower.is_configuration_synchronized))
        print("---> serial number : " + mower.serial_number)
        print("---> version : " + mower.version)
        print("---> last time online : " + mower.last_time_online)
        print("---> battery level : " + str(mower.battery_level))
        print("---> battery rechargeable status : " + mower
              .battery_rechargable_status)
        print("---> battery charging : " + str(mower.battery_charging))
        print("---> radio quality : " + str(mower.radio_quality))
        print("---> radio connection status : " + mower.radio_connection_status)
        print("---> radio state : " + mower.radio_state)
        print("---> internal temperature : " + str(mower.internal_temperature))

```

## Development environment

```sh
$ pip install -e .[dev]
```


## Credits

This library would not have been possible without the work of :
* DXSdata (http://www.dxsdata.com/2016/07/php-class-for-gardena-smart-system-api/)
* Gerrieg (https://www.roboter-forum.com/index.php?thread/16777-gardena-smart-system-analyse/&l=2)