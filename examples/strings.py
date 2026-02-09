# Strings examples in Python


def main():
    # Basic string operations
    business_name = "23people"
    name_length = len(business_name)
    third_char = business_name[2]
    business_number = int(business_name[:2])

    print(f"Business name: {business_name}")
    print(f"Length of business name: {name_length}")
    print(f"Third character of business name: {third_char}")
    print(f"Business number extracted from name: {business_number}")

    concatenate_list_and_number = str([1, 2, 3]) + str(4)
    print(f"Concatenation of list and number as strings: {concatenate_list_and_number}")

    upper_business_name = business_name.upper()
    lower_business_name = business_name.lower()

    business_name_with_spaces = "     23people     "
    print(f"Business name without spaces: '{business_name_with_spaces.strip()}'")

    # Split and join strings

    information_text = "23 individuals, 16 female, 7 male"
    text_words = information_text.split(", ")
    print(f"Split information text into words: {text_words}")

    names = ["Jorge", "Alejandra", "Miguel", "Marcelo"]
    names_in_one_string = ", ".join(names)
    print(f"Names joined into one string: {names_in_one_string}")


if __name__ == "__main__":
    main()
