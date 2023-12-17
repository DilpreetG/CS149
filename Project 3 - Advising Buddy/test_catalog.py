"""Unit tests for catalog_utils.

Author: Dilpreet Singh Gill
Version: 12/1/2023
"""

import catalog_utils as cu


def test_parse_credits():
    assert cu.parse_credits("3") == (3,)
    assert cu.parse_credits("1-4") == (1, 2, 3, 4)
    assert cu.parse_credits("2-2") == (2,)


def test_json_to_catalog():
    cs101_json_dict = {
    "CS 101": {
        "name": "Introduction to Computer Science",
        "credits": "3",
        "description": "How to think like a computer scientist. Topics include an overview of the context of computing, computational operations, computational devices, algorithms and data structures, the storage and transmission of data, the presentation of information, and the limits of computing. Students learn about the design and implementation of computational systems, the value of abstraction, problem-solving and the ways in which computation impacts society.",
        "prerequisites": []
    }
}
    cs101_expected_result = {
    "CS 101": {
        "name": "Introduction to Computer Science",
        "credits": (3,),
        "description": "How to think like a computer scientist. Topics include an overview of the context of computing, computational operations, computational devices, algorithms and data structures, the storage and transmission of data, the presentation of information, and the limits of computing. Students learn about the design and implementation of computational systems, the value of abstraction, problem-solving and the ways in which computation impacts society.",
        "prerequisites": set()
    }
}
    assert cu.json_to_catalog(cs101_json_dict) == cs101_expected_result
    cs261_json_dict = {
    "CS 261": {
        "name": "Computer Systems I",
        "credits": "3",
        "description": "This course provides an introduction to the operation of modern interrupt-driven computer systems. Explores the representation of software and information in binary memory, the primary components of a CPU, systems programming and basic interactions with an Operating System. You may only enroll in CS 261 at most twice.",
        "prerequisites": [
            "CS 159",
            "CS 227"
        ]
    }
}
    cs261_expected_result = {
    "CS 261": {
        "name": "Computer Systems I",
        "credits": (3,),
        "description": "This course provides an introduction to the operation of modern interrupt-driven computer systems. Explores the representation of software and information in binary memory, the primary components of a CPU, systems programming and basic interactions with an Operating System. You may only enroll in CS 261 at most twice.",
        "prerequisites": {
            "CS 159",
            "CS 227"
        }
    }
}
    assert cu.json_to_catalog(cs261_json_dict) == cs261_expected_result

def test_load_catalog():
    catalog = cu.load_catalog("japn_catalog.json")
    assert catalog == {'JAPN 101': {'credits': (4,),
              'description': 'The fundamentals of Japanese through listening, speaking, reading, and writing.',
              'name': 'Elementary Japanese I',
              'prerequisites': set()},
 'JAPN 102': {'credits': (4,),
              'description': 'The fundamentals of Japanese through listening, speaking, reading, and writing. Practice in pronunciation and development of comprehension.',
              'name': 'Elementary Japanese II',
              'prerequisites': {'JAPN 101'}},
 'JAPN 231': {'credits': (3, 4),
              'description': 'A thorough review of grammar, vocabulary building, conversation, composition, and reading.',
              'name': 'Intermediate Japanese I',
              'prerequisites': {'JAPN 102'}}}


def test_get_dependencies():
    catalog = {'JAPN 101': {'credits': (4,),
              'description': 'The fundamentals of Japanese through listening, speaking, reading, and writing.',
              'name': 'Elementary Japanese I',
              'prerequisites': set()},
 'JAPN 102': {'credits': (4,),
              'description': 'The fundamentals of Japanese through listening, speaking, reading, and writing. Practice in pronunciation and development of comprehension.',
              'name': 'Elementary Japanese II',
              'prerequisites': {'JAPN 101'}},
 'JAPN 231': {'credits': (3, 4),
              'description': 'A thorough review of grammar, vocabulary building, conversation, composition, and reading.',
              'name': 'Intermediate Japanese I',
              'prerequisites': {'JAPN 102'}}}

    assert cu.get_dependencies("JAPN 231", catalog) == {"JAPN 102", "JAPN 101"}
    assert cu.get_dependencies("JAPN 102", catalog) == {"JAPN 101"}
    assert cu.get_dependencies("JAPN 101", catalog) == set()


def test_total_credits():
    schedule = [
   {'JAPN 101'},            # First semester
   {'JAPN 102'},             # Second semester
   {'JAPN 231'}    # Third semester
]

    catalog = {'JAPN 101': {'credits': (4,),
              'description': 'The fundamentals of Japanese through listening, speaking, reading, and writing.',
              'name': 'Elementary Japanese I',
              'prerequisites': set()},
 'JAPN 102': {'credits': (4,),
              'description': 'The fundamentals of Japanese through listening, speaking, reading, and writing. Practice in pronunciation and development of comprehension.',
              'name': 'Elementary Japanese II',
              'prerequisites': {'JAPN 101'}},
 'JAPN 231': {'credits': (3, 4),
              'description': 'A thorough review of grammar, vocabulary building, conversation, composition, and reading.',
              'name': 'Intermediate Japanese I',
              'prerequisites': {'JAPN 102'}}}

    assert cu.total_credits(schedule, catalog) == (11, 12)


