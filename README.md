# SolarEdge Interface
[![PyPi](https://img.shields.io/pypi/v/solaredge-interface.svg)](https://pypi.python.org/pypi/solaredge-interface/)
[![Python Versions](https://img.shields.io/pypi/pyversions/solaredge-interface.svg)](https://github.com/ndejong/solaredge-interface/)
[![Build Status](https://api.travis-ci.org/ndejong/solaredge-interface.svg?branch=master)](https://travis-ci.org/ndejong/solaredge-interface/)
[![Read the Docs](https://img.shields.io/readthedocs/solaredge-interface)](https://solaredge-interface.readthedocs.io)
![License](https://img.shields.io/github/license/ndejong/solaredge-interface.svg)

The SolarEdge Interface provides both a command-line interface and a Python module interface to interact with 
the SolarEdge API service.

## Features
* All (documented) SolarEdge API endpoints are implemented with multisite support for endpoints that provide 
  multisite queries.
* Response data for all endpoints are available as a Python-dict structure; a Pandas-DataFrame or; as raw-JSON.
* The command-line interface output can be formatted as a CSV; as a Pandas style JSON structure or; as plain-JSON.
* Timestamps can be returned as `datetime` values with their respective site timezones applied.  Doing so is the 
  default behaviour, however this can be disabled if required.
* Configuration via environment variables or config file is possible, thus making it safer to manage your API 
  key value(s).
* Decent debug logging to help detect and discover problems should they arise.
* Easy installation using PyPI `pip`
* Plenty of documentation and examples - https://solaredge-interface.readthedocs.io

## Installation
```shell
user@computer:~$ pip3 install solaredge-interface
```

## Command Line Usage
For example, obtain the current power flow at site 1234567.  This assumes the API_KEY has been set using the 
`SOLAREDGE_API_KEY` environment variable; alternatively use the `--config` command parameter to load a 
configuration file.  Response data in CSV format for all sub-commands can be achieved by adding `--format csv`
```shell
user@computer:~$ solaredge-interface site_current_power_flow 1234567
{
  "siteCurrentPowerFlow": {
    "updateRefreshRate": 3,
    "unit": "kW",
    "connections": [
      {
        "from": "GRID",
        "to": "Load"
      }
    ],
    "GRID": {
      "status": "Active",
      "currentPower": 0.7
    },
    "LOAD": {
      "status": "Active",
      "currentPower": 0.7
    },
    "PV": {
      "status": "Idle",
      "currentPower": 0.0
    }
  }
}
```

Plenty more command-line examples [available here](https://solaredge-interface.readthedocs.io/en/latest/docs/command-line/examples/).

## Python Module Usage
```python
Python 3.8.5 (default, Jul 28 2020, 12:59:40) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> from solaredge_interface.api.SolarEdgeAPI import SolarEdgeAPI
>>> api = SolarEdgeAPI(api_key='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', datetime_response=True, pandas_response=True)
>>> response = api.get_site_current_power_flow(1234567)
>>> response.data
{'siteCurrentPowerFlow': {'updateRefreshRate': 3, 'unit': 'kW', 'connections': [{'from': 'GRID', 'to': 'Load'}], 'GRID': {'status': 'Active', 'currentPower': 0.7}, 'LOAD': {'status': 'Active', 'currentPower': 0.7}, 'PV': {'status': 'Idle', 'currentPower': 0.0}}}
>>>
```

Additional Python-module examples are available in the [python-modules](https://solaredge-interface.readthedocs.io/en/latest/docs/python-modules/) pages.

## History
This project started as a fork from EnergieID which was renamed to solaredge-interface because it was heavily 
re-worked and extended in a way that is not compatible with previous forks.
* 2020-10-11 - forked to [ndejong/solaredge-interface](https://github.com/ndejong/solaredge-interface)
* 2018-01-26 - forked to [EnergieID/solaredge](https://github.com/EnergieID/solaredge)
* 2017-11-28 - original [bertouttier/solaredge](https://github.com/bertouttier/solaredge)

## Project
* Github - [github.com/ndejong/solaredge-interface](https://github.com/ndejong/solaredge-interface)
* PyPI - [pypi.python.org/pypi/solaredge-interface](https://pypi.python.org/pypi/solaredge-interface/)
* TravisCI - [travis-ci.org/github/ndejong/solaredge-interface](https://travis-ci.org/github/ndejong/solaredge-interface)
* ReadTheDocs - [solaredge-interface.readthedocs.io](https://solaredge-interface.readthedocs.io)

---
Copyright &copy; 2020 Nicholas de Jong
