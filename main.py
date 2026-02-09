def main():
    print("Hello from python-project-template!")
    a: str = "a"
    print(a + 1)  # This will cause a type error, which should be caught by Ruff and Ty


if __name__ == "__main__":
    main()
