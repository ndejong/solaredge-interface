# SolarEdge Interface

## Command Line
Usage for all sub-commands can easily be obtained using the `--help` switch after the sub-command.

Sub-commands map to their `SolarEdgeAPI` Python-module counterparts which in-turn maps to the 
[SolarEdge API documentation](https://www.solaredge.com/sites/default/files/se_monitoring_api.pdf) 

The `api_key` value MUST be set using an environment variable or via a config file, there is no ability 
to set this directly via the command-line itself.

Refer to the [Usage](./usage) and [Examples](./examples) for more detail.

## Environment Variables
* `SOLAREDGE_API_KEY` - the api_key value available through the SolarEdge Monitoring interface within 
  the Admin section.
* `SOLAREDGE_SITE_ID` - the site_id value required for most sub-commands, setting it as a environment value simply
  makes the usage of the command-line tool easier when working with the same site.
* `SOLAREDGE_OUTPUT_FORMAT` - by default output is returned in *json* format, alternatively *csv* and *pandas* 
  formats are possible.

For example, setting the site_id as an environment variable:-
```shell
user@computer:~$ export SOLAREDGE_SITE_ID=1234567
```

## Configuration File
A configuration file will be read from any location specified using the `--config` option.  If this option is not
set an attempt to locate read a configuration from `~/.solaredge-interface` and finally from
`/etc/solaredge-interface` will be made.  Use the `--verbose` to review which file is being read if there is any
confusion.

Settings provided in configuration files always override the equivalent environment value settings.

The configuration file is standard [config](https://docs.python.org/3/library/configparser.html) file format and 
requires a `[solaredge-interface]` section as shown in the sample.

Sample configuration file:- 
```ini
[solaredge-interface]
api_key = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
site_id = 1234567
format = json
```
