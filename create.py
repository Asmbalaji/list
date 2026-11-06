from input_handler import get_value

def create_list():

    print("\n========== CREATE LIST ==========")

    numbers = []

    n = int(input("How many elements? "))

    for i in range(n):

        print(f"\nElement {i + 1}")

        value = get_value()

        if value is not None:
            numbers.append(value)

    print("\n[ SUCCESS ] List created!")
    print("Created List:", numbers)

    return numbers