"""
Module for Operation class creating
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Operation:
    """"""
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
            account_info = "".join([x for x in self.come_from if x.isalpha()])
            card_nums = "".join([x for x in self.come_from if x.isnumeric()])
            return f"{account_info} {card_nums[:4]} {card_nums[6:8]}** **** {card_nums[-4:]}"

    def hide_account_numbers(self, to: str) -> str:
        """Returns string with hidden account numbers."""
        account_info = "".join([x for x in self.to if x.isalpha()])
        return f"{account_info} **{self.to[-4:]}"



operation = Operation(**{
    "id": 594226727,
    "state": "CANCELED",
    "date": "2018-09-12T21:27:25.241689",
    "operationAmount": {
      "amount": "67314.70",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "come_from": "Visa Platinum 1246377376343588",
    "to": "Счет 14211924144426031657"
  })

print(operation)