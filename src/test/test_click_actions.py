
import pytest
from click.testing import CliRunner
from solaredge_interface.cli import click
from solaredge_interface import __version__


def test_solaredge_interface_version():
    runner = CliRunner()
    result = runner.invoke(click.solaredge_interface, '--version')
    assert __version__ in result.output
    assert result.exit_code == 0


def test_solaredge_interface_help():
    runner = CliRunner()
    result = runner.invoke(click.solaredge_interface, '--help')
    assert 'Usage:' in result.output
    assert 'Options:' in result.output
    assert 'Commands:' in result.output
    assert 'accounts' in result.output
    assert 'site_current_power_flow' in result.output
    assert 'site_data_period' in result.output
    assert 'site_details' in result.output
    assert 'site_energy' in result.output
    assert 'site_energy_details' in result.output
    assert 'site_environmental_benefits' in result.output
    assert 'site_equipment_change_log' in result.output
    assert 'site_equipment_data' in result.output
    assert 'site_equipment_sensors' in result.output
    assert 'site_inventory' in result.output
    assert 'site_meters' in result.output
    assert 'site_overview' in result.output
    assert 'site_power' in result.output
    assert 'site_power_details' in result.output
    assert 'site_storage_data' in result.output
    assert 'site_time_frame_energy' in result.output
    assert 'sites' in result.output
    assert 'version_current' in result.output
    assert 'version_supported' in result.output
    assert result.exit_code == 0


def test_solaredge_interface_accounts_help():
    runner = CliRunner()
    result = runner.invoke(click.get_accounts, '--help')
    assert 'Usage:' in result.output
    assert 'Options:' in result.output


def test_solaredge_interface_sites_help():
    runner = CliRunner()
    result = runner.invoke(click.get_sites, '--help')
    assert 'Usage:' in result.output
    assert 'Options:' in result.output


def test_solaredge_interface_site_details_help():
    runner = CliRunner()
    result = runner.invoke(click.get_site_details, '--help')
    assert 'Usage:' in result.output
    assert 'Options:' in result.output


def test_solaredge_interface_site_data_period_help():
    runner = CliRunner()
    result = runner.invoke(click.get_site_data_period, '--help')
    assert 'Usage:' in result.output
    assert 'Options:' in result.output
