from create import create_list
from display import display_list
from insert import insert_element
from update import update_element
from delete import delete_element
from menu import main_menu

numbers = create_list()

while True:

    choice = main_menu()

    if choice == 1:
        display_list(numbers)

    elif choice == 2:
        insert_element(numbers)

    elif choice == 3:
        update_element(numbers)

    elif choice == 4:
        delete_element(numbers)

    elif choice == 5:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")