"""
Module consisting of functions that necessary for main module working.
"""

from pathlib import Path
import json


def get_operations() -> list:
    """Returns list of client's operations."""
    file = Path().joinpath("operations.json")
    with open(file) as read_file:
        data = json.load(read_file)
    return data


def edit_operations(data: list) -> list:
    """Returns edited list of operations."""
    for operation in data:
        operation["come_from"] = operation.pop("from")
    return data


def sort_operations(data: list) -> list:
    """Returns sorted list of operations by data."""
    return sorted(data, key=lambda x: x['date'])


# def show_last_operation(data: list, number: int) -> list:
#     """Returns list of specified number last operations."""
#     return


example_data = get_operations()
sorted_list = sort_operations(example_data)

print(sorted_list)
