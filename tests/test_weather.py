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
# 2 found
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
# None found

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
        parse_measurement(" Köln , 1:1 , 21 ")

def test_invalid_measurement7():
    with pytest.raises(ValueError):
        parse_measurement(" Köln : 14;21 : 21 ")

def test_invalid_measurement8():
    with pytest.raises(ValueError):
        parse_measurement("2; 14;21 ; 21 ")

def test_invalid_measurement8():
    with pytest.raises(ValueError):
        parse_measurement("2; 14;21 ; 21 ")


def test_invalid_measurement9():
    with pytest.raises(ValueError):
        parse_measurement(1.5)

def test_invalid_measurement10():
    with pytest.raises(ValueError):
        parse_measurement('')

def test_invalid_measurement11():
    with pytest.raises(ValueError):
        parse_measurement(' ')

def test_invalid_measurement12():
    with pytest.raises(ValueError):
        parse_measurement('Köln')

def test_invalid_measurement13():
    with pytest.raises(ValueError):
        parse_measurement('1')

def test_invalid_measurement14():
    with pytest.raises(ValueError):
        parse_measurement('; ; ; ;')

def test_invalid_measurement15():
    with pytest.raises(ValueError):
        parse_measurement('1;2 ; 3; 4;5')

def test_invalid_measurement16():
    with pytest.raises(ValueError):
        parse_measurement(';')

def test_invalid_measurement17():
    with pytest.raises(ValueError):
        parse_measurement('; ;')

def test_invalid_measurement18():
    with pytest.raises(ValueError):
        parse_measurement('::')


#----------------------------------------------------------------------------------------------#
# Tests for average_temperature
# 1

def test_invalid_avg_temp1():
    with pytest.raises(ValueError):
        average_temperature('a',"Köln")

def test_invalid_avg_temp2():
    with pytest.raises(ValueError):
        average_temperature("Köln",'b')

def test_invalid_avg_temp3():
    with pytest.raises(ValueError):
        average_temperature('-1000',"Köln")

def test_invalid_avg_temp4():
    with pytest.raises(ValueError):
        average_temperature('1000',"Köln")

def test_invalid_avg_temp5():
    with pytest.raises(ValueError):
        average_temperature('[1,2,3]',"Köln")

def test_invalid_avg_temp6():
    with pytest.raises(ValueError):
        average_temperature('[1,2,3]',"köln")

def test_invalid_avg_temp7():
    with pytest.raises(ValueError):
        average_temperature(' ',"köln")

def test_invalid_avg_temp8():
    with pytest.raises(ValueError):
        average_temperature('',"köln")


'''
def test_invalid_avg_temp():
    with pytest.raises(ValueError):
        average_temperature('')

def test_invalid_avg_temp():
    with pytest.raises(ValueError):
        average_temperature('')

def test_invalid_avg_temp():
    with pytest.raises(ValueError):
        average_temperature('')

def test_invalid_avg_temp():
    with pytest.raises(ValueError):
        average_temperature('')

def test_invalid_avg_temp():
    with pytest.raises(ValueError):
        average_temperature('')

def test_invalid_avg_temp():
    with pytest.raises(ValueError):
        average_temperature('')

'''


#----------------------------------------------------------------------------------------------#
# Tests for hottest_measurement
# 

def test_invalid_hottest_temp1():
    with pytest.raises(ValueError):
        hottest_measurement('')

'''def test_invalid_hottest_temp2():
    with pytest.raises(ValueError):
        hottest_measurement('01010120274871287481274')'''

def test_invalid_hottest_temp3():
    with pytest.raises(IndexError):
        hottest_measurement('12')

def test_invalid_hottest_temp4():
    with pytest.raises(IndexError):
        hottest_measurement('-100')

def test_invalid_hottest_temp5():
    with pytest.raises(IndexError):
        hottest_measurement("1,2,3")

'''def test_invalid_hottest_temp6():
    with pytest.raises(ValueError):
        hottest_measurement("-10,5,0")
'''
'''
def test_invalid_hottest_temp():
    with pytest.raises(ValueError):
        hottest_measurement('')

def test_invalid_hottest_temp():
    with pytest.raises(ValueError):
        hottest_measurement('')

def test_invalid_hottest_temp():
    with pytest.raises(ValueError):
        hottest_measurement('')

def test_invalid_hottest_temp():
    with pytest.raises(ValueError):
        hottest_measurement('')

def test_invalid_hottest_temp():
    with pytest.raises(ValueError):
        hottest_measurement('')
'''