# py-smart-gardena

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/py-smart-gardena.svg)](https://badge.fury.io/py/py-smart-gardena)
[![Build Status](https://travis-ci.org/py-smart-gardena/py-smart-gardena.svg?branch=master)](https://travis-ci.org/py-smart-gardena/py-smart-gardena)
[![Python 3](https://pyup.io/repos/github/py-smart-gardena/py-smart-gardena/python-3-shield.svg)](https://pyup.io/repos/github/py-smart-gardena/py-smart-gardena/)
[![Updates](https://pyup.io/repos/github/py-smart-gardena/py-smart-gardena/shield.svg)](https://pyup.io/repos/github/py-smart-gardena/py-smart-gardena/)
[![Known Vulnerabilities](https://snyk.io/test/github/py-smart-gardena/py-smart-gardena/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/py-smart-gardena/py-smart-gardena?targetFile=requirements.txt)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

Feel free to join the discord server : [![Support Server](https://img.shields.io/discord/853252789522268180.svg?color=7289da&label=Discord&logo=discord&style=flat-square)](https://discord.gg/59sFjykS)

## Description

The **py-smart-gardena** library aims to provide python way to communicate with gardena smart systems and
all gardena smart equipment. Configuration of the equipement and inclusion has still
 to be done using the Gardena application or website.

## Support

**This project needs your support.**  
Gardena equipments are expensive, and I need to buy them in order to add support.
If you find this library useful and want to help me support more devices (or if you
just want to reward me for my spent time), you are very welcome !   
Your help is very much appreciated.

Here are the links if you want to show your support :  
<span class="badge-paypal"><a href="https://paypal.me/grmklein" title="Donate to this project using Paypal"><img src="https://img.shields.io/badge/paypal-donate-yellow.svg" alt="PayPal donate button" /></a></span>

Thx for your support !

## Requirements

*   **Python 3.8+**

## Supported devices

For now, only few devices are supported. I may add new ones in the future :  
*   Gateway
*   Smart Mower
*   Smart water control
*   Smart sensor
*   Power plugs
*   Smart Irrigation control

## Account creation in order to have access to Gardena API

Gardena requires the creation of an account and an application in order to use their API.
You can find how to create such an account and application here : <a href="https://developer.husqvarnagroup.cloud/docs/getting-started#/docs/getting-started/#3connect-api-to-application">Account and application creation</a>

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

You first need to get a client id (also called application key in the
API documentation) for your personal installation of gardena.  To do
so, create an account here : https://developer.husqvarnagroup.cloud/

Then you need to create an application, add APIs (Authentication API
and GARDENA smart system API), and copy the application key as
explained here: https://developer.husqvarnagroup.cloud/docs/getting-started

The library manages the token for you then.
An exception is raised if authentication fails.

```python
from gardena.smart_system import SmartSystem
import pprint

smart_system = SmartSystem(email="email@gmail.com", password="my_password", client_id="client_id")
await smart_system.authenticate()
await smart_system.update_locations()
for location in smart_system.locations.values():
    await smart_system.update_devices(location)
    pprint.pprint(location)
    for device in location.devices.values():
        pprint.pprint(device)

await smart_system.start_ws(smart_system.locations['LOCATION_ID'])


```
Once authentication is successful, you need to gather locations and devices for the first time and then, you can create start the websocket in order to get updates automatically.

### Locations

Locations are automatically retrieved the first time from the API, and then the websocket is used to get updates.

Here is the list of the current available fields and methods :

```python

for location in smart_system.locations.values():
    print("location : " + location.name + "(" + location.id + ")")

```

### Devices

Devices are automatically retrieved the first time from the API, and then the websocket is used to get updates. They are stored in each locations. Depending on the function type, you can have diffrents fields.

#### Mowers

```python
    for device in smart_system.locations["LOCATION_ID"].find_device_by_type("MOWER"):
          print(f"name : {device.name}")
          print(f"id : {device.id}")
          print(f"type : {device.type}")
          print(f"model_type : {device.model_type}")
          print(f"battery_level : {device.battery_level}")
          print(f"battery_state : {device.battery_state}")
          print(f"rf_link_level : {device.rf_link_level}")
          print(f"rf_link_state : {device.rf_link_state}")
          print(f"serial : {device.serial}")
          print(f"activity : {device.activity}")
          print(f"operating_hours : {device.operating_hours}")
          print(f"state : {device.state}")
          print(f"last_error_code : {device.last_error_code}")
```

#### Power Socket

```python
    for device in smart_system.locations["LOCATION_ID"].find_device_by_type("POWER_SOCKET"):
          print(f"name : {device.name}")
          print(f"id : {device.id}")
          print(f"type : {device.type}")
          print(f"model_type : {device.model_type}")
          print(f"battery_level : {device.battery_level}")
          print(f"battery_state : {device.battery_state}")
          print(f"rf_link_level : {device.rf_link_level}")
          print(f"rf_link_state : {device.rf_link_state}")
          print(f"serial : {device.serial}")
          print(f"activity : {device.activity}")
          print(f"state : {device.state}")
```

#### Sensor

```python
    for device in smart_system.locations["LOCATION_ID"].find_device_by_type("SENSOR"):
          print(f"name : {device.name}")
          print(f"id : {device.id}")
          print(f"type : {device.type}")
          print(f"model_type : {device.model_type}")
          print(f"battery_level : {device.battery_level}")
          print(f"battery_state : {device.battery_state}")
          print(f"rf_link_level : {device.rf_link_level}")
          print(f"rf_link_state : {device.rf_link_state}")
          print(f"serial : {device.serial}")
          print(f"ambient_temperature : {device.ambient_temperature}")
          print(f"light_intensity : {device.light_intensity}")
          print(f"soil_humidity : {device.soil_humidity}")
          print(f"soil_temperature : {device.soil_temperature}")

```

#### Smart irrigation control

```python
    for device in smart_system.locations["LOCATION_ID"].find_device_by_type("SMART_IRRIGATION_CONTROL"):
          print(f"name : {device.name}")
          print(f"id : {device.id}")
          print(f"type : {device.type}")
          print(f"model_type : {device.model_type}")
          print(f"battery_level : {device.battery_level}")
          print(f"battery_state : {device.battery_state}")
          print(f"rf_link_level : {device.rf_link_level}")
          print(f"rf_link_state : {device.rf_link_state}")
          print(f"serial : {device.serial}")
          print(f"valve_set_id : {device.valve_set_id}")
          print(f"valve_set_state : {device.valve_set_state}")
          print(f"valve_set_last_error_code : {device.valve_set_last_error_code}")
          for valve in device.valves.values():
            print(f"name : {valve['name']}")
            print(f"{valve['name']} - id : {valve['id']}")
            print(f"{valve['name']} - activity : {valve['activity']}")
            print(f"{valve['name']} - state : {valve['state']}")
            print(f"{valve['name']} - last_error_code : {valve['last_error_code']}")
```

#### Smart water control

```python
    for device in smart_system.locations["LOCATION_ID"].find_device_by_type("WATER_CONTROL"):
          print(f"name : {device.name}")
          print(f"id : {device.id}")
          print(f"type : {device.type}")
          print(f"model_type : {device.model_type}")
          print(f"battery_level : {device.battery_level}")
          print(f"battery_state : {device.battery_state}")
          print(f"rf_link_level : {device.rf_link_level}")
          print(f"rf_link_state : {device.rf_link_state}")
          print(f"serial : {device.serial}")
          print(f"valve_set_id : {device.valve_set_id}")
          print(f"valve_name : {device.valve_name}")
          print(f"valve_id : {device.valve_id}")
          print(f"valve_activity : {device.valve_activity}")
          print(f"valve_state : {device.valve_state}")
```

### Using websocket

Once the websocket has been started, everything is managed and the devices are 
automatically updated once their state change.
In order for your to be alerted of such a change, you need to add a callback to the 
device.
This callback will be called each time the device state changed :

```python
def my_callback(device):
    print(f"The device {device.name} has been updated !")

device.add_callback(my_callback)

```

## Development environment

To install the dev environment, you just have to do, in the source code directory :

```sh
$ pip install -e .[dev]
```
