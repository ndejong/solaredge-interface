
from solaredge_interface.cli import click
from solaredge_interface import __title__ as NAME
from solaredge_interface import __version__ as VERSION
from solaredge_interface.exceptions.SolarEdgeInterfaceException import SolarEdgeInterfaceException


def solaredge_interface():

    try:
        click.solaredge_interface()
    except SolarEdgeInterfaceException as e:
        print('')
        print('{} v{}'.format(NAME, VERSION))
        print('ERROR: ', end='')
        for err in iter(e.args):
            print(err)
        print('')
        exit(9)
