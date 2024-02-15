def get_user_input_set(valid_armor_sets):
    while True:
        user_armor_set = input("Enter the armor set: ").lower()
        if validate_armor_set(user_armor_set, valid_armor_sets):
            return user_armor_set
        else:
            print("\nInvalid set! Please try again.\n")

def get_user_input_type(valid_armor_types_for_set):
    while True:
        user_armor_type = input("Enter the armor type (head, body, or legs): ").lower()
        if validate_armor_type(user_armor_type, valid_armor_types_for_set):
            return user_armor_type
        else:
            print("\nInvalid type! Please enter head, body, or legs.\n")

def get_user_input_level():
    while True:
        user_current_level_str = input("Enter the upgrade level (1-4): ")
        if user_current_level_str.isdigit() and 1 <= int(user_current_level_str) <= 4:
            return int(user_current_level_str)
        else:
            print("\nInvalid level! Please enter a number from 1 to 4.\n")

def validate_armor_set(user_armor_set, valid_armor_sets):
    return user_armor_set.lower() in valid_armor_sets

def validate_armor_type(user_armor_type, valid_armor_types_for_set):
    return user_armor_type.lower() in valid_armor_types_for_set