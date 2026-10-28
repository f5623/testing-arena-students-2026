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



#------------------------------------------------------------------------------------------------------------#
# Test parse_time_function
# assert parse_time("14:21") == 861


def test_invalid_time1():
    with pytest.raises(ValueError):
        parse_time("14:21")

#------------------------------------------------------------------------------------------------------------#
# Test parse_time_function
#  assert parse_measurement("Köln;14:21;21.7") == ("Köln", 861, 21.7)

'''
def test_invalid_parse_measurement1():
    with pytest.raises(ValueError):
        parse_measurement(123)

def test_invalid_parse_measurement2():
    with pytest.raises(ValueError):
        parse_measurement(";asd;")

def test_invalid_parse_measurement3():
    with pytest.raises(ValueError):
        parse_measurement(";;asd")

def test_invalid_parse_measurement4():
    with pytest.raises(ValueError):
        parse_measurement(";;")

def test_invalid_parse_measurement5():
    with pytest.raises(ValueError):
        parse_measurement(";;12")

def test_invalid_parse_measurement6():
    with pytest.raises(ValueError):
        parse_measurement(";12.6;")

def test_invalid_parse_measurement7():
    with pytest.raises(ValueError):
        parse_measurement("12;;")

def test_invalid_parse_measurement8():
    with pytest.raises(ValueError):
        parse_measurement("12.5;;")

def test_invalid_parse_measurement9():
    with pytest.raises(ValueError):
        parse_measurement(" ")

def test_invalid_parse_measurement10():
    with pytest.raises(ValueError):
        parse_measurement("")
'''
#------------------------------------------------------------------------------------------------------------#
# Test filter_by_temperature_function


''' 
measurements = [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 18.5),
        ("Bonn", 900, 25.0),
    ]

    assert filter_by_temperature(measurements, 15.0, 20.0) == [
        ("Düsseldorf", 720, 18.5)
    ]
'''
'''
def test_invalid_filter_by_temperature1():
    with pytest.raises(ValueError):
        filter_by_temperature(" ",20,15)


def test_invalid_filter_by_temperature2():
    with pytest.raises(ValueError):
        filter_by_temperature(" ",20,-100)


def test_invalid_filter_by_temperature3():
    with pytest.raises(ValueError):
        filter_by_temperature("",100,-100)

def test_invalid_filter_by_temperature4():
    with pytest.raises(ValueError):
        filter_by_temperature("123",1000,-1000)

'''