# Function para manghingi ng 10 numbers at hanapin kung alin ang may mga kaparehas
def display_duplicate_numbers():
    # Gumawa ng box para sa lahat ng ita-type na numbers
    number_list = []
    # Gumawa ng hiwalay na box para ilista yung mga nakita nating may duplicate
    duplicate_list = []

    # Loop para manghingi ng exactly 10 numbers
    for i in range(10):
        current_number = float(input("\033[96mEnter number " + str(i + 1) + ": \033[0m"))
        # Ihulog yung number sa main box natin
        number_list.append(current_number)
    print("\033[92mNumbers with duplicates:\033[0m")

    # Isa-isahin natin i-check yung mga numbers sa main box
    for current_number in number_list:
        # Kung higit sa isa ang bilang niya (> 1) AT wala pa siya sa duplicate_list tracker natin...
        if number_list.count(current_number) > 1 and current_number not in duplicate_list:
            # Ilista natin sa tracker para hindi siya ma-print nang paulit-ulit
            duplicate_list.append(current_number)
            # I-print yung number na na-detect nating may kaparehas
            print("\033[93m" + str(current_number) + "\033[0m")

# Ito yung magsisilbing switch para umandar yung buong script
if __name__ == "__main__":
    display_duplicate_numbers()