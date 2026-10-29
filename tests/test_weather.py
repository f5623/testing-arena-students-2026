"""Starter tests for the weather module.

These tests deliberately cover only ordinary examples. They show how pytest works,
but they are not a sufficient test suite for the specification in SPECIFICATION.md.
"""
import pytest

from weather import (
    average_temperature,
    filter_by_temperature,
    hottest_measurement,
    parse_measurement,
    parse_time,
)


def test_parse_time_regular_time():
    assert parse_time("14:21") == 861


def test_parse_measurement_regular_line():
    assert parse_measurement("Köln;14:21;21.7") == ("Köln", 861, 21.7)


def test_filter_by_temperature_regular_values():
    measurements = [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 18.5),
        ("Bonn", 900, 25.0),
    ]

    assert filter_by_temperature(measurements, 15.0, 20.0) == [
        ("Düsseldorf", 720, 18.5)
    ]


def test_average_temperature_regular_values():
    measurements = [
        ("Köln", 600, 10.0),
        ("Köln", 720, 20.0),
    ]

    assert average_temperature(measurements, "Köln") == 15.0


def test_hottest_measurement_with_unique_maximum():
    measurements = [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 25.0),
        ("Bonn", 900, 20.0),
    ]

    assert hottest_measurement(measurements) == ("Düsseldorf", 720, 25.0)


#----------------------------------------------------------------------------------------------#
# Tests for parse time
'''
parse_time("14:21") == 861
parse_time("00:00") == 0
parse_time("23:59") == 1439
'''

def test_invalid_time1():
    with pytest.raises(ValueError):
        parse_time("ab:cd")

def test_invalid_time2():
    with pytest.raises(ValueError):
        parse_time("ab.cd")

def test_invalid_time3():
    with pytest.raises(ValueError):
        parse_time("a:b")

def test_invalid_time4():
    with pytest.raises(ValueError):
        parse_time("a.b")

def test_invalid_time5():
    with pytest.raises(ValueError):
        parse_time("24:00")

def test_invalid_time6():
    with pytest.raises(ValueError):
        parse_time("24:60")

def test_invalid_time7():
    with pytest.raises(ValueError):
        parse_time("23:60")


#----------------------------------------------------------------------------------------------#
# Tests for parse_measurement

def test_invalid_measurement1():
    with pytest.raises(ValueError):
        parse_measurement(1)


def test_invalid_measurement2():
    with pytest.raises(ValueError):
        parse_measurement("a:b:c")

def test_invalid_measurement3():
    with pytest.raises(ValueError):
        parse_measurement("a:")

def test_invalid_measurement4():
    with pytest.raises(ValueError):
        parse_measurement("a:b")

def test_invalid_measurement5():
    with pytest.raises(ValueError):
        parse_measurement(":c")

def test_invalid_measurement6():
    with pytest.raises(ValueError):
        parse_measurement(" Köln , 1:1 ; 21 ")

def test_invalid_measurement7():
    with pytest.raises(ValueError):
        parse_measurement(" Köln ; 14;21 ; 21 ")

def test_invalid_measurement8():
    with pytest.raises(ValueError):
        parse_measurement("2; 14;21 ; 21 ")

def test_invalid_measurement8():
    with pytest.raises(ValueError):
        parse_measurement("2; 14;21 ; 21 ")
