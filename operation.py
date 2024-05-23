"""
Module for Operation class creating
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Operation:
    id: str
    state: str
    date: str
    operationAmount: dict
    description: str
    to: str
    come_from: str = None

    @classmethod
    def from_list(cls, array: list) -> list:
        return [Operation(**x) for x in array]

    def edit_date(self, date: str) -> str:
        """Returns representation of time."""
        date = datetime.fromisoformat(self.date)
        day = date.day
        month = date.month
        year = date.year
        return f"{day}.{month}.{year}"

    def hide_card_numbers(self, come_from: str) -> str:
        """Return string with hidden card numbers."""
        if come_from:
            card_nums = ''.join([x for x in self.come_from if x.isnumeric()])
            return f"{card_nums[:4]} {card_nums[6:8]}** **** {card_nums[-4:]}"

    def hide_account_numbers(self, to: str) -> str:
        """Returns string with hidden account numbers."""
        return f"**{self.to[-4:]}"


example_data = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "come_from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }




operation = Operation(**example_data)
print(operation)

