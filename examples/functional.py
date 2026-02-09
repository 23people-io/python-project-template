# Functional programming example in Python

from functools import reduce


def say_hi(name: str) -> str:
    return f"Hi, {name}!"


def main():
    first_class_greet = say_hi
    print(first_class_greet("Marcelo"))

    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(map(lambda x: x**2, numbers))
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    numbers_sum = reduce(lambda x, y: x + y, numbers)

    print(f"Squared numbers: {squared_numbers}")
    print(f"Even numbers: {even_numbers}")
    print(f"Sum of numbers: {numbers_sum}")


if __name__ == "__main__":
    main()
