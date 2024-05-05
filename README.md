# Personal Financial Wallet

This application serves as a personal financial wallet to track income and expenses. Below is the detailed functionality of the application:

## Features

1. **Show Balance**
   - This option displays the total balance along with the total incomes and expenses.

2. **Add Record**
   - Allows users to add a new financial record with the following details:
     - Date (default: current date if not provided)
     - Category (income/expense) (default: expense if not provided)
     - Amount
     - Description (default: "Empty" if not provided)

3. **Edit Record**
   - Enables users to modify an existing financial record by providing the index of the record and updating the following details:
     - Date
     - Category
     - Amount
     - Description

4. **Search Records**
   - Provides the ability to search for specific financial records based on the following criteria:
     - Category (optional)
     - Date (optional)
     - Amount (optional)

5. **Exit**
   - Exits the application.

## Implementation

The application is implemented using Python. It consists of a `Wallet` class with the following methods:

- `data_load`: Loads existing financial records from a file.
- `data_save`: Saves financial records to a file.
- `show_balance`: Displays the total balance, total incomes, and total expenses.
- `add_rec`: Adds a new financial record.
- `edit_record`: Modifies an existing financial record.
- `search_records`: Searches for specific financial records based on provided criteria.

The application runs in a loop, displaying a menu of options to the user. The user can choose an option by entering the corresponding number. The application handles invalid inputs gracefully and prompts the user to enter valid values.
