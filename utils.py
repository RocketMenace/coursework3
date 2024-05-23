"""
Module consisting of functions that necessary for main module working.
"""

import json
from pathlib import Path


def get_operations() -> list:
    """Returns list of client's operations."""
    file = Path().joinpath("operations.json")
    with open(file, encoding="UTF-8") as read_file:
        data = json.load(read_file)
    return data


def edit_operations(data: list) -> list:
    """Returns edited list of operations."""
    lst = [x for x in data if x.get("from")]
    for operation in lst:
        operation["come_from"] = operation.pop("from")
    return lst


def sort_operations(data: list) -> list:
    """Returns sorted list of operations by data."""
    lst = [x for x in data if x.get("date")]
    return sorted(lst, key=lambda x: x["date"], reverse=True)


def show_last_operation(data: list, number: int) -> list:
    """Returns list of specified number last operations."""
    return [x for x in data[0:number + 1] if x["state"] == "EXECUTED"]
