


def print_input_parameter(some_numer: int)-> str:
    print(f"The Input was: {some_numer}")


if __name__ == "__main__":
    print("Starting Program")

    # The types are just hints
    # There will be no checking at runtime and other Values will also be accepted (Pydantic will work differently)
    # Not even the return Value is checked
    print_input_parameter("dasd")
    print_input_parameter(83.65)
    print_input_parameter(23)