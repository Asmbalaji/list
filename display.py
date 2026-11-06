def display_list(numbers):

    print("\n========== DISPLAY LIST ==========")

    if not numbers:
        print("[ INFO ] List is empty")

    else:

        for index, value in enumerate(numbers):

            print(
                f"Index: {index} | "
                f"Value: {value} | "
                f"Type: {type(value).__name__}"
            )

        print("\nTotal Elements:", len(numbers))

    print("==================================")