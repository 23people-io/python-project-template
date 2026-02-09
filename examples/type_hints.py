def no_type_hints_average(numbers):
    total_sum = sum(numbers)
    number_of_elements = len(numbers)
    return total_sum / number_of_elements


def type_hints_average(numbers: list[int]) -> float:
    total_sum = sum(numbers)
    number_of_elements = len(numbers)
    return total_sum / number_of_elements


def main():
    # Without type hints, the following calls will not raise any errors, but they will cause
    # runtime errors
    no_type_hints_average("hola mundo")
    no_type_hints_average(["hola", "mundo"])

    average_1 = no_type_hints_average([1, 2, 3, 4]) + "hola mundo"

    # With type hints, static type checkers like Ruff and Ty will catch these errors before runtime
    type_hints_average("hola mundo")
    type_hints_average(["hola", "mundo"])
    average_2 = type_hints_average([1, 2, 3, 4]) + "hola mundo"


if __name__ == "__main__":
    main()
