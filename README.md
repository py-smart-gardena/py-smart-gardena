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
        print("---> battery rechargeable status : " + mower.battery_status)
        print("---> battery charging : " + str(mower.battery_charging))
        print("---> radio quality : " + str(mower.radio_quality))
        print("---> radio connection status : " + mower.radio_connection_status)
        print("---> radio state : " + mower.radio_state)
        print("---> internal temperature : " + str(mower.internal_temperature))
        print("---> mower status : " + mower.mower_status)
        print("---> manual operation : " + str(mower.mower_manual_operation))
        print("---> timestamp next start : " + mower.mower_timestamp_next_start)

    # Iterate over sensors
    for sensor in location.sensors.values():
        print("-> sensor : " + sensor.name + "(" + sensor.id + ")")
        print("---> category : " + sensor.category)
        print(
            "---> is_configuration_synchronized : " +
            str(sensor.is_configuration_synchronized))
        print("---> serial number : " + sensor.serial_number)
        print("---> version : " + sensor.version)
        print("---> last time online : " + sensor.last_time_online)
        print("---> device state : " + sensor.device_state)
        print("---> battery level : " + str(sensor.battery_level))
        print("---> battery rechargeable status : " + sensor.battery_status)
        print("---> battery charging : " + str(sensor.battery_charging))
        print("---> radio quality : " + str(sensor.radio_quality))
        print("---> radio connection status : " + sensor.radio_connection_status)
        print("---> radio state : " + sensor.radio_state)
        print("---> ambient temperature : " + str(
            sensor.sensor_ambient_temperature))
        print("---> frost warning : " + sensor.sensor_frost_warning)
        print("---> soil temperature : " + str(sensor.sensor_soil_temperature))
        print("---> soil humidity : " + str(sensor.sensor_soil_humidity))
        print("---> light : " + str(sensor.sensor_light))
        print("---> firmware status : " + sensor.firmware_status)
    
```

## Development environment

```sh
$ pip install -e .[dev]
```


## Credits

This library would not have been possible without the work of :
* DXSdata (http://www.dxsdata.com/2016/07/php-class-for-gardena-smart-system-api/)
* Gerrieg (https://www.roboter-forum.com/index.php?thread/16777-gardena-smart-system-analyse/&l=2)