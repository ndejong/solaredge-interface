# SolarEdge Interface

## Command Line Usage

### solaredge-interface
```shell
user@computer:~$ solaredge-interface --help
Usage: solaredge-interface [OPTIONS] COMMAND [ARGS]...

  The solaredge-interface provides a command-line interface to interact with
  the Python SolarEdgeAPI module which itself calls the SolarEdge public API
  endpoints at https://monitoringapi.solaredge.com making it even easier to
  access your data from SolarEdge.

  Configuration can be achieved through command arguments, environment
  values or config file.

  Documentation available https://solaredge-interface.readthedocs.io

Options:
  -c, --config TEXT       Override default config ~/.solaredge-interface
  -f, --format TEXT       Output format; csv, json, pandas (default: json)
  -v, --verbose           Verbose logging messages (debug level).
  -q, --quiet             Quiet mode, with priority over --verbose
  -W, --disable-warnings  Disable Python warnings.
  --version               Show the version and exit.
  --help                  Show this message and exit.

Commands:
  accounts                     Get the accessible >sub< accounts.
  site_current_power_flow      Current power flow between all elements of...
  site_data_period             Sites(s) start_date and end_date of...
  site_details                 Get site details; name, location, status,...
  site_energy                  Site(s) energy measurements
  site_energy_details          Detailed site energy measurements from meters
  site_environmental_benefits  Environmental benefits based on site energy...
  site_equipment_change_log    Equipment component replacements ordered by...
  site_equipment_data          Get specific inverter data for a given...
  site_equipment_sensors       Sensors in the site and connections
  site_inventory               Inventory of SolarEdge equipment at the site
  site_meters                  Meter lifetime energy, metadata and...
  site_overview                Sites(s) overview data
  site_power                   Site(s) power measurements
  site_power_details           Detailed site power measurements from meters
  site_storage_data            Detailed storage information from batteries
  site_time_frame_energy       Site(s) total energy produced for a given...
  sites                        Get the list of accessible sites
  version_current              Current version in <major.minor.revision>...
  version_supported            Supported version numbers in...
```

### solaredge-interface accounts
```shell
user@computer:~$ solaredge-interface accounts --help
Usage: solaredge-interface accounts [OPTIONS]

  Get the accessible >sub< accounts.

  NB: the response from this endpoint returns a "Not authorized" message if
  there are no sub-accounts assigned.

Options:
  --size INTEGER         The maximum number of accounts returned by this call
  --start_index INTEGER  The first account index to be returned in the results
  --search_text TEXT     The search text for accounts
  --sort_property TEXT   A sorting option based on one of its properties
  --sort_order TEXT      Sort order for the sort property
  --help                 Show this message and exit.
```

### solaredge-interface \<sub-command\>
Usage for all sub-commands can easily be obtained using the `--help` switch after the sub-command as shown
in the `accounts` example above.

