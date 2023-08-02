
import sys
import click
import logging
import warnings

from solaredge_interface import __version__ as VERSION
from solaredge_interface import __env_api_key__ as ENV_API_KEY
from solaredge_interface import __output_format_default__ as OUTPUT_FORMAT_DEFAULT
from solaredge_interface.utils import arg_helper
from solaredge_interface.utils.output import format_output
from solaredge_interface.api.SolarEdgeAPI import SolarEdgeAPI
from solaredge_interface.cli.config import Config
from solaredge_interface.exceptions.SolarEdgeInterfaceException import SolarEdgeInterfaceException

solaredge_api = None
solaredge_cli_config = None


@click.group()
@click.option('-c', '--config', help='Override default config ~/.solaredge-interface')
@click.option('-f', '--format', help='Output format; csv, json, pandas (default: json)')
@click.option('-v', '--verbose', is_flag=True, help='Verbose logging messages (debug level).')
@click.option('-q', '--quiet', is_flag=True, help='Quiet mode, with priority over --verbose')
@click.option('-W', '--disable-warnings', is_flag=True, help='Disable Python warnings.')
@click.version_option(VERSION)
def solaredge_interface(config, format, verbose, quiet, disable_warnings):
    """
    The solaredge-interface provides a command-line interface to interact with the Python SolarEdgeAPI module which
    itself calls the SolarEdge public API endpoints at https://monitoringapi.solaredge.com making it even easier to
    access your data from SolarEdge.

    Configuration can be achieved through command arguments, environment values or config file.

    Documentation available https://solaredge-interface.readthedocs.io
    """

    ctx = click.get_current_context()
    ctx.ensure_object(dict)

    if quiet:
        level = logging.CRITICAL
    elif verbose:
        level = logging.DEBUG
    else:
        level = logging.WARNING

    logging.basicConfig(
        level=level,
        format='[%(levelname)s|%(asctime)s|%(name)s]: %(message)s',
    )

    if not sys.warnoptions and not disable_warnings:
        warnings.simplefilter("default")  # Change the filter in this process

    global solaredge_api
    global solaredge_cli_config

    solaredge_cli_config = Config(session_config_file=config)
    if not solaredge_cli_config.api_key:
        raise SolarEdgeInterfaceException('SolarEdge api_key value not supplied.  See documentation to set this '
                                          'using the {} environment variable or using configuration file(s).'
                                          .format(ENV_API_KEY))
    if format:
        solaredge_cli_config.format = format
    elif solaredge_cli_config.format is None:
        solaredge_cli_config.format = OUTPUT_FORMAT_DEFAULT

    solaredge_api = SolarEdgeAPI(api_key=solaredge_cli_config.api_key, datetime_response=True, pandas_response=True)


@solaredge_interface.command('accounts')
@click.option('--size', help='The maximum number of accounts returned by this call', required=False, default=100)
@click.option('--start_index', help='The first account index to be returned in the results', required=False, default=0)
@click.option('--search_text', help='The search text for accounts', required=False, default="")
@click.option('--sort_property', help='A sorting option based on one of its properties', required=False, default="")
@click.option('--sort_order', help='Sort order for the sort property', required=False, default="ASC")
def get_accounts(**kwargs):
    """
    Get the accessible >sub< accounts.

    NB: the response from this endpoint returns a "Not authorized" message if there are no sub-accounts assigned.
    """
    format_output(
        response=solaredge_api.get_accounts(**kwargs),
        output_format=solaredge_cli_config.format
    )


@solaredge_interface.command('sites')
@click.option('--size', help='The maximum number of sites returned by this call', required=False, default=100)
@click.option('--start_index', help='The first site index to be returned in the results', required=False, default=0)
@click.option('--search_text', help='The search text for sites', required=False, default="")
@click.option('--sort_property', help='A sorting option based on one of its properties', required=False, default="")
@click.option('--sort_order', help='Sort order for the sort property', required=False, default="ASC")
@click.option('--status', help='Selected sites to be included in the list', required=False, default="Active,Pending")
def get_sites(**kwargs):
    """
    Get the list of accessible sites
    """
    format_output(
        response=solaredge_api.get_sites(**kwargs),
        output_format=solaredge_cli_config.format
    )


