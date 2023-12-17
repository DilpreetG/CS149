"""Utility functions for working with catalog information.

Author: Dilpreet Singh Gill
Version: 12/4/2023
"""

import json
import textwrap
import copy


def parse_credits(credits):
    """Return a tuple of ints representing the possible credit values.

    Examples:
    >>> parse_credits("3")
    (3,)
    >>> parse_credits("1-4")
    (1, 2, 3, 4)

    Args:
        credits (str): The credits string.

    Returns:
        tuple: An ordered tuple of all possible credit values.
    """
    final = ()
    if '-' not in credits:
        cred_int = int(credits)
        return (cred_int, )
    elif '-' in credits:
        cred_list = credits.split('-')
        min_cred = int(cred_list[0])
        max_cred = int(cred_list[1])
        for i in range(min_cred, (max_cred + 1)):
            final += (i,)
        return final


def json_to_catalog(json_dict):
    """Convert from the json catalog format to the correct internal format.

    This will return an exact copy of the provided dictionary except for the
    following:

    * The lists of prerequisite course ids will be converted to sets.
    * The credit strings will be converted to integer tuples (using
    the parse_credits function)

    Args:
        json_dict (dict): A catalog dictionary as ready by the json module.

    Returns:
        dict: A catalog dictionary in the correct internal format.

    """
    final_dict = copy.deepcopy(json_dict)
    for key in json_dict:
        final_dict[key]["credits"] = parse_credits(json_dict[key]["credits"])
        if final_dict[key]["prerequisites"] == list():
            final_dict[key]["prerequisites"] = set()
        else:
            final_dict[key]["prerequisites"] = set(json_dict[key]["prerequisites"])
    return final_dict


def load_catalog(filename):
    """Read course information from an JSON file and return a dictionary.

    Args:
        filename (str): The filename of the JSON file.

    Returns:
        dict: A dictionary containing course information.
    """
    json_contents = ''
    with open(filename, 'r') as file:
        for line in file:
            json_contents += line.strip()
    json_dict = json.loads(json_contents)
    temp_dict = json_to_catalog(json_dict)
    final_dict = dict()
    for key in temp_dict:
        final_dict[key] = dict()
        final_dict[key]['credits'] = temp_dict[key]['credits']
        final_dict[key]['description'] = temp_dict[key]['description']
        final_dict[key]['name'] = temp_dict[key]['name']
        final_dict[key]['prerequisites'] = temp_dict[key]['prerequisites']
    return final_dict


def get_dependencies(course_id, catalog):
    """Get the all dependencies for a course.

    This function will return the prerequisites for the course, plus
    all prerequisites for those prerequisites, and so on.

    Args:
        course_id (str): The ID of the course.
        catalog (dict): The dictionary containing course information.

    Returns:
        set: A set of course dependencies.

    """
    final = set()
    empty_set = set()

    # If there's no prereq
    if catalog[course_id]['prerequisites'] == empty_set:
        return final

    # Add current course prerequisites and their dependencies
    final.update(catalog[course_id]['prerequisites'])
    for prereq in catalog[course_id]['prerequisites']:
        # Check if the prerequisite has additional dependencies
        final.update(get_dependencies(prereq, catalog))

    return final


def format_course_info(course_id, catalog, width=40):
    """Format course information for display.

    The resulting string will have five fields: Name, Description,
    Credits, Prerequisites, and Dependencies. Each field will be
    separated by a blank line and each will be wrapped to the maximum
    allowable number of characters. The string will not end in a newline.

    Args:
        course_id (str): The ID of the course.
        catalog (dict): The dictionary containing course information.
        width (int, optional): The width for text wrapping. Defaults to 40.

    Returns:
        str: Formatted course information.
    """
    course_info = catalog.get(course_id, {})
    name = f"Name: {course_info.get('name', 'N/A')}"
    description = f"Description: {course_info.get('description', 'N/A')}"
    credits = f"Credits: {'-'.join(map(str, course_info.get('credits', ())))}"

    prerequisites = course_info.get('prerequisites', set())
    if prerequisites:
        prerequisites = ', '.join(sorted(prerequisites))
    else:
        prerequisites = ''
    prerequisites = f"Prerequisites: {prerequisites}"

    dependencies = get_dependencies(course_id, catalog)
    if dependencies:
        dependencies = ', '.join(sorted(dependencies))
    else:
        dependencies = ''
    dependencies = f"Dependencies: {dependencies}"

    formatted_info = '\n\n'.join([
        textwrap.fill(name, width),
        textwrap.fill(description, width),
        textwrap.fill(credits, width),
        textwrap.fill(prerequisites, width),
        textwrap.fill(dependencies, width)
    ])

    return formatted_info


def total_credits(schedule, catalog):
    """Calculate the range of total credits in a schedule.

    Args:
        schedule (list): The course schedule.
        catalog (dict): The dictionary containing course information.

    Returns:
        tuple: A two entry tuple where the first entry is the minimum
            total credits for the schedule and the second is the maximum total
            credits.
    """
    lest_cred = 0
    most_cred = 0

    for semester in schedule:
        for course_id in semester:
            course_info = catalog.get(course_id)
            if course_info:
                creds = course_info.get('credits')
                if creds:
                    if isinstance(creds, tuple):
                        lest_cred += min(creds)
                        most_cred += max(creds)
                    else:
                        lest_cred += creds
                        most_cred += creds
    return (lest_cred, most_cred)


def available_classes(schedule, semester, catalog):
    """Get the available classes for a semester based on the current schedule.

    A course is available for the indicated semester if it is not
    already present somewhere in the schedule, and all of the
    prerequisites have been fulfilled in some previous semester.

    Args:
        schedule (list): The current course schedule.
        semester (int): The semester for which to find available classes.
        catalog (dict): The dictionary containing course information.

    Returns:
        set: A set of available classes for the specified semester.

    """
    avail_courses = \
        set(course for sem_cs in schedule for course in sem_cs)
    completed_prerequisites = set()
    for i in range(semester):
        completed_prerequisites.update(course for course in schedule[i])
    ava_c = set()
    for course, info in catalog.items():
        if course not in avail_courses:
            if set(info["prerequisites"]) - completed_prerequisites == set():
                ava_c.add(course)
    return ava_c


def check_prerequisites(schedule, catalog):
    """Check for courses in a schedule with unmet prerequisites.

    Args:
        schedule (list): The course schedule.
        catalog (dict): The dictionary containing course information.

    Returns:
        set: A set of courses with unmet prerequisites.
    """
    schedule_classes = set()
    unmet_preqs = set()
    empty_set = set()
    # Iterate through schedule
    for course_set in schedule:
        # Check if mulitple in a semsester
        if len(course_set) > 1:
            for course in course_set:
                for preq in catalog[course]['prerequisites']:
                    if any(dependency in course_set for dependency
                           in catalog[course]['prerequisites']):
                        unmet_preqs.add(course)
        for course in course_set:
            schedule_classes.add(course)
            # Get prerequisites
    for course in schedule_classes:
        for preq in catalog[course]['prerequisites']:
            if preq == empty_set:
                continue
            if preq not in schedule_classes:
                unmet_preqs.add(course)
    return unmet_preqs
