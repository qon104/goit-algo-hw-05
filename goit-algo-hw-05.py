
# Завдання 1

def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

fib = caching_fibonacci()
print(fib(10))  # 55
print(fib(15))  # 610

# Завдання 2

import re
from typing import Callable

def generator_numbers(text: str):
    for match in re.findall(r'\b\d+\.\d+\b', text):
        yield float(match)

def sum_profit(text: str, func: Callable):
    return sum(func(text))

text = "Загальний дохід: 1000.01 основний, 27.45 додатковий, 324.00 ще."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")  # 1351.46

# Завдання 3

import sys
from collections import Counter

def parse_log_line(line: str) -> dict:
    parts = line.strip().split(' ', 3)
    if len(parts) < 4:
        return None
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": parts[3]
    }

def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                parsed = parse_log_line(line)
                if parsed:
                    logs.append(parsed)
    except FileNotFoundError:
        print("Файл не знайдено.")
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log["level"].lower() == level.lower(), logs))

def count_logs_by_level(logs: list) -> dict:
    levels = [log["level"] for log in logs]
    return dict(Counter(levels))

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<17}| {count}")

def main():
    if len(sys.argv) < 2:
        print("Вкажіть шлях до лог-файлу.")
        return

    file_path = sys.argv[1]
    level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level:
        filtered = filter_logs_by_level(logs, level)
        print(f"\nДеталі логів для рівня '{level.upper()}':")
        for log in filtered:
            print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    main()
    
# Завдання 4
 
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
    return wrapper

contacts = {}

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def get_phone(args, contacts):
    name = args[0]
    return contacts[name]

def show_all():
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    while True:
        command = input("Enter a command: ").strip().lower()
        if command == "exit":
            print("Good bye!")
            break
        elif command == "add":
            args = input("Enter name and phone: ").split()
            print(add_contact(args, contacts))
        elif command == "phone":
            args = input("Enter name: ").split()
            print(get_phone(args, contacts))
        elif command == "all":
            print(show_all())
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()