@solaredge_interface.command('site_details')
@click.argument('site_id', required=False)
def get_site_details(**kwargs):
    """
    Get site details; name, location, status, etc.
    """
    kwargs = arg_helper.site_id(kwargs, config=solaredge_cli_config)
    format_output(
        response=solaredge_api.get_site_details(**kwargs),
        output_format=solaredge_cli_config.format
    )


@solaredge_interface.command('site_data_period')
@click.argument('site_id', required=False)
def get_site_data_period(**kwargs):
    """
    Sites(s) start_date and end_date of production
    """
    kwargs = arg_helper.site_id(kwargs, config=solaredge_cli_config)
    format_output(
        response=solaredge_api.get_site_data_period(**kwargs),
        output_format=solaredge_cli_config.format
    )


@solaredge_interface.command('site_energy')
@click.argument('site_id', required=False)
@click.option('--start_date', help='Default 7 days ago, else format "YYYY-MM-DD"')
@click.option('--end_date', help='Default todays date, else format "YYYY-MM-DD"')
@click.option('--time_unit', help='QUARTER_OF_AN_HOUR, HOUR, *DAY, WEEK, MONTH, YEAR', default='DAY')
def get_site_energy(**kwargs):
    """
    Site(s) energy measurements
    """
    kwargs = arg_helper.site_id(kwargs, config=solaredge_cli_config)
    kwargs = arg_helper.end_date(kwargs)
    kwargs = arg_helper.start_date(kwargs, delta_days=-7)
    format_output(
        response=solaredge_api.get_site_energy(**kwargs),
        output_format=solaredge_cli_config.format
    )


@solaredge_interface.command('site_time_frame_energy')
@click.argument('site_id', required=False)
@click.option('--start_date', help='Default 7 days ago, else format "YYYY-MM-DD"')
@click.option('--end_date', help='Default todays date, else format "YYYY-MM-DD"')
def get_site_time_frame_energy(**kwargs):
    """
    Site(s) total energy produced for a given period
    """
    kwargs = arg_helper.site_id(kwargs, config=solaredge_cli_config)
    kwargs = arg_helper.end_date(kwargs)
    kwargs = arg_helper.start_date(kwargs, delta_days=-7)
    format_output(
        response=solaredge_api.get_site_time_frame_energy(**kwargs),
        output_format=solaredge_cli_config.format
    )


@solaredge_interface.command('site_overview')
@click.argument('site_id', required=False)
def get_site_overview(**kwargs):
    """
    Sites(s) overview data
    """
    kwargs = arg_helper.site_id(kwargs, config=solaredge_cli_config)
    format_output(
        response=solaredge_api.get_site_overview(**kwargs),
        output_format=solaredge_cli_config.format
    )


@solaredge_interface.command('site_power')
@click.argument('site_id', required=False)
@click.option('--start_time', help='Default 7 days ago, else format "YYYY-MM-DD hh:mm:ss"')
@click.option('--end_time', help='Default now time, else format "YYYY-MM-DD hh:mm:ss"')
def get_site_power(**kwargs):
    """
    Site(s) power measurements
    """
    kwargs = arg_helper.site_id(kwargs, config=solaredge_cli_config)
    kwargs = arg_helper.end_time(kwargs)
    kwargs = arg_helper.start_time(kwargs, delta_time=-(3600*24*7))
    format_output(
        response=solaredge_api.get_site_power(**kwargs),
        output_format=solaredge_cli_config.format
    )


