
import logging
import json
from datetime import datetime
from solaredge_interface.utils.timedates import datetime_to_string, FORMAT_DATETIME_TIMEZONE_STRING


logger = logging.getLogger(__name__)
DATA_PARSE_ERROR_LOGGER = False


class JSONEncoderDateTime(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime):
            return datetime_to_string(obj, datetime_format=FORMAT_DATETIME_TIMEZONE_STRING)
        else:
            return json.JSONEncoder.default(self, obj)


def json_decode(string, error_logger=DATA_PARSE_ERROR_LOGGER):
    try:
        data = json.loads(string)
    except json.decoder.JSONDecodeError:
        if error_logger:
            logger.error('Unable to JSON decode: {}'.format(string[0:255]))
        data = None
    return data
