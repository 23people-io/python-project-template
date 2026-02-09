# Object-Oriented Programming (OOP) example in Python


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Hello, my name is {self.name} and I am {self.age} years old."


def main():
    person = Person("Marcelo", 30)
    my_greet = person.greet()
    print(my_greet)


if __name__ == "__main__":
    main()
