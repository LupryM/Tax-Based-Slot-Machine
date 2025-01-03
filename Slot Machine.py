import random  # To generate slot machine values randomly

# 3 x 3 slot machine with 3 Rows, 3 in a Row = win

# Declare Global Constants
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

rows = 3
cols = 3

# 4 Symbols In A Column
symbol_count = {"A": 2, "B": 4, "C": 6, "D": 8}  # 2 As, 4 Bs, 6 Cs
symbol_value = {"A": 5, "B": 4, "C": 3, "D": 2}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(lines + 1)

    return winnings, winning_lines


def get_slot_machine_spins(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):  # _ for when you don't care about the count in a loop
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]  # : is a copy operator to prevent from altering original list
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        amount = input("What would you like to deposit? R ")

        # Check if amount is a number
        if amount.isdigit():
            amount = int(amount)  # int() converts the string to an integer
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a valid number.")
    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter Number Of Lines to Bet On (1-" + str(
            MAX_LINES) + ")? ")  # Adding number to a string causes exception

        # Check if lines is a number
        if lines.isdigit():
            lines = int(lines)  # int() converts the string to an integer
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("lines must be between 1-" + str(MAX_LINES) + ".")
        else:
            print("Please enter a valid number.")

    return lines


def get_bet():
    while True:
        amount = input("How  much would you like to bet)? ")  # Adding number to a string causes exception

        # Check if lines is a number
        if amount.isdigit():
            amount = int(amount)  # int() converts the string to an integer
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between R{MIN_BET} - R{MAX_BET}.")  # f string converts any variable to string
        else:
            print("Please enter a valid number.")
    return amount


def spin(balance):
    lines = get_number_of_lines()

    # Check that balance is greater that bet
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You have insufficient funds to place that bet, your current balance is: R{balance}")
        else:
            break

    print(f"You are betting R{bet} on {lines} lines, Your Total bet is equal to: R{total_bet}")

    slots = get_slot_machine_spins(rows, cols, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won R{winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is R{balance}")
        answer = input("Press enter to play (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with R{balance}")


main()
