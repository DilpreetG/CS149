"""Unit tests for schedule_utils.

Author: Dilpreet Singh Gill
Version: 12/1/2023
"""

import schedule_utils as su

def test_schedule_to_json():
    #TEST 1
    schedule = [
        {'ALGEBRA'},
        {'CS 149'},
        {'CS 159', 'CS 227'}
    ]
    result = su.schedule_to_json(schedule)
    expected = [
        ["ALGEBRA"],
        ["CS 149"],
        ["CS 159", "CS 227"]
    ]
    assert result == expected
    #TEST 2
    schedule2 = [
        {'ALGEBRA'}
    ]
    result = su.schedule_to_json(schedule2)
    expected = [
        ["ALGEBRA"]
    ]
    assert result == expected
    #TEST 3
    schedule3 = [
        {}
    ]
    result = su.schedule_to_json(schedule3)
    expected = [
        []
    ]
    assert result == expected
    #TEST 4
    schedule = [
        {'ALGEBRA', 'ALGEBRA'},
        {'CS 149'},
        {'CS 159', 'CS 227'}
    ]
    result = su.schedule_to_json(schedule)
    expected = [
        ["ALGEBRA"],
        ["CS 149"],
        ["CS 159", "CS 227"]
    ]
    assert result == expected


def test_json_to_schedule():
    #TEST 1
    schedule_list = [
        ["ALGEBRA"],
        ["CS 149"],
        ["CS 159", "CS 227"]
    ]
    result = su.json_to_schedule(schedule_list)
    expected = [
        {'ALGEBRA'},
        {'CS 149'},
        {'CS 159', 'CS 227'}
    ]
    assert result == expected
    #TEST 2
    schedule_list = [
        ["ALGEBRA"],
        ["CS 149"],
        ["CS 159", "CS 227", "CS 227", "CS 227", "CS 159"]
    ]
    result = su.json_to_schedule(schedule_list)
    expected = [
        {'ALGEBRA'},
        {'CS 149'},
        {'CS 159', 'CS 227'}
    ]
    #TEST 3
    schedule_list = [
        []
    ]
    result = su.json_to_schedule(schedule_list)
    expected = [
        {}
    ]
    #TEST 4
    schedule_list = [
        ["ALGEBRA"],
        ["CS 149"],
        ["CS 159", "CS 227"],
        ["ALGEBRA"]
    ]
    result = su.json_to_schedule(schedule_list)
    expected = [
        {'ALGEBRA'},
        {'CS 149'},
        {'CS 159', 'CS 227'},
        {'ALGEBRA'}
    ]

def test_save_load_schedule():
    schedule = [
        {'ALGEBRA'},
        {'CS 149'},
        {'CS 159', 'CS 227'}
    ]
    filename = "test_schedule.json"

    # Save schedule to file
    su.save_schedule(schedule, filename)

    # Load schedule from file
    loaded_schedule = su.load_schedule(filename)

    assert loaded_schedule == schedule


def test_get_duplicates():
    #TEST 1
    schedule_with_duplicates = [
        {'ALGEBRA'},
        {'STATS'},
        {'CALC'},
        {'CS 149'},
        {'CS 149'},
        {'CS 159', 'CS 227'},
        {'STATS'}
    ]

    result_duplicates = su.get_duplicates(schedule_with_duplicates)
    expected_duplicates = {'CS 149', 'STATS'}

    assert result_duplicates == expected_duplicates
    #TEST 2
    schedule_no_duplicates = [
        {'ALGEBRA'},
        {'STATS'},
        {'CALC'},
        {'CS 149'},
        {'CS 159', 'CS 227'}
    ]

    result_no_duplicates = su.get_duplicates(schedule_no_duplicates)
    expected_no_duplicates = set()

    assert result_no_duplicates == expected_no_duplicates
