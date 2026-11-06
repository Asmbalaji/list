from input_handler import get_value

def update_element(numbers):

    print("\n========== UPDATE ELEMENT ==========")

    print("Current List:", numbers)

    index = int(input("Enter index: "))

    if 0 <= index < len(numbers):

        old_value = numbers[index]

        value = get_value()

        if value is not None:

            numbers[index] = value

            print("\n[ SUCCESS ] Updated!")
            print("Old Value:", old_value)
            print("New Value:", value)
            print("Updated List:", numbers)

    else:
        print("[ ERROR ] Invalid index!")