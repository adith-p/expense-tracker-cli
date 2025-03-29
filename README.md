# Expense Tracker CLI
https://roadmap.sh/projects/expense-tracker

A simple command-line interface tool for tracking personal expenses.

## Overview

Expense Tracker CLI allows you to easily add, update, delete, and view your expenses right from your terminal. It provides features to track expenses over time and generate monthly summaries.

## Features

- Add new expenses with descriptions and amounts
- Update existing expense entries
- Delete unwanted expenses
- List all expenses with optional filtering by month
- View expense summaries with monthly breakdowns
- Data persisted in JSON format for easy portability

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/expense-tracker-cli.git
   ```

2. Navigate to the project directory:
   ```
   cd expense-tracker-cli
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Adding an expense

```
python main.py add --description "Grocery shopping" --amount 50
```

### Updating an expense

```
python main.py update --id 0 --description "Weekly groceries" --amount 55
```

### Deleting an expense

```
python main.py delete --id 0
```

### Listing expenses

List all expenses:
```
python main.py list
```

List expenses for a specific month:
```
python main.py list --month 3
```

### Viewing expense summary

View total expenses:
```
python main.py summary
```

View summary for a specific month:
```
python main.py summary --month 3
```

## Command Reference

| Command | Description | Options |
|---------|-------------|---------|
| `add` | Add a new expense | `-d, --description` (required): Description of the expense<br>`--amount` (required): Amount spent |
| `update` | Update an existing expense | `--id` (required): ID of the expense to update<br>`-d, --description`: New description<br>`--amount`: New amount |
| `delete` | Delete an expense | `--id` (required): ID of the expense to delete |
| `list` | List all expenses | `-m, --month`: Filter by month (1-12) |
| `summary` | Show expense summary | `-m, --month`: Filter by month (1-12) |

## Data Storage

The application stores expense data in a `data.json` file in the same directory. The data structure includes:
- Total amount spent
- Number of entries
- Individual expense entries with IDs, dates, descriptions, and amounts

## Project Status

This project was created as part of the [roadmap.sh](https://roadmap.sh/projects/expense-tracker) project series.
