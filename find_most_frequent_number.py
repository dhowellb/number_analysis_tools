# Function para humingi ng numbers at hanapin kung alin ang pinakamadalas maulit
def find_most_frequent_number():
    # Box para hakutin lahat ng numbers na ita-type
    number_list = []

    print("\033[96mEnter numbers (type any letter to stop):\033[0m")

    # Umpisahan ang infinite loop para sa unli-inputs
    while True:
        try:
            current_number = float(input("\033[96mEnter a number: \033[0m"))
            # Ihulog agad sa box natin yung number
            number_list.append(current_number)
            
        except ValueError:
            # Shield on! Pag nag-type ng letter, stop na sa paghingi para makapag-compute.
            print("\033[93mInvalid input detected. Calculating most frequent number...\033[0m")
            break
    # I-check muna kung may laman ba talaga yung list bago mag-compute
    # TANDAAN: Pantay dapat 'to sa 'while' loop sa taas
    if len(number_list) > 0:
        # Set muna natin yung default winner sa pinakaunang number sa list
        most_frequent = number_list[0]
        # Default bilang ng pagkakaulit ay zero
        max_count = 0
        
        # Isa-isang i-check ang bawat number sa loob ng list
        for current_number in number_list:
            # Bilangin kung ilang beses siya lumabas sa buong list
            current_count = number_list.count(current_number)
            
            # Kung mas marami ang bilang niya kaysa sa current winner natin...
            if current_count > max_count:
                # Papalitan natin ang records! Siya na ang bagong winner.
                max_count = current_count
                most_frequent = current_number
                
        # I-print ang final winner natin at kung ilang beses siya lumabas
        print("\033[92mThe number with the most duplicates is:\033[0m", most_frequent)
        print("\033[96mIt appeared\033[0m", max_count, "\033[96mtimes.\033[0m")
    else:
        # Pag letter agad ang tinype sa simula pa lang:
        print("\033[91mNo valid numbers were entered.\033[0m")

# Ang ating start button para umandar yung script
if __name__ == "__main__":
    find_most_frequent_number()