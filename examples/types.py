class Animal:
    pass


class Dog(Animal):
    pass


def main():
    print("Type of 1:", type(1))  # Output: <class 'int'>
    print("Type of '1'", type("1"))  # Output: <class 'str'>

    print("Is 1 an instance of int?", isinstance(1, int))
    print("Is '1' an instance of int?", isinstance("1", int))

    print(
        "Is 'hola mundo' an instance of str or bool?",
        isinstance("hola mundo", (str, bool)),
    )

    my_dog = Dog()
    print("Is my_dog an object of exactly type Animal?", type(my_dog) == Animal)
    print("Is my_dog an instance of Animal?", isinstance(my_dog, Animal))


if __name__ == "__main__":
    main()
