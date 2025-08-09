# Завдання 2
import re
from typing import Callable

def generator_numbers(text: str):
    for match in re.findall(r'\b\d+\.\d+\b', text):
        yield float(match)

def sum_profit(text: str, func: Callable):
    return sum(func(text))

if __name__ == "__main__":
    text = "Загальний дохід: 1000.01 основний, 27.45 додатковий, 324.00 ще."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")  # 1351.46
