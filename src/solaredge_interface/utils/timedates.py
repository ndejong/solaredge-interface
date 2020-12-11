
from pytz import timezone
from dateutil import parser
from datetime import datetime, timedelta

FORMAT_DATE_STRING = '%Y-%m-%d'
FORMAT_DATETIME_STRING = '%Y-%m-%d %H:%M:%S'
FORMAT_DATETIME_TIMEZONE_STRING = '%Y-%m-%d %H:%M:%S %Z%z'
DICT_KEY_CONTAIN_CONVERT_DATETIME = ['date', 'time']  # keys containing these stings will attempt string to datetime


def datestring_current(tz=None, datetime_format=FORMAT_DATE_STRING):
    if tz:
        dt = datetime.now(tz=timezone(tz))
    else:
        dt = datetime.now()
    return dt.strftime(datetime_format)


def datestring_days_delta(datestring, delta, datetime_format=FORMAT_DATE_STRING):
    dt = parser.parse(datestring)
    dt_delta = dt + timedelta(days=delta)
    return dt_delta.strftime(datetime_format)


def timestring_current(tz=None, datetime_format=FORMAT_DATETIME_STRING):
    if tz:
        dt = datetime.now(tz=timezone(tz))
    else:
        dt = datetime.now()
    return dt.strftime(datetime_format)


def timestring_seconds_delta(timestring, delta, datetime_format=FORMAT_DATETIME_STRING):
    dt = parser.parse(timestring)
    dt_delta = dt + timedelta(seconds=delta)
    return dt_delta.strftime(datetime_format)


def datetime_to_string(dt, datetime_format=FORMAT_DATETIME_STRING):
    value = dt.strftime(datetime_format)
    return value


def string_to_datetime(string, tz=None):
    try:
        dt = parser.parse(string)
    except (ValueError, TypeError):
        return string
    if tz and not dt.tzinfo:
        dt = timezone(tz).localize(dt)
    return dt


def data_to_datetime(data, tz=None):
    if type(data) is list:
        for index, item in enumerate(data):
            data[index] = data_to_datetime(item)
    elif type(data) is dict:
        for key in data.keys():
            if type(data[key]) is str:
                for key_pattern in DICT_KEY_CONTAIN_CONVERT_DATETIME:
                    if key_pattern in key.lower():
                        data[key] = string_to_datetime(data[key], tz)
                        break
            else:
                data[key] = data_to_datetime(data[key])
    return data


def set_datetime_tzinfo(data, tz=None):
    if type(data) is list:
        for index, item in enumerate(data):
            data[index] = set_datetime_tzinfo(item, tz)
    elif type(data) is dict:
        for key in data.keys():
            data[key] = set_datetime_tzinfo(data[key], tz)
    elif type(data) is datetime and data.tzinfo is None and tz:
        data = timezone(tz).localize(data)
    return data
