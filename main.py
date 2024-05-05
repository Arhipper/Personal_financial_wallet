import os
from datetime import datetime

file_path: str = 'data.txt'


class Wallet:
    """Class to Create Wallet"""

    def __init__(self) -> None:
        """Initiate Wallet"""
        self.finances: list = []

    def data_load(self) -> None:
        """Loading data"""
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                while line := file.readline():
                    rec: list = line.strip().split('|')
                    self.finances.append({
                        'date': rec[0],
                        'category': rec[1],
                        'amount': float(rec[2]),
                        'description': rec[3]
                    })

    def data_save(self) -> None:
        """Saving data"""
        with open(file_path, 'w') as file:
            for rec in self.finances:
                file.write(
                    f"{rec['date']}|{rec['category']}|{rec['amount']}|{rec['description']}|\n"
                )

    def show_balance(self) -> None:
        """Showing data"""
        incomes: float = round(sum(rec['amount'] for rec in self.finances if rec['category'] == 'income'), 2)
        expenses: float = round(sum(rec['amount'] for rec in self.finances if rec['category'] == 'expense'), 2)
        balance: float = incomes - expenses
        print(f'\nTotal Balance: {balance}')
        print(f'Total Incomes: {incomes}')
        print(f'Total Expenses: {expenses}\n')

    def add_rec(self, date: str, category: str, amount: float, description: str) -> None:
        """Adding an entry to the data"""
        self.finances.append({
            'date': date,
            'category': category,
            'amount': amount,
            'description': description
        })
        self.data_save()

    def edit_record(self, index: int, date: str, category: str, amount: float, description: str) -> None:
        """Changing the data entry"""
        if 0 <= index < len(self.finances):
            self.finances[index] = {
                "date": date,
                "category": category,
                "amount": amount,
                "description": description
            }
            self.data_save()
        else:
            print("Invalid index.")

    def search_records(self, category: str = None, date: str = None, amount: float = None) -> list:
        """Searching for a record in the data"""
        results: list = []
        count_index = 0
        for rec in self.finances:
            count_index += 1
            if ((not category or rec['category'] == category) and
                    (not date or rec['date'] == date) and
                    (not amount or rec['amount'] == amount)):
                results.append(({"index": count_index}, rec))
        return results


if __name__ == '__main__':
    my_wallet: Wallet = Wallet()
    my_wallet.data_load()

    while True:
        print('*' * 22)
        print("* 1. Show Balance    *")
        print("* 2. Add Record      *")
        print("* 3. Edit Record     *")
        print("* 4. Search Records  *")
        print("* 5. Exit            *")
        print('*' * 22)

        choice: str = input("Enter your choice: ")

        if choice == '1':
            my_wallet.show_balance()

        elif choice == '2':
            try:
                date: str = input("Enter date (YYYY-MM-DD) (default current date): ")
                if date == "":
                    date = datetime.now().strftime("%Y-%m-%d")
                    print(date)

                category: str = input("Enter category (income/expense) (default expenses): ")
                if category == "":
                    category = "expense"

                if (amount := input("Enter amount: ")) == "":
                    amount = 0.0
                else:
                    amount = float(amount)

                description: str = input("Enter description: ")
                if description == "":
                    description = "Empty"

            except ValueError:
                print("Invalid input format. Please enter valid values.")
                continue
            my_wallet.add_rec(date, category, amount, description)

        elif choice == '3':
            index: int = int(input("Enter index of the record to edit: "))
            date: str = input("Enter new date (YYYY-MM-DD): ")
            category: str = input("Enter new category (income/expense): ")
            amount: float = float(input("Enter new amount: "))
            description: str = input("Enter new description: ")
            my_wallet.edit_record(index, date, category, amount, description)

        elif choice == '4':
            category: str = input("Enter category to search (optional): ")
            date: str = input("Enter date to search (optional): ")
            if (amount := input("Enter amount to search (optional): ")) != "":
                amount = float(amount)
            results = my_wallet.search_records(category, date, amount)
            print("Search Results:")
            for result in results:
                print(result)

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please try again.")
