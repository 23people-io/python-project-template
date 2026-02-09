# Boolean operators examples in Python


def main():
    and_operation = 10 < 2 and (10 - 1) == 9
    or_operation = 10 < 2 or (10 - 1) == 9
    not_operation = not (10 <= 10)

    in_operation_1 = "a" in "Marcelo"
    in_operation_2 = 10 in [1, 2, 3, 4]

    print(f"AND - 10 < 2 and (10 - 1) == 9: {and_operation}")
    print(f"OR - 10 < 2 or (10 - 1) == 9: {or_operation}")
    print(f"NOT - not (10 <= 10): {not_operation}")

    print(f"IN - 'a' in Marcelo: {in_operation_1}")
    print(f"IN - 10 in [1, 2, 3, 4]: {in_operation_2}")


if __name__ == "__main__":
    main()
