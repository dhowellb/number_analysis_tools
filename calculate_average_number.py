# Function para manghingi ng numbers at kunin ang average
def calculate_average_number():
    # Tracker para sa total na pinagsama-samang numbers
    total_sum = 0.0
    # Tracker kung ilang numbers na ang nai-type
    number_count = 0

    print("\033[96mEnter numbers (type any letter to stop):\033[0m")

    # Umpisahan ang infinite loop para sa unli-inputs
    while True:
        try:
            current_number = float(input("\033[96mEnter a number: \033[0m"))
            # Idagdag yung tinype na number sa running total natin
            total_sum = total_sum + current_number
            # Magdagdag ng 1 sa bilang ng numbers na nakuha natin
            number_count = number_count + 1
            
        except ValueError:
            # Shield on! Pag nag-type ng letter, stop na sa paghingi para makapag-compute.
            print("\033[93mInvalid input detected. Calculating average...\033[0m")
            break
    # I-check muna kung may nakuha ba talagang numbers (kung higit sa zero ang count)
    # TANDAAN: Siguraduhing pantay ang 'if' na ito sa 'while' na nasa taas!
    if number_count > 0:
        # Compute the average: Divide ang total sum sa kung ilang numbers ang tinype
        average_result = total_sum / number_count
        print("\033[92mThe average is:\033[0m", average_result)
    else:
        # Kung nag-letter agad sa umpisa pa lang kaya walang nai-compute:
        print("\033[91mNo valid numbers were entered.\033[0m")

# Ito yung magsisilbing switch para umandar yung buong script
if __name__ == "__main__":
    calculate_average_number()