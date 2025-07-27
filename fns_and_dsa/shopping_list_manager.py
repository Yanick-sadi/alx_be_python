shopping_list = []

def add_item(shopping_list, item):
    shopping_list.append(item)
    print(f"'{item} added to shopping_list'")

def remove_item(shopping_list, item):
    try:
        shopping_list.remove(item)
        print(f"'{item} removed from shopping list'")
    except ValueError:
        print(f"'{item} not found in the list")

def display_list():
    if not shopping_list:
        print("The list is empty")
    else:
        print("current list")
        for index, item in enumerate(shopping_list,start=1):
            print(f"{index} . {item}")

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == '1':
            item = input("Enter item to add: ").strip()
            pass
        elif choice == '2':
            item = input("enter item to remove").strip()
            pass
        elif choice == '3':
            display_list()
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()