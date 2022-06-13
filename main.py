import random

options = ["R", "P", "S"]

computer_option = random.choice(options)

user_option = input("Rock (R), Paper (P) or Scissors (S)? ")

def play_game():
    if(user_option == computer_option):
        print("CPU: {}".format(computer_option))
        print("Player: {}".format(user_option))
        print("It's a tie. Play again.")

    else:
        #Computer choosing Rock.
        if(computer_option == "R"):
            if(user_option == "S"):
                print("CPU: {}".format(computer_option))
                print("Player: {}".format(user_option))
                print("Rock beats Scissors. The computer wins!")

            elif(user_option == "Paper"):
                print("CPU: {}".format(computer_option))
                print("Player: {}".format(user_option))
                print("Paper beats Rock. You win!")

        #Computer choosing Scissors.
        elif(computer_option == "S"):
            if(user_option == "R"):
                print("CPU: {}".format(computer_option))
                print("Player: {}".format(user_option))
                print("Rock beats Scissors. You win!")    

            elif(user_option == "P"):
                print("CPU: {}".format(computer_option))
                print("Player: {}".format(user_option))
                print("Scissors beats Paper. The computer wins!")    

        #Computer choosing Paper.
        elif(computer_option == "P"):
            if(user_option == "R"):
                print("CPU: {}".format(computer_option))
                print("Player: {}".format(user_option))
                print("Paper beats Rock. The computer wins!")

            elif(user_option == "S"):                  
                print("CPU: {}".format(computer_option))
                print("Player: {}".format(user_option))
                print("Scissors beats Paper. You win!")


if(user_option not in options):
    print("Error!\nYou can only pick R, S or P.")
    user_option = input("Rock (R), Paper (P) or Scissors (S)? ")
    play_game()
else:
    play_game()
