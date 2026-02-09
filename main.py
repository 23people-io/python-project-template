def main():
    print("Hello from python-project-template!")
    a: str = "a"


if __name__ == "__main__":
    main()
    try:
        print(1 / 0)
    except ZeroDivisionError as e:
        print(f"Caught an exception: {e}")
