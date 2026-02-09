# Sets example in Python
def main():
    message = "23people"
    message_chars_list = list(message)
    print(f"List of characters in the message: {message_chars_list}")

    message_chars_set = set(message)
    print(f"Set of unique characters in the message: {message_chars_set}")

    my_set = set()  # {} is a dictionary, not a set
    my_set.add(1)
    print(f"My set after adding 1: {my_set}")

    my_second_set = {1, 2, 3}
    my_second_set.remove(2)
    print(f"My second set after removing 2: {my_second_set}")


if __name__ == "__main__":
    main()
