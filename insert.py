from input_handler import get_value

def insert_element(numbers):

    print("\n========== INSERT ELEMENT ==========")

    print("Current List:", numbers)

    value = get_value()

    if value is not None:

        index = int(input("Enter index: "))

        if 0 <= index <= len(numbers):

            numbers.insert(index, value)

            print("\n[ SUCCESS ] Element inserted!")
            print("Inserted Value:", value)
            print("Data Type:", type(value).__name__)
            print("Updated List:", numbers)

        else:
            print("[ ERROR ] Invalid index!")