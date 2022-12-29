# defining function which will take input from user as a parameter and then
import random


def program(parameter):
    user_score = 0
    cpu_score = 0
    tie = 0

    # It will check wether user had started or not
    if parameter == "start" or parameter == "yes":
        gameover = "start"
        print(f"\nChoose your choice from--> \t\t{choice}")
        print("Enter your choice or enter 'finish' to end the game : \t")
        while gameover != "finish":
            print(
                f"User's score: {user_score}                     Match ties: {tie}                                    CPU's score: {cpu_score}")
            # assigning random value to cpu from choice
            cpu_choice = random.choice(choice).lower()
            # Taking user's choice
            user_choice = input("Enter your choice : \t").lower().strip()
            # assingning user's choice to gameover
            gameover = user_choice
            # Comparing user's choice to cpu's choice if both are same it will print tie and increase tie by 1
            if user_choice == cpu_choice:
                print(f"CPU's choice      :     {cpu_choice}")
                print(f"Tie\n")
                tie += 1
            # checking all the conditions where cpu can win and increasing cpu's score by 1
            elif user_choice == "rock" and cpu_choice == "paper" or user_choice == "scissor" and cpu_choice == "rock" or user_choice == "paper" and cpu_choice == "scissor":
                print(f"CPU's choice      :     {cpu_choice}")
                print("CPU wins \n")
                cpu_score += 1
            # checking all the conditions where user can win and increasing user's score by 1
            elif user_choice == "rock" and cpu_choice == "scissor" or user_choice == "scissor" and cpu_choice == "paper" or user_choice == "paper" and cpu_choice == "rock":
                print(f"CPU's choice      :     {cpu_choice}")
                print("You win!! Congo.....\n")
                user_score += 1
            # if user enterd finish
            elif user_choice == "finish":
                break

            # if user entered any other input except choice
            elif user_choice not in choice:
                print("Please enter correct input")

        return user_score, cpu_score, tie

    elif parameter == "no":
        return "See you again !!"
    else:
        return "Oops! wrong input :"
# -----------------------------------------------------------------------------------------------------------------
# A function which will print the result


def result(user_score, cpu_score):
    # Checking condition is user has more points than cpu
    if user_score > cpu_score:
        print(f"\nHurrah!!! You win \n")
    # If they both got equal points
    elif user_score == cpu_score:
        print(f"\nMatch tie\n")
    else:
        print(f"\nBetter luck next time!!\n")
        # It will print the result
    print(f"Your Score : {user_score}\t\t\t\tCPU score : {cpu_score}")
    return "\nThanks for playing !!"


# ------------------------------------------------------------------------------
choice = ["rock", "paper", "scissor"]
print("Hello there!\nWelcome to the Rock Paper Scissor game\n\n")
game = input("Press start to initiate the game : \n").strip().lower()

if game == "start":
    # function will return all the values in tuple so converting them into list by which we can iterate
    res = list(program(game))
    # assigning value to the user cpu and tie
    user_score, cpu_score, tie = res[0], res[1], res[2]

    # If user finish the game immediate after starting then
    count = 0
    while user_score == 0 and cpu_score == 0 and tie == 0 and game == "start" or game == "yes":
        count += 1
        print("\nWant to play again?\n")
        game = input("Yes or No \n: ").strip().lower()
        # checking wether user want to play again or not
        if game == "yes":
            resu = list(program(game))
            user_score, cpu_score, tie = resu[0], resu[1], resu[2]
            result(user_score, cpu_score)

        elif game == "no":
            print(program(game))
            break
        else:
            print("Wrong input")

    if count == 0:
        print(result(user_score, cpu_score))

else:
    print(program(game))

# Program finished
