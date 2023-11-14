data_file_path = "data.txt"

def load_data():
    try:
        with open(data_file_path, 'r') as file:
            data = [eval(line.strip()) for line in file.readlines()]
        return data
    except FileNotFoundError:
        return []

def save_data(data):
    with open(data_file_path, 'w') as file:
        for entry in data:
            file.write(str(entry) + '\n')

def add_data():
    data = load_data()
    new_entry = {}
    for key in input("Enter keys (comma-separated): ").split(','):
        value = input(f"Enter value for {key}: ")
        new_entry[key.strip()] = value.strip()
    data.append(new_entry)
    save_data(data)
    print("Data has been successfully added.")

def retrieve_data():
    data = load_data()
    if not data:
        print("No data found.")
    else:
        print("Stored Data:")
        for entry in data:
            print(entry)

def update_data():
    data = load_data()
    if not data:
        print("No data to update.")
        return

    key_to_update = input("Enter key to update: ")
    value_to_update = input(f"Enter the new value for {key_to_update}: ")

    updated = False
    for entry in data:
        if key_to_update in entry:
            entry[key_to_update] = value_to_update
            updated = True

    if updated:
        save_data(data)
        print("Data has been successfully updated.")
    else:
        print(f"No data found with key: {key_to_update}")

def delete_data():
    data = load_data()
    if not data:
        print("No data found.")
        return

    key_to_delete = input("Enter key to delete: ")
    data = [entry for entry in data if key_to_delete not in entry]

    save_data(data)
    print("Data has been successfully deleted.")

while True:
    try:
        print("\nMENU")
        print("1. Add Data")
        print("2. Retrieve Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_data()
        elif choice == '2':
            retrieve_data()
        elif choice == '3':
            update_data()
        elif choice == '4':
            delete_data()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
    except Exception as e:
        print(f"Error: {e}")

