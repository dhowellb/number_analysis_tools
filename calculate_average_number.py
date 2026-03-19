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