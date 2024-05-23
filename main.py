"""
Module of main code of program.
"""

from operation import Operation
import utils as u


def main():
    # Extract data from json file.
    list_operations = u.get_operations()
    # Editing file for class creation.
    operations_edited = u.edit_operations(list_operations)
    # Sorting operations by date.
    sorted_operations = u.sort_operations(operations_edited)
    # Extract specified number of operations.
    last_operations = u.show_last_operation(sorted_operations, 5)
    # Class creation from list.
    operations = Operation.from_list(last_operations)
    # Show final result
    for operation in operations:
        print(f"{operation.edit_date(operation.date)} {operation.description} \n"
              f"{operation.hide_card_numbers(operation.come_from)} -> {operation.hide_account_numbers(operation.to)}\n"
              f"{operation.operationAmount['amount']} {operation.operationAmount['currency']['name']}\n")

main()