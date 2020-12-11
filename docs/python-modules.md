# SolarEdge Interface

## SolarEdgeAPI
All API calls return a `response` object with request and response attributes that are likely helpful to the 
developer.

* `cookies` - any cookies set by the server in the response
* `elapsed` - time elapsed, taken from the Python-requests module [Response attribute](https://requests.readthedocs.io/en/master/api/#requests.Response.elapsed)
* `headers` - response headers, taken from the Python-requests module [Response attribute](https://requests.readthedocs.io/en/master/api/#requests.Response.headers)
* `request` - the Python-requests `request` object which contains the attributes for the http-request etc.
* `status_code` - the response http status code.
* `text` - the raw text response from the server.
* `data` - the parsed out from JSON contained in the `text` attribute.
* `pandas` - a Pandas DataFrame representation of the `data` after a data-flattening procedure.
* `url` - the request URL used.

Example

```python
Python 3.8.5 (default, Jul 28 2020, 12:59:40) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> from solaredge_interface.api.SolarEdgeAPI import SolarEdgeAPI
>>> api = SolarEdgeAPI(api_key='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', datetime_response=True, pandas_response=True)
>>> response = api.get_site_current_power_flow(1234567)
>>> response.status_code
200
>>>
>>> response.url
'https://monitoringapi.solaredge.com/site/1234567/currentPowerFlow?api_key=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
>>>
>>> response.data
{'siteCurrentPowerFlow': {'updateRefreshRate': 3, 'unit': 'kW', 'connections': [{'from': 'GRID', 'to': 'Load'}], 'GRID': {'status': 'Active', 'currentPower': 0.7}, 'LOAD': {'status': 'Active', 'currentPower': 0.7}, 'PV': {'status': 'Idle', 'currentPower': 0.0}}}
>>>
```

Refer to the [SolarEdgeAPI documentation](./solaredgeapi) for further detail. 

## SolarEdgeInterfaceException
Use `SolarEdgeInterfaceException` to catch exception thrown by the `SolarEdgeAPI`
