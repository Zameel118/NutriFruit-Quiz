import json

#Ensures user enters non-whitespace input.
def input_something(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value

#Ensures user enters a valid float >= 0.
def input_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("Invalid input! Enter a number greater than or equal to 0.")
        except ValueError:
            print("Invalid input! Enter a valid number.")

#Saves the data list to data.txt in JSON format.
def save_data(data):
    with open("data.txt", "w") as file:
        json.dump(data, file, indent=2)


try:
    #Try to load existing data from file
    with open("data.txt", "r") as file:
        data = json.load(file)
except:
    data = []

print("Welcome to the Fruit Quiz Admin Program.")

while True:
    print("\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.")
    choice = input("> ").lower()

    if choice == "a":
        #Ensures no duplicate name before collecting other data
        name = input_something("Enter fruit name: ")
        exists = any(fruit["name"].lower() == name.lower() for fruit in data)
        if exists:
            print(f'"{name}" already exists in the data.')
            continue
            
        #Collect nutritional information
        print(f'\nIn 100 grams of {name}, how many...')
        fruit = {
            "name": name,
            "energy": input_float("Calories are there?: "),
            "fibre": input_float("Grams of fibre are there?: "),
            "sugar": input_float("Grams of sugar are there?: "),
            "potassium": input_float("Milligrams of potassium are there?: ")
        }
        data.append(fruit)
        save_data(data)
        print("Fruit added!")

    elif choice == "l":
        if not data:
            print("No fruit saved")
        else:
            print('List of fruit:')
            for i, fruit in enumerate(data, 1):
                print(f"{i}) {fruit['name']}")

    elif choice == "s":
        if not data:
            print("No fruit saved")
        else:
            term = input_something("Enter search term: ").lower()
            found = False
            print('Search results:')
            for i, fruit in enumerate(data, 1):
                if term in fruit["name"].lower():
                    print(f"{i}) {fruit['name']}")
                    found = True
            if not found:
                print("No results found")

    elif choice == "v":
        if not data:
            print("No fruit saved")
        else:
            try:
                index = int(input('Fruit number to view: ')) - 1
                if 0 <= index < len(data):
                    fruit = data[index]
                    print(f"\nNutritional information for 100 grams of {fruit['name']}:")
                    print(f"Energy: {fruit['energy']} calories")
                    print(f"Fibre: {fruit['fibre']} grams")
                    print(f"Sugar: {fruit['sugar']} grams")
                    print(f"Potassium: {fruit['potassium']} milligrams")
                else:
                    print("Invalid index number")
            except ValueError:
                print("Invalid index number")

    elif choice == "d":
        if not data:
            print("No fruit saved")
        else:
            try:
                index = int(input("Fruit number to delete: ")) - 1
                if 0 <= index < len(data):
                    del data[index]
                    save_data(data)
                    print("Fruit deleted")
                else:
                    print("Invalid index number")
            except ValueError:
                print("Invalid index number")

    elif choice == "q":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
        if not data:
            print("Enter 'a' to add your first fruit!")
