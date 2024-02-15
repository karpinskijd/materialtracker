import csv

def get_armor_upgrade_materials_from_csv(filename):
    armor_upgrade_data = []

    try:
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
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred while reading the CSV file: {e}")

    return armor_upgrade_data

def get_unique_armor_sets(upgrades_data):
    return set(armor_set.lower() for _, armor_set, _, _, _, _ in upgrades_data)

def display_materials(upgrades_data, user_armor_type, user_armor_set, user_current_level):
    found_armor_set = user_armor_set.lower() in {set_name.lower() for set_name in get_unique_armor_sets(upgrades_data)}
    found_armor_type = any(user_armor_type.lower() == armor[0].lower() for armor in upgrades_data)
    found_level = any(user_current_level == armor[3] for armor in upgrades_data)

    if not found_armor_set:
        print(f"\nError: Armor set '{user_armor_set}' is invalid.")
    if not found_armor_type:
        print(f"\nError: Armor type '{user_armor_type}' is invalid.")
    if not found_level:
        print(f"\nError: Level '{user_current_level}' is invalid.")

    valid_armor_types_for_set = set()
    
    for armor_type, armor_set, _, _, _, _ in upgrades_data:
        if armor_set.lower() == user_armor_set.lower():
            valid_armor_types_for_set.add(armor_type.lower())

    upgrade_materials = []
    current_armor_piece = None

    for armor_type, armor_set, armor_piece, current_level, material, quantity in upgrades_data:
        if (
            armor_type.lower() == user_armor_type.lower()
            and armor_set.lower() == user_armor_set.lower()
            and current_level == user_current_level
        ):
            if current_armor_piece is None:
                current_armor_piece = armor_piece

            upgrade_materials.append(f"{quantity} {material}")

    if current_armor_piece and upgrade_materials:
        print("\n~~~~~~~~~~~~")
        print(f"\nMaterials needed to upgrade {current_armor_piece} to level {user_current_level}:")
        print("\n".join(upgrade_materials))
        print("\n~~~~~~~~~~~~\n")

def display_menu():
    print("\n~~~~~~TOTK UPGRADE MATERIALS LIST~~~~~~")
    print("\nOptions:")
    print("1. Use material tracker")
    print("2. View available sets")
    print("3. Exit\n")