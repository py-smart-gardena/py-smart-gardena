# py-smart-gardena

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/py-smart-gardena.svg)](https://badge.fury.io/py/py-smart-gardena)
[![Build Status](https://travis-ci.org/py-smart-gardena/py-smart-gardena.svg?branch=master)](https://travis-ci.org/py-smart-gardena/py-smart-gardena)
[![Python 3](https://pyup.io/repos/github/py-smart-gardena/py-smart-gardena/python-3-shield.svg)](https://pyup.io/repos/github/py-smart-gardena/py-smart-gardena/)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/b782f7b0573e4623b5a0fb3fa607a734)](https://www.codacy.com/gh/py-smart-gardena/py-smart-gardena?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=py-smart-gardena/py-smart-gardena&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/057e00063e8848e9b8a17ba892552e9f)](https://www.codacy.com/app/grm/py-smart-gardena?utm_source=github.com&utm_medium=referral&utm_content=grm/py-smart-gardena&utm_campaign=Badge_Coverage)
[![Updates](https://pyup.io/repos/github/py-smart-gardena/py-smart-gardena/shield.svg)](https://pyup.io/repos/github/py-smart-gardena/py-smart-gardena/)
[![Known Vulnerabilities](https://snyk.io/test/github/py-smart-gardena/py-smart-gardena/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/py-smart-gardena/py-smart-gardena?targetFile=requirements.txt)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![Downloads](https://pepy.tech/badge/py-smart-gardena)](https://pepy.tech/project/py-smart-gardena)

## Description

The **py-smart-gardena** library aims to provide python way to communicate with gardena smart systems and
all gardena smart equipments. Configuration of the equipement and inclusion has still
 to be done using the Gardena application or website.

## Support

**This project needs your support.**  
Gardena equipments are expensive, and I need to buy them in order to add support.
If you find this library useful and want to help me support more devices (or if you
just want to reward me for my spent time), you are very welcome !   
Your help is very much appreciated.

Here are the links if you want to show your support :  
<span class="badge-paypal"><a href="https://paypal.me/grmklein" title="Donate to this project using Paypal"><img src="https://img.shields.io/badge/paypal-donate-yellow.svg" alt="PayPal donate button" /></a></span>

You can also send me crypto using one of the following addresses :

Bitcoin (BTC) : 15k9HW17MU6JSTZZkbQ3YNxEtYF5yhBgNR

Ethereum (ETH) : 0x67afa7dc3882821e21f68e5ccd98f5c74b24295f

MONERO (XMR) : 4AyVQ9HEuphJiHHgnA7BwiPSAwgodzGtqGnyD7qbxqGta3UZJk7JNcx4VMaSmL6Sn5W8b14tyPzXmQAjZGK9jc89PWpYWxy

Thx for your support !

## Requirements

*   **Python 3.6+**

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
smart_system.authenticate()
smart_system.update_locations()
for location in smart_system.locations.values():
    smart_system.update_devices(location)
    pprint.pprint(location)
    for device in location.devices.values():
        pprint.pprint(device)

smart_system.start_ws(smart_system.locations['LOCATION_ID'])


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
