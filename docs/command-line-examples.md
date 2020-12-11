# SolarEdge Interface

## Command Line Examples

### site_current_power_flow
Simple example providing the `--format json` and `1234567` inputs as command-line parameters, these two parameters
could also have been set as environment variables or config file settings.
```shell
user@computer:~$ solaredge-interface --format json site_current_power_flow 1234567
{
  "siteCurrentPowerFlow": {
    "updateRefreshRate": 3,
    "unit": "kW",
    "connections": [
      {
        "from": "LOAD",
        "to": "Grid"
      },
      {
        "from": "PV",
        "to": "Load"
      }
    ],
    "GRID": {
      "status": "Active",
      "currentPower": 1.42
    },
    "LOAD": {
      "status": "Active",
      "currentPower": 0.33
    },
    "PV": {
      "status": "Active",
      "currentPower": 1.75
    }
  }
}
```

### site_energy (json format)
Get the site energy per-week from 2020-11-15 until the current date, review the sub-command usage via `--help` for 
details on valid parameter settings.
```shell
user@computer:~$ solaredge-interface site_energy --time_unit WEEK --start_date 2020-11-15 1234567
{
  "energy": {
    "timeUnit": "WEEK",
    "unit": "Wh",
    "measuredBy": "INVERTER",
    "values": [
      {
        "date": "2020-11-09 00:00:00 AEST+1000",
        "value": 372324.0
      },
      {
        "date": "2020-11-16 00:00:00 AEST+1000",
        "value": 390627.0
      },
      {
        "date": "2020-11-23 00:00:00 AEST+1000",
        "value": 384758.0
      },
      {
        "date": "2020-11-30 00:00:00 AEST+1000",
        "value": 350726.0
      },
      {
        "date": "2020-12-07 00:00:00 AEST+1000",
        "value": 167133.0
      }
    ]
  }
}
```

### site_energy (csv format)
Gets the same site energy data and returns in CSV format which may be useful in some situations. 
```shell
computer:~$ solaredge-interface --format csv site_energy --time_unit WEEK --start_date 2020-11-15 1234567
,energy.timeUnit,energy.unit,energy.measuredBy,energy.values.date,energy.values.value
row_0,WEEK,Wh,INVERTER,2020-11-09 00:00:00+10:00,372324.0
row_1,WEEK,Wh,INVERTER,2020-11-16 00:00:00+10:00,390627.0
row_2,WEEK,Wh,INVERTER,2020-11-23 00:00:00+10:00,384758.0
row_3,WEEK,Wh,INVERTER,2020-11-30 00:00:00+10:00,350726.0
row_4,WEEK,Wh,INVERTER,2020-12-07 00:00:00+10:00,167133.0
```

### site_energy (pandas-json format)
Gets the same site energy data and returns in Pandas-json format which allows the data to be easily loaded into a 
Pandas DataFrame using [from_dict](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.from_dict.html)
The would-be developer is perhaps better off using the `SolarEdgeAPI` directly since a Pandas DataFrame is available
as an attribute in an API response.

```shell
computer:~$ solaredge-interface -W --format pandas site_energy --time_unit WEEK --start_date 2020-11-15 1234567
{
  "energy.timeUnit": {
    "row_0": "WEEK",
    "row_1": "WEEK",
    "row_2": "WEEK",
    "row_3": "WEEK",
    "row_4": "WEEK"
  },
  "energy.unit": {
    "row_0": "Wh",
    "row_1": "Wh",
    "row_2": "Wh",
    "row_3": "Wh",
    "row_4": "Wh"
  },
  "energy.measuredBy": {
    "row_0": "INVERTER",
    "row_1": "INVERTER",
    "row_2": "INVERTER",
    "row_3": "INVERTER",
    "row_4": "INVERTER"
  },
  "energy.values.date": {
    "row_0": 1604844000000,
    "row_1": 1605448800000,
    "row_2": 1606053600000,
    "row_3": 1606658400000,
    "row_4": 1607263200000
  },
  "energy.values.value": {
    "row_0": 372324.0,
    "row_1": 390627.0,
    "row_2": 384758.0,
    "row_3": 350726.0,
    "row_4": 167133.0
  }
}
```