@solaredge_interface.command('site_power_details')
@click.argument('site_id', required=False)
@click.option('--start_time', help='Default 7 days ago, else format "YYYY-MM-DD hh:mm:ss"')
@click.option('--end_time', help='Default now time, else format "YYYY-MM-DD hh:mm:ss"')
@click.option('--meters', help='Production, Consumption, SelfConsumption, FeedIn, Purchased', default=None)
def get_site_power_details(**kwargs):
    """
    Detailed site power measurements from meters
    """
    kwargs = arg_helper.site_id(kwargs, config=solaredge_cli_config)
    kwargs = arg_helper.end_time(kwargs)
    kwargs = arg_helper.start_time(kwargs, delta_time=-(3600*24*7))
    format_output(
        response=solaredge_api.get_site_power_details(**kwargs),
        output_format=solaredge_cli_config.format
    )


@solaredge_interface.command('site_energy_details')
@click.argument('site_id', required=False)
@click.option('--start_time', help='Default 7 days ago, else format "YYYY-MM-DD hh:mm:ss"')
@click.option('--end_time', help='Default now time, else format "YYYY-MM-DD hh:mm:ss"')
@click.option('--meters', help='Production, Consumption, SelfConsumption, FeedIn, Purchased', default=None)
@click.option('--time_unit', help='QUARTER_OF_AN_HOUR, HOUR, DAY, WEEK, MONTH, YEAR', default='DAY')
def get_site_energy_details(**kwargs):
    """
    Detailed site energy measurements from meters
    """
    kwargs = arg_helper.site_id(kwargs, config=solaredge_cli_config)
    kwargs = arg_helper.end_time(kwargs)
    kwargs = arg_helper.start_time(kwargs, delta_time=-(3600*24*7))
    format_output(
        response=solaredge_api.get_site_energy_details(**kwargs),
        output_format=solaredge_cli_config.format
    )


@solaredge_interface.command('site_current_power_flow')
@click.argument('site_id', required=False)
def get_site_current_power_flow(**kwargs):
    """
    Current power flow between all elements of the site
    """
    kwargs = arg_helper.site_id(kwargs, config=solaredge_cli_config)
    format_output(
        response=solaredge_api.get_site_current_power_flow(**kwargs),
        output_format=solaredge_cli_config.format
    )


@solaredge_interface.command('site_storage_data')
@click.argument('site_id', required=False)
@click.option('--start_time', help='Default 7 days ago, else format "YYYY-MM-DD hh:mm:ss"')
@click.option('--end_time', help='Default now time, else format "YYYY-MM-DD hh:mm:ss"')
@click.option('--serials', help='If omitted, returns all batteries at site', default=None)
def get_site_storage_data(**kwargs):
    """
    Detailed storage information from batteries
    """
    kwargs = arg_helper.site_id(kwargs, config=solaredge_cli_config)
    kwargs = arg_helper.end_time(kwargs)
    kwargs = arg_helper.start_time(kwargs, delta_time=-(3600*24*7))
    format_output(
        response=solaredge_api.get_site_storage_data(**kwargs),
        output_format=solaredge_cli_config.format
    )


@solaredge_interface.command('site_environmental_benefits')
@click.argument('site_id', required=False)
@click.option('--system_units', help='Metrics, Imperial - case sensitive', default=None)
def get_site_environmental_benefits(**kwargs):
    """
    Environmental benefits based on site energy production
    """
    kwargs = arg_helper.site_id(kwargs, config=solaredge_cli_config)
    format_output(
        response=solaredge_api.get_site_environmental_benefits(**kwargs),
        output_format=solaredge_cli_config.format
    )


@solaredge_interface.command('site_inventory')
@click.argument('site_id', required=False)
def get_site_inventory(**kwargs):
    """
    Inventory of SolarEdge equipment at the site
    """
    kwargs = arg_helper.site_id(kwargs, config=solaredge_cli_config)
    format_output(
        response=solaredge_api.get_site_inventory(**kwargs),
        output_format=solaredge_cli_config.format
    )


