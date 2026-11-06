def get_value():

    print("\nSelect Data Type")
    print("1. Integer")
    print("2. Float")
    print("3. String")
    print("4. Boolean")

    choice = input("Enter your choice: ")

    if choice == "1":
        return int(input("Enter integer: "))

    elif choice == "2":
        return float(input("Enter float: "))

    elif choice == "3":
        return input("Enter string: ")

    elif choice == "4":
        value = input("Enter True or False: ").lower()

        if value == "true":
            return True
        elif value == "false":
            return False
        else:
            print("Invalid Boolean value")
            return None

    else:
        print("Invalid choice")
        return None