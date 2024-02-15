import csv

def get_armor_upgrade_materials_from_csv(filename):
    armor_upgrade_data = []

    with open(filename, 'r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            armor_type = row['Type']
            armor_set = row['Set']
            armor_piece = row['Piece']
            current_level_str = row['Level']
            current_level = int(current_level_str)
            material = row['Material']
            quantity = int(row['Quantity'])

            armor_upgrade_data.append((armor_type, armor_set, armor_piece, current_level, material, quantity))

    return armor_upgrade_data

def get_unique_armor_sets(upgrades_data):
    return set(armor_set for _, armor_set, _, _, _, _ in upgrades_data)

csv_file_path = "../materials.csv"
upgrades_from_csv = get_armor_upgrade_materials_from_csv(csv_file_path)

# get all unique armor sets for option 2
unique_armor_sets = get_unique_armor_sets(upgrades_from_csv)

# main menu
while True:
    # display menu options
    print("\n~~~~~~TOTK UPGRADE MATERIALS LIST~~~~~~")
    print("\nOptions:")
    print("1. Use material tracker")
    print("2. View available sets")
    print("3. Exit\n")

    user_option = input("Enter your choice (1, 2, or 3): ")

    if user_option == '1':
        user_armor_type = input("\nEnter the armor type (head, body, or legs): ")
        user_armor_set = input("Enter the armor set: ")

        # ensuring level input is an int value so nothing breaks... hopefully
        while True:
            user_current_level_str = input("Enter the upgrade level (1-4): ")
            
            if user_current_level_str.isdigit():
                user_current_level = int(user_current_level_str)
                break
            else:
                print("Invalid level! Please enter a number from 1 to 4.")

        # check if user input exists in the csv
        found_armor_set = user_armor_set.lower() in {set_name.lower() for set_name in unique_armor_sets}
        found_armor_type = any(user_armor_type.lower() == armor[0].lower() for armor in upgrades_from_csv)
        found_level = any(user_current_level == armor[3] for armor in upgrades_from_csv)

        # error displays
        if not found_armor_set:
            print(f"\nError: Armor set '{user_armor_set}' is invalid.")
        if not found_armor_type:
            print(f"\nError: Armor type '{user_armor_type}' is invalid.")
        if not found_level:
            print(f"\nError: Level '{user_current_level}' is invalid.")

        # accumulate materials for upgrade
        upgrade_materials = []
        current_armor_piece = None 

        for armor_type, armor_set, armor_piece, current_level, material, quantity in upgrades_from_csv:
            if (
                armor_type.lower() == user_armor_type.lower()
                and armor_set.lower() == user_armor_set.lower()
                and current_level == user_current_level
            ):
                if current_armor_piece is None:
                    current_armor_piece = armor_piece

                upgrade_materials.append(f"{quantity} {material}")

        # display the material list from the csv
        if current_armor_piece and upgrade_materials:
            print("\n~~~~~~~~~~~~")
            print(f"\nMaterials needed to upgrade {current_armor_piece} to level {user_current_level}:")
            print("\n".join(upgrade_materials))
            print("\n~~~~~~~~~~~~\n")

        # back to menu or get out
        next_option = input("Enter 'menu' to return to the options menu, or any key to exit!\n")

        if next_option.lower() == 'menu':
            continue # takes user back to menu
        else:
            print("\nExiting the material tracker...\n")
            break

    elif user_option == '2':
        # display all the armor sets
        print("\n~~~~~~Available Armor Sets~~~~~~\n")
        for armor_set in unique_armor_sets:
            print(armor_set)
        print("~~~~~~~~~~~~\n")
        # bail
        back_option = input("\nEnter 'x' to go back to the main menu or any other key to exit: ")
        if back_option.lower() != 'x':
            break

    elif user_option == '3':
        print("\nExiting the material tracker...\n")
        break

    else:
        print("Invalid option! Please enter 1, 2, or 3.")
