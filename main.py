from user_input import get_user_input_set, get_user_input_type, get_user_input_level
from data_processing import get_armor_upgrade_materials_from_csv, get_unique_armor_sets, display_materials, display_menu

def main():
    csv_file_path = "materials.csv"
    upgrades_from_csv = get_armor_upgrade_materials_from_csv(csv_file_path)

    # get all unique armor sets for option 2
    unique_armor_sets = get_unique_armor_sets(upgrades_from_csv)

    while True:
        display_menu()
        user_option = input("Enter your choice (1, 2, or 3): ")
        if user_option not in ['1', '2', '3']:
            print("Invalid option! Please enter 1, 2, or 3.")
            continue

        if user_option == '1':
            user_armor_set = get_user_input_set(get_unique_armor_sets(upgrades_from_csv))

            valid_armor_types_for_set = set()
            
            for armor_type, armor_set, _, _, _, _ in upgrades_from_csv:
                if armor_set.lower() == user_armor_set.lower():
                    valid_armor_types_for_set.add(armor_type.lower())

            if len(valid_armor_types_for_set) == 1:
                # some sets only have armor for one body part; this skips directly to the level prompt for those sets
                user_armor_type = valid_armor_types_for_set.pop()
                user_current_level = get_user_input_level()
            else:
                user_armor_type = get_user_input_type(valid_armor_types_for_set)
                user_current_level = get_user_input_level()

            display_materials(upgrades_from_csv, user_armor_type, user_armor_set, user_current_level)

            next_option = input("Enter 'x' to return to the options menu, or any key to exit!\n")
            if next_option.lower() == 'x':
                continue
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

if __name__ == "__main__":
    main()
