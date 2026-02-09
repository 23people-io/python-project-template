# Lists examples in Python


def main():
    empty_list = []

    numbers_list = [1, 2, 3, 10]

    multiple_typing_list = [1, "2", [1, 2], 3.4, {"five": 5}]

    # List Operators

    names = ["Jorge", "Marcelo", "Alejandra"]
    second_name = names[1]
    last_name = names[-1]
    print(f"Second name: {second_name}")
    print(f"Last name: {last_name}")

    concat_list = [1, 2, 4, 5] + [10, 20, 30]
    print(f"Concatenated list: {concat_list}")

    names.append("Juan")
    print(f"Names after appending: {names}")

    names.pop()
    print(f"Names after popping: {names}")

    # Slicing

    letters = ["a", "b", "c", "d"]

    first_two_letters = letters[:2]
    letters_between_index_1_and_3 = letters[1:3]
    all_but_first_letter = letters[1:]

    print(f"First two letters: {first_two_letters}")
    print(f"Letters between index 1 and 3: {letters_between_index_1_and_3}")
    print(f"All but first letter: {all_but_first_letter}")

    letters[2:] = ["w", "x", "y", "z"]
    print(f"Letters after slice assignment: {letters}")

    # Range
    my_range = range(3)
    init_end_range = range(4, 7)
    init_end_step_range = range(1, 10, 3)
    reversed_range = range(10, 1, -2)

    print(f"Range from 0 to 2: {list(my_range)}")
    print(f"Range from 4 to 6: {list(init_end_range)}")
    print(f"Range from 1 to 9 with step 3: {list(init_end_step_range)}")
    print(f"Reversed range from 10 to 2 with step -2: {list(reversed_range)}")

    inventory = [20, 15, 50, 30, 10]
    stock_adjustments = [5, -3, 0, -10, 2]

    for i in range(len(inventory)):
        if inventory[i] + stock_adjustments[i] < 0:
            print(f"Warning: Insufficient stock for item {i + 1}")
            continue
        inventory[i] += stock_adjustments[i]

    # Enumerate

    no_enum_list = ["hola", "mundo", "23people"]
    enum_list = list(enumerate(no_enum_list))
    print(f"Enumerated list: {enum_list}")

    # List Comprehensions

    words_list = ["hola", "mundo", "chao", "universo"]
    exclamations_word_list = []
    for word in words_list:
        exclamations_word_list.append(f"¡{word}!")

    exclamations_word_list_comp = [f"¡{word}!" for word in words_list]

    print(f"Exclamations word list without comprehension: {exclamations_word_list}")
    print(f"Exclamations word list with comprehension: {exclamations_word_list_comp}")

    exclamations_word_list_comp_conditional = [f"¡{word}!" for word in words_list if "a" in word]
    print(
        f"""Exclamations word list with comprehension and condition:
        {exclamations_word_list_comp_conditional}"""
    )

    # Sort method

    words_list = ["hola", "mundo", "chao", "universo"]

    words_list.sort()
    print(f"Sorted words list: {words_list}")

    words_list.sort(reverse=True)
    print(f"Sorted words list in reverse: {words_list}")

    words_list.sort(key=len)
    print(f"Sorted words list by length: {words_list}")

    words_list.sort(key=lambda x: x.lower(), reverse=True)
    print(f"Sorted words list by lowercase in reverse: {words_list}")

    # Map function

    def mult_by_2_plus_1(x: int) -> int:
        return x * 2 + 1

    numbers = [1, 2, 3, 4, 5]
    mapped_numbers = list(map(mult_by_2_plus_1, numbers))
    print(f"Mapped numbers: {mapped_numbers}")


if __name__ == "__main__":
    main()