@solaredge_interface.command('site_equipment_data')
@click.argument('site_id', required=False)
@click.option('--start_time', help='Default 7 days ago, else format "YYYY-MM-DD hh:mm:ss"')
@click.option('--end_time', help='Default now time, else format "YYYY-MM-DD hh:mm:ss"')
@click.option('--serial_number', help='The inverter short serial number', required=True)
def get_site_equipment_data(**kwargs):
    """
    Get specific inverter data for a given timeframe
    """
    kwargs = arg_helper.site_id(kwargs, config=solaredge_cli_config)
    kwargs = arg_helper.end_time(kwargs)
    kwargs = arg_helper.start_time(kwargs, delta_time=-(3600*24*7))
    format_output(
        response=solaredge_api.get_site_equipment_data(**kwargs),
        output_format=solaredge_cli_config.format
    )


@solaredge_interface.command('site_equipment_change_log')
@click.argument('site_id', required=False)
@click.option('--serial_number', help='The inverter short serial number', required=True)
def get_site_equipment_change_log(**kwargs):
    """
    Equipment component replacements ordered by date
    """
    kwargs = arg_helper.site_id(kwargs, config=solaredge_cli_config)
    format_output(
        response=solaredge_api.get_site_equipment_change_log(**kwargs),
        output_format=solaredge_cli_config.format
    )


@solaredge_interface.command('site_meters')
@click.argument('site_id', required=False)
@click.option('--start_time', help='Default 7 days ago, else format "YYYY-MM-DD hh:mm:ss"')
@click.option('--end_time', help='Default now time, else format "YYYY-MM-DD hh:mm:ss"')
@click.option('--meters', help='Production, Consumption, SelfConsumption, FeedIn, Purchased', default=None)
def get_site_meters(**kwargs):
    """
    Meter lifetime energy, metadata and connection detail
    """
    kwargs = arg_helper.site_id(kwargs, config=solaredge_cli_config)
    kwargs = arg_helper.end_time(kwargs)
    kwargs = arg_helper.start_time(kwargs, delta_time=-(3600*24*7))
    format_output(
        response=solaredge_api.get_site_meters(**kwargs),
        output_format=solaredge_cli_config.format
    )

@solaredge_interface.command('site_sensors')
@click.argument('site_id', required=False)
@click.option('--start_time', help='Default 7 days ago, else format "YYYY-MM-DD hh:mm:ss"')
@click.option('--end_time', help='Default now time, else format "YYYY-MM-DD hh:mm:ss"')
def get_site_meters(**kwargs):
    """
    Returns a list of all the sensors in the site, and the device to which they are connected.
    """
    kwargs = arg_helper.site_id(kwargs, config=solaredge_cli_config)
    kwargs = arg_helper.end_time(kwargs)
    kwargs = arg_helper.start_time(kwargs, delta_time=-(3600*24*7))
    format_output(
        response=solaredge_api.get_site_sensors(**kwargs),
        output_format=solaredge_cli_config.format
    )


@solaredge_interface.command('site_equipment_sensors')
@click.argument('site_id', required=False)
def get_site_equipment_sensors(**kwargs):
    """
    Sensors in the site and connections
    """
    kwargs = arg_helper.site_id(kwargs, config=solaredge_cli_config)
    format_output(
        response=solaredge_api.get_site_equipment_sensors(**kwargs),
        output_format=solaredge_cli_config.format
    )


@solaredge_interface.command('version_current')
def get_version_current(**kwargs):
    """
    Current version in <major.minor.revision> format
    """
    format_output(
        response=solaredge_api.get_version_current(**kwargs),
        output_format=solaredge_cli_config.format
    )


@solaredge_interface.command('version_supported')
def get_version_supported(**kwargs):
    """
    Supported version numbers in <major.minor.revision> format.
    """
    format_output(
        response=solaredge_api.get_version_supported(**kwargs),
        output_format=solaredge_cli_config.format
    )
