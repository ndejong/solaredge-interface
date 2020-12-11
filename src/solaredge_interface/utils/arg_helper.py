
import logging
from solaredge_interface.exceptions.SolarEdgeInterfaceException import SolarEdgeInterfaceException
from solaredge_interface import __env_site_id__ as ENV_SITE_ID
from solaredge_interface import __output_format_default__ as OUTPUT_FORMAT_DEFAULT
from solaredge_interface.utils.timedates import datestring_current, datestring_days_delta
from solaredge_interface.utils.timedates import timestring_current, timestring_seconds_delta


logger = logging.getLogger(__name__)


def site_id(kwargs, config):
    if kwargs['site_id'] is None:
        kwargs['site_id'] = config.site_id
    if kwargs['site_id'] is None:
        raise SolarEdgeInterfaceException('Must provide a "site_id" input value.  See documentation to set via command '
                                          'line argument or using the {} environment variable.'.format(ENV_SITE_ID))
    logger.debug('site_id: {}'.format(kwargs['site_id']))
    return kwargs


def end_date(kwargs):
    if 'end_date' not in kwargs.keys() or kwargs['end_date'] is None:
        kwargs['end_date'] = datestring_current()
    logger.debug('end_date: {}'.format(kwargs['end_date']))
    return kwargs


def start_date(kwargs, delta_days=-7):
    if 'start_date' not in kwargs.keys() or kwargs['start_date'] is None:
        kwargs['start_date'] = datestring_days_delta(kwargs['end_date'], delta=delta_days)
    logger.debug('start_date: {}'.format(kwargs['start_date']))
    return kwargs


def end_time(kwargs):
    if 'end_time' not in kwargs.keys() or kwargs['end_time'] is None:
        kwargs['end_time'] = timestring_current()
    logger.debug('end_time: {}'.format(kwargs['end_time']))
    return kwargs


def start_time(kwargs, delta_time=-(3600*24*7)):
    if 'start_time' not in kwargs.keys() or kwargs['start_time'] is None:
        kwargs['start_time'] = timestring_seconds_delta(kwargs['end_time'], delta=delta_time)
    logger.debug('start_time: {}'.format(kwargs['start_time']))
    return kwargs
