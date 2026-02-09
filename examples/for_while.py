# For and while loop examples in Python


def main():
    name = "Juan"
    name_vowels = []

    vowels = ["a", "e", "i", "o", "u"]
    for char in name:
        if char in vowels:
            name_vowels.append(char)

    print(f"Vowels in the name {name}: {name_vowels}")

    number = 0
    for i in range(5):
        number += i

    print(f"Sum of numbers from 0 to 4: {number}")

    i = 0
    while i < 5:
        i += 1

    print(f"Final value of i after while loop: {i}")


if __name__ == "__main__":
    main()
