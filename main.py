import calendar
import datetime
import json
import os
import pathlib
from sqlite3 import Date
from traceback import print_tb
from rich.console import Console
from rich.table import Table

from utils.arg_helper import get_parser


def file_size(filename: str) -> bool:
    return os.path.getsize(filename) < 0


def get_json_data() -> dict:

    with open("data.json", "r") as file:
        return json.load(file)


def timestamp():
    return datetime.date.today().isoformat()


def main():
    args = get_parser()

    console = Console

    json_file = pathlib.Path("data.json")

    if not json_file.exists() or file_size(json_file):
        json_data = {"total_amount": 0, "entry_no": 0}
        with open("data.json", "a+") as file:
            json.dump(json_data, file, indent=4)

    if args.command == "add":
        json_data = get_json_data()
        json_data[f"etry{json_data["entry_no"]}"] = {
            "expense_id": json_data["entry_no"],
            "Date": timestamp(),
            "Description": args.description,
            "Amount": args.amount,
        }
        json_data["entry_no"] += 1
        json_data["total_amount"] += args.amount
        with open("data.json", "w") as file:
            json.dump(json_data, file, indent=4)

    elif args.command == "update":
        if not args.description and not args.amount:
            print("enter the new field values to update")
            return
        json_data = get_json_data()

        entry_key = f"etry{args.id}"

        if entry_key not in json_data.keys():
            print(f"{entry_key} is not a valid id, enter a valid id")
            return

        if args.description:
            json_data[entry_key]["Description"] = args.description
        if args.amount:
            json_data[entry_key]["Amount"] = args.amount

        with open("data.json", "w") as file:
            json.dump(json_data, file, indent=4)

        print(f"Expense {args.id} updated successfully")

    elif args.command == "delete":
        json_data = get_json_data()
        entry_key = f"etry{args.id}"

        if entry_key not in json_data.keys():
            print(f"{entry_key} is not a valid id, enter a valid id")
            return

        json_data.pop(entry_key)

        with open("data.json", "w") as file:
            json_data["entry_no"] -= 1
            json.dump(json_data, file, indent=4)

        print(f"Expense {args.id} deleted successfully")

    elif args.command == "list":
        console = Console()

        json_data = get_json_data()

        table = Table(
            show_header=True,
            header_style="bold magenta",
            show_lines=False,
            box=None,
        )

        table.add_column("id", style="dim", width=12)
        table.add_column("Date", style="dim", width=12)
        table.add_column("Description")
        table.add_column("Amount", justify="right")

        if args.month and 1 <= args.month <= 12:
            month_str = f"{args.month:02d}"
            for i in range(json_data["entry_no"]):
                entry_key = f"etry{i}"

                if entry_key in json_data:
                    entry = json_data.get(entry_key)

                    if entry["Date"][5:7] == month_str:
                        table.add_row(
                            f"{json_data[entry_key]["expense_id"]}",
                            f"{json_data[entry_key]["Date"]}",
                            f"{json_data[entry_key]["Description"]}",
                            f"{json_data[entry_key]["Amount"]}",
                        )
            console.print(table)
            return

        for i in range(0, json_data["entry_no"] + 1):

            try:
                table.add_row(
                    f"{json_data[f"etry{i}"]["expense_id"]}",
                    f"{json_data[f"etry{i}"]["Date"]}",
                    f"{json_data[f"etry{i}"]["Description"]}",
                    f"{json_data[f"etry{i}"]["Amount"]}",
                )
            except:
                continue

        console.print(table)

    elif args.command == "summary":
        json_data = get_json_data()

        if not args.month:
            print(f"Total amount is {json_data["total_amount"]}")
            return

        if 1 <= args.month <= 12:
            monthly_total = 0
            month_str = f"{args.month:02d}"
            for i in range(json_data["entry_no"]):
                entry_key = f"etry{i}"

                if month_str == json_data[entry_key]["Date"][5:7]:
                    monthly_total += json_data[entry_key]["Amount"]

            print(
                f"montly income for {calendar.month_name[args.month]}:{monthly_total}"
            )

        else:
            print("enter a valid month")
            return


if __name__ == "__main__":
    main()
