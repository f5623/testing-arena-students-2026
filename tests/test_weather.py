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

## Some extra tests

def test_parse_time_midnight():
    assert parse_time("00:00") == 0

def test_parse_time_last_minute():
    assert parse_time("23:59") == 1439

def test_parse_time_no_leading_zeros():
    assert parse_time("9:5") == 545

def test_parse_time_single_digit_hour():
    assert parse_time("9:05") == 545



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

# some extra tests

def test_parse_measurement_whitespace():
    assert parse_measurement(" Köln ; 14:21 ; 21.7 ") == ("Köln", 861, 21.7)

def test_parse_measurement_invalid_time():
    with pytest.raises(ValueError):
        parse_measurement("Köln;25:00;21.7")

def test_parse_measurement_invalid_temperature():
    with pytest.raises(ValueError):
        parse_measurement("Köln;14:21;abc")

def test_parse_measurement_empty_city_after_strip():
    with pytest.raises(ValueError):
        parse_measurement("   ;14:21;21.7")

def test_parse_measurement_negative_temp_ok():
    # Spec: no plausibility check
    assert parse_measurement("Köln;14:21;-5.3") == ("Köln", 861, -5.3)   

#----------------------------------------------------------------------------------------------#
# Tests for filter_by_temperature
# 

def test_filter_inclusive_boundaries():
    m = [("A", 0, 10.0), ("B", 0, 20.0), ("C", 0, 15.0)]
    assert filter_by_temperature(m, 10.0, 20.0) == [
        ("A", 0, 10.0), ("B", 0, 20.0), ("C", 0, 15.0)
    ]

def test_filter_preserves_order_and_duplicates():
    m = [("A", 0, 20.0), ("B", 0, 15.0), ("A", 0, 20.0)]
    assert filter_by_temperature(m, 10.0, 25.0) == [
        ("A", 0, 20.0), ("B", 0, 15.0), ("A", 0, 20.0)
    ]

def test_filter_lower_gt_upper():
    with pytest.raises(ValueError):
        filter_by_temperature([], 20.0, 10.0)

def test_filter_does_not_mutate_input():
    m = [("A", 0, 15.0), ("B", 0, 5.0)]
    original = list(m)
    filter_by_temperature(m, 10.0, 20.0)
    assert m == original

def test_filter_returns_new_list():
    m = [("A", 0, 15.0)]
    result = filter_by_temperature(m, 10.0, 20.0)
    assert result is not m   

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
        average_temperature('1,2,3',"Köln")

def test_invalid_avg_temp6():
    with pytest.raises(ValueError):
        average_temperature('1,2,3',"köln")

def test_invalid_avg_temp7():
    with pytest.raises(ValueError):
        average_temperature(' ',"köln")

def test_invalid_avg_temp8():
    with pytest.raises(ValueError):
        average_temperature('',"köln")

# more tests

def test_average_case_sensitive():
    m = [("Köln", 0, 10.0), ("köln", 0, 20.0)]
    assert average_temperature(m, "Köln") == 10.0

def test_average_no_match_raises():
    with pytest.raises(ValueError):
        average_temperature([("Berlin", 0, 10.0)], "Köln")

def test_average_ignores_other_cities():
    m = [("Köln", 0, 10.0), ("Bonn", 0, 100.0), ("Köln", 0, 20.0)]
    assert average_temperature(m, "Köln") == 15.0

def test_average_does_not_mutate():
    m = [("Köln", 0, 10.0)]
    original = list(m)
    average_temperature(m, "Köln")
    assert m == original   

#----------------------------------------------------------------------------------------------#
# Tests for hottest_measurement
# 0

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

# more tests

def test_hottest_tie_earliest_time_wins():
    m = [("A", 500, 30.0), ("B", 200, 30.0)]
    assert hottest_measurement(m) == ("B", 200, 30.0)

def test_hottest_tie_same_time_first_occurrence():
    m = [("A", 300, 30.0), ("B", 300, 30.0)]
    assert hottest_measurement(m) == ("A", 300, 30.0)

def test_hottest_empty_raises():
    with pytest.raises(ValueError):
        hottest_measurement([])

def test_hottest_does_not_mutate():
    m = [("A", 0, 10.0), ("B", 0, 20.0)]
    original = list(m)
    hottest_measurement(m)
    assert m == original   