def test_available_classes():
    #TEST 1
    schedule = [
   {'JAPN 101'},            # First semester
   {'JAPN 102'},             # Second semester
   {'JAPN 231'}    # Third semester
]
    semester = 3
    catalog = {'JAPN 101': {'credits': (4,),
              'description': 'The fundamentals of Japanese through listening, speaking, reading, and writing.',
              'name': 'Elementary Japanese I',
              'prerequisites': set()},
 'JAPN 102': {'credits': (4,),
              'description': 'The fundamentals of Japanese through listening, speaking, reading, and writing. Practice in pronunciation and development of comprehension.',
              'name': 'Elementary Japanese II',
              'prerequisites': {'JAPN 101'}},
 'JAPN 231': {'credits': (3, 4),
              'description': 'A thorough review of grammar, vocabulary building, conversation, composition, and reading.',
              'name': 'Intermediate Japanese I',
              'prerequisites': {'JAPN 102'}}}


    assert cu.available_classes(schedule, semester, catalog) == set()
    #TEST 2
    schedule = [
   {'JAPN 101'},            # First semester
   {'JAPN 102'},             # Second semester
   {}    # Third semester
]
    semester = 3
    catalog = {'JAPN 101': {'credits': (4,),
              'description': 'The fundamentals of Japanese through listening, speaking, reading, and writing.',
              'name': 'Elementary Japanese I',
              'prerequisites': set()},
 'JAPN 102': {'credits': (4,),
              'description': 'The fundamentals of Japanese through listening, speaking, reading, and writing. Practice in pronunciation and development of comprehension.',
              'name': 'Elementary Japanese II',
              'prerequisites': {'JAPN 101'}},
 'JAPN 231': {'credits': (3, 4),
              'description': 'A thorough review of grammar, vocabulary building, conversation, composition, and reading.',
              'name': 'Intermediate Japanese I',
              'prerequisites': {'JAPN 102'}}}
    assert cu.available_classes(schedule, semester, catalog) == {'JAPN 231'}

def test_check_prerequisites():
    #TEST 1
    schedule = [
   {'JAPN 101'},            # First semester
   {'JAPN 102'},             # Second semester
   {'JAPN 231'}    # Third semester
]

    catalog = {'JAPN 101': {'credits': (4,),
              'description': 'The fundamentals of Japanese through listening, speaking, reading, and writing.',
              'name': 'Elementary Japanese I',
              'prerequisites': set()},
 'JAPN 102': {'credits': (4,),
              'description': 'The fundamentals of Japanese through listening, speaking, reading, and writing. Practice in pronunciation and development of comprehension.',
              'name': 'Elementary Japanese II',
              'prerequisites': {'JAPN 101'}},
 'JAPN 231': {'credits': (3, 4),
              'description': 'A thorough review of grammar, vocabulary building, conversation, composition, and reading.',
              'name': 'Intermediate Japanese I',
              'prerequisites': {'JAPN 102'}}}
    assert cu.check_prerequisites(schedule, catalog) == set()
    #TEST 2
    schedule = [
   {},            # First semester
   {'JAPN 102'},             # Second semester
]

    catalog = {'JAPN 101': {'credits': (4,),
              'description': 'The fundamentals of Japanese through listening, speaking, reading, and writing.',
              'name': 'Elementary Japanese I',
              'prerequisites': set()},
 'JAPN 102': {'credits': (4,),
              'description': 'The fundamentals of Japanese through listening, speaking, reading, and writing. Practice in pronunciation and development of comprehension.',
              'name': 'Elementary Japanese II',
              'prerequisites': {'JAPN 101'}},
 'JAPN 231': {'credits': (3, 4),
              'description': 'A thorough review of grammar, vocabulary building, conversation, composition, and reading.',
              'name': 'Intermediate Japanese I',
              'prerequisites': {'JAPN 102'}}}
    assert cu.check_prerequisites(schedule, catalog) == {'JAPN 102'}

# We're providing tests for format_course_info() because these
# kinds of tests are particularly annoying to write.

def test_format_course_info():
    catalog = cu.load_catalog("japn_catalog.json")

    # Test the default width...
    actual = cu.format_course_info("JAPN 231", catalog)
    expect = """Name: Intermediate Japanese I

Description: A thorough review of
grammar, vocabulary building,
conversation, composition, and reading.

Credits: 3-4

Prerequisites: JAPN 102

Dependencies: JAPN 101, JAPN 102"""
    assert actual == expect

    #  Test an alternate width...
    actual = cu.format_course_info("JAPN 231", catalog, width=80)
    expect = """Name: Intermediate Japanese I

Description: A thorough review of grammar, vocabulary building, conversation,
composition, and reading.

Credits: 3-4

Prerequisites: JAPN 102

Dependencies: JAPN 101, JAPN 102"""
    assert actual == expect

    #  Test a different course and a different width...
    actual = cu.format_course_info("JAPN 101", catalog, width=50)
    expect = """Name: Elementary Japanese I

Description: The fundamentals of Japanese through
listening, speaking, reading, and writing.

Credits: 4

Prerequisites:

Dependencies:"""
    assert actual == expect
