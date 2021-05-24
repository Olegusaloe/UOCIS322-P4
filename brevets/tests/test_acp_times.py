import nose
from nose.tools import assert_raises

import arrow
from brevets import acp_times
from acp_times import open_time, close_time

import logging

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)

log = logging.getLogger(__name__)

time = arrow.get("2000-01-01T00:00")


def test_neg():
    assert_raises(ValueError, open_time, -10, 200, time)
    assert_raises(ValueError, open_time, -20, 300, time)
    assert_raises(ValueError, open_time, -30, 400, time)
    assert_raises(ValueError, open_time, -40, 600, time)


def test_zero():
    assert open_time(0, 200, time).format('YYYY-MM-DDTHH:mm') == '2000-01-01T00:00'
    assert open_time(0, 300, time).format('YYYY-MM-DDTHH:mm') == '2000-01-01T00:00'
    assert open_time(0, 400, time).format('YYYY-MM-DDTHH:mm') == '2000-01-01T00:00'
    assert open_time(0, 600, time).format('YYYY-MM-DDTHH:mm') == '2000-01-01T00:00'
    
    assert close_time(0, 200, time).format('YYYY-MM-DDTHH:mm') == '2000-01-01T00:00'
    assert close_time(0, 300, time).format('YYYY-MM-DDTHH:mm') == '2000-01-01T00:00'
    assert close_time(0, 400, time).format('YYYY-MM-DDTHH:mm') == '2000-01-01T00:00'
    assert close_time(0, 600, time).format('YYYY-MM-DDTHH:mm') == '2000-01-01T00:00'


def test_200():
	assert open_time(60, 200, time).format('YYYY-MM-DDTHH:mm') == '2000-01-01T01:46'
    assert close_time(60, 200, time).format('YYYY-MM-DDTHH:mm') == '2000-01-01T04:00'

def test_300():
    assert open_time(100, 300, date).format('YYYY-MM-DDTHH:mm') == '2000-01-01T02:56'
    assert close_time(100, 300, date).format('YYYY-MM-DDTHH:mm') == '2000-01-01T06:40'

def test_600(): 
	assert open_time(500, 600, time).format('YYYY-MM-DDTHH:mm') == '2000-01-01T15:28'
    assert close_time(500, 600, time).format('YYYY-MM-DDTHH:mm') == '2000-01-01T09:20'

def test_1000():
    assert open_time(1000, 1000, time).format('YYYY-MM-DDTHH:mm') == '2000-01-02T09:05'
    assert close_time(1000, 1000, time).format('YYYY-MM-DDTHH:mm') == '2021-01-04T03:00'
