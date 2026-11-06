def delete_element(numbers):

    print("\n========== DELETE ELEMENT ==========")

    if len(numbers) == 0:
        print("[ INFO ] The list is empty. Nothing to delete.")

    else:
        print("Current List:", numbers)

        index = int(input("Enter index to delete: "))

        if 0 <= index < len(numbers):

            deleted_value = numbers.pop(index)

            print("\n[ SUCCESS ] Element deleted successfully!")
            print("Deleted Value :", deleted_value)
            print("Deleted Index :", index)
            print("Updated List  :", numbers)

        else:
            print("\n[ ERROR ] Invalid index!")
            print("Valid index range: 0 to", len(numbers) - 1)

    print("====================================")