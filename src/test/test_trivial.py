
from solaredge_interface import __author__
from solaredge_interface import __version__
from solaredge_interface import __title__
from solaredge_interface import __license__


def test_author_exist():
    assert __author__ is not None


def test_version_exist():
    assert __version__ is not None


def test_title_exist():
    assert __title__ is not None


def test_license_exist():
    assert __license__ is not None
