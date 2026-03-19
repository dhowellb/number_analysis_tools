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