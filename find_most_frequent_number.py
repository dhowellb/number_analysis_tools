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