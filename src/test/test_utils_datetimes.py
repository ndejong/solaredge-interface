
from pytz import timezone
from datetime import datetime


from solaredge_interface.utils.timedates import \
    datestring_current, timestring_current, \
    datestring_days_delta, timestring_seconds_delta, \
    datetime_to_string, string_to_datetime, \
    data_to_datetime

from solaredge_interface.utils.timedates import FORMAT_DATETIME_TIMEZONE_STRING, FORMAT_DATETIME_STRING


def test_datestring_current():
    value_1 = datestring_current()
    assert type(value_1) is str
    assert '-' in value_1
    assert ' ' not in value_1
    assert ':' not in value_1

    value_2 = datestring_current(tz='Australia/Sydney')
    assert type(value_2) is str
    assert '-' in value_2
    assert ' ' not in value_2
    assert ':' not in value_2


def test_timestring_current():
    value_1 = timestring_current()
    assert type(value_1) is str
    assert '-' in value_1
    assert ' ' in value_1
    assert ':' in value_1

    value_2 = timestring_current(tz='Australia/Sydney')
    assert type(value_2) is str
    assert '-' in value_2
    assert ' ' in value_2
    assert ':' in value_2

    assert value_1 != value_2


def test_datestring_days_delta():

    value = datestring_days_delta(datestring='2000-01-01', delta=10)
    assert value == '2000-01-11'

    value = datestring_days_delta(datestring='2000-01-01', delta=10, datetime_format=FORMAT_DATETIME_TIMEZONE_STRING)
    assert value == '2000-01-11 00:00:00 '

    value = datestring_days_delta(datestring='2000-01-01', delta=180, datetime_format=FORMAT_DATETIME_STRING)
    assert value == '2000-06-29 00:00:00'

    value = datestring_days_delta(datestring='2020-12-07 14:23:17 AEST+1000', delta=180, datetime_format=FORMAT_DATETIME_TIMEZONE_STRING)
    assert value == '2021-06-05 14:23:17 AEST+1000'


def test_timestamp_seconds_delta():

    value = timestring_seconds_delta(timestring='2000-01-02 00:00:00', delta=(24*3600)-1)
    assert value == '2000-01-02 23:59:59'

    value = timestring_seconds_delta(timestring='2000-01-02 00:00:00 AEST', delta=(24*3600)-1, datetime_format=FORMAT_DATETIME_TIMEZONE_STRING)
    assert value == '2000-01-02 23:59:59 AEST+1000'

    value = timestring_seconds_delta(timestring='2000-01-01 00:00:00 AEST', delta=(180*24*3600)-1, datetime_format=FORMAT_DATETIME_TIMEZONE_STRING)
    assert value == '2000-06-28 23:59:59 AEST+1000'

    value = timestring_seconds_delta(timestring='2000-01-01 00:00:00', delta=(180*24*3600)-1)
    assert value == '2000-06-28 23:59:59'

    value = timestring_seconds_delta(timestring='2000-01-01 00:00:00 AEST', delta=(180*24*3600)-1)
    assert value == '2000-06-28 23:59:59'

    value = timestring_seconds_delta(timestring='2000-01-01 00:00:00 +10', delta=(180*24*3600)-1, datetime_format=FORMAT_DATETIME_TIMEZONE_STRING)
    assert value == '2000-06-28 23:59:59 +1000'

    value = timestring_seconds_delta(timestring='2000-01-01 00:00:00 +1000', delta=(180*24*3600)-1, datetime_format=FORMAT_DATETIME_TIMEZONE_STRING)
    assert value == '2000-06-28 23:59:59 +1000'

    value = timestring_seconds_delta(timestring='2000-01-01 00:00:00 +10:00', delta=(180*24*3600)-1, datetime_format=FORMAT_DATETIME_TIMEZONE_STRING)
    assert value == '2000-06-28 23:59:59 +1000'


def test_datetime_to_string():

    dt1_string = datetime_to_string(datetime.now(tz=timezone('UTC')))
    dt2_string = datetime_to_string(datetime.now(tz=timezone('Australia/Sydney')))
    assert dt1_string != dt2_string

    dt1_now = datetime.now()
    dt2_now = timezone('Australia/Sydney').localize(dt1_now)
    dt1_string = datetime_to_string(dt1_now)
    dt2_string = datetime_to_string(dt2_now)
    assert dt1_string == dt2_string

    dt1_string = datetime_to_string(dt1_now, datetime_format=FORMAT_DATETIME_TIMEZONE_STRING)
    dt2_string = datetime_to_string(dt2_now, datetime_format=FORMAT_DATETIME_TIMEZONE_STRING)
    assert dt1_string != dt2_string


def test_string_to_datetime():
    dt_string = '2020-12-01 00:56:02'
    dt_string_full = dt_string + ' UTC+0000'
    dt1 = string_to_datetime(dt_string)
    dt2 = string_to_datetime(dt_string_full)
    assert dt1 != dt2
    assert dt_string == datetime_to_string(dt1, datetime_format=FORMAT_DATETIME_STRING)
    assert dt_string_full == datetime_to_string(dt2, datetime_format=FORMAT_DATETIME_TIMEZONE_STRING)

    dt3_string = '2020-12-06 17:57:51 AEST+1000'
    dt3 = string_to_datetime(dt3_string)

    dt4_string = '2020-12-06 17:57:51'
    dt4 = string_to_datetime(dt4_string, tz='Australia/Brisbane')

    assert (dt3-dt4).total_seconds() == 0


def test_data_to_datetime():
    data1 = [{
        'foo': 'bar',
        'date1': '2020-01-01',
        'date2': { 'date2_inner': '2020-01-01 00:00:55 UTC+0000' },
        'timestamp': '2020-12-06 17:57:51 AEDT+1100',
    }]

    data1_datetime = data_to_datetime(data1)
    assert datetime_to_string(data1_datetime[0]['timestamp']) == '2020-12-06 17:57:51'
    assert datetime_to_string(data1_datetime[0]['date2']['date2_inner'], datetime_format=FORMAT_DATETIME_TIMEZONE_STRING) == '2020-01-01 00:00:55 UTC+0000'
