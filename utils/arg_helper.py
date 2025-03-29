import argparse


def get_parser():
    parser = argparse.ArgumentParser(
        prog="expense-tracker",
        description="A simple CLI tool to track and manage your expenses",
        epilog="Example: expense-tracker add --description 'Groceries' --amount 50.75",
    )
    sub_parsers = parser.add_subparsers(
        dest="command", help="Available commands", required=True
    )
    # add parser
    add_parsers = sub_parsers.add_parser("add", help="Add a new expense")
    add_parsers.add_argument(
        "-d", "--description", required=True, help="Description of the expense"
    )
    add_parsers.add_argument(
        "--amount", type=int, required=True, help="Amount spent (positive number)"
    )

    # update parser
    update_parsers = sub_parsers.add_parser(
        "update",
        help='Update an existing expense either "description" or "amount" is required',
    )
    update_parsers.add_argument(
        "--id", type=int, required=True, help="ID of the expense to update"
    )
    update_parsers.add_argument(
        "-d",
        "--description",
        required=False,
        help="New description of the expense (optional)",
    )
    update_parsers.add_argument(
        "--amount", type=int, required=False, help="New amount spent (optional)"
    )

    # delete parser
    delete_parsers = sub_parsers.add_parser("delete", help="Delete an existing expense")
    delete_parsers.add_argument(
        "--id", type=int, required=True, help="ID of the expense to delete"
    )

    # list parser
    list_parsers = sub_parsers.add_parser("list", help="List all expenses")
    list_parsers.add_argument(
        "-m",
        "--month",
        required=False,
        type=int,
        help="Filter expenses by month (1-12)",
    )

    # summary parser
    sum_parsers = sub_parsers.add_parser("summary", help="Show expense summary")
    sum_parsers.add_argument(
        "-m", "--month", type=int, help="Show summary for a specific month (1-12)"
    )

    return parser.parse_args()
