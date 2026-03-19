# Function para unli-hingi ng numbers at hanapin ang pinakamataas
def find_highest_number():
    # Start tayo sa 'None' (wala pang laman) kasi wala pa namang tina-type si user
    highest_number = None

    print("\033[96mEnter numbers (type any letter to stop):\033[0m")

    # Umpisahan na ang infinite loop
    while True:
        try:
            current_number = float(input("\033[96mEnter a number: \033[0m"))
            
            # Kung 'None' pa siya (unang number) OR mas mataas yung bagong type...
            # Papalitan natin yung record ng highest_number!
            if highest_number == None or current_number > highest_number:
                highest_number = current_number
                
        except ValueError:
            # Shield on! Pag letter ang tinype, break na agad sa loop para makapag-print.
            print("\033[93mInvalid input detected. Stopping program.\033[0m")
            break
    # Bago mag-print, i-check muna kung may pumasok ba talagang number
    # TANDAAN: Siguraduhing pantay 'to sa 'while' loop sa taas para walang error
    if highest_number != None:
        print("\033[92mThe highest number entered is:\033[0m", highest_number)
    else:
        # Kung nag-type agad ng letter sa umpisa pa lang:
        print("\033[91mNo valid numbers were entered.\033[0m")

# Ito yung magsisilbing switch para umandar yung script
if __name__ == "__main__":
    find_highest_number()