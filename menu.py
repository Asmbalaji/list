def main_menu():

    print("\n" + "=" * 45)
    print("       PYTHON LIST MANAGEMENT SYSTEM")
    print("=" * 45)

    print("              MAIN MENU")
    print("-" * 45)

    print("  [1]  Display List")
    print("  [2]  Insert Element")
    print("  [3]  Update Element")
    print("  [4]  Delete Element")
    print("  [5]  Exit Program")

    print("-" * 45)

    try:
        choice = int(input("  Enter your choice (1-5): "))
        return choice

    except ValueError:
        print("\n[ ERROR ] Please enter a valid number!")
        return 0