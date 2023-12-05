# This is a simple math quiz add and subtract with a random number genertator
# 12/05/2023
# CTI-110 P5HW - Math Quiz
# Stephen Hughes
#

import random
class Text:
    BOLD_START = '\033[1m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

def generate_numbers():
    first = random.randint(1, 250)
    second = random.randint(1, 250)
    return first, second

def add_numbers():
    first, second = generate_numbers()
    result = first + second
    guess = int(input(f"  {first}\n+ {second}\n\nEnter answer. "))
    guesses = 1
    while guess != result:
        if guess < result:
            guess = int(input("Sorry, guess is too low.\nTry again: "))
        else:
            guess = int(input("Sorry, guess is too high.\nTry again: "))
        guesses += 1
    print("--------------------")
    print(Text.GREEN +"Congratulations!!!!" + Text.END + "Your answer is correct.")
    print(f"Number of guesses: {guesses}")
    print("--------------------")
def subtract_numbers():
    first, second = generate_numbers()
    if first < second:
        first, second = second, first
    result = first - second
    guess = int(input(f"  {first}\n- {second}\nEnter answer. "))
    guesses = 1
    while guess != result:
        guess = int(input("Sorry, guess is incorrect.\nTry again: "))
        guesses += 1
    print("--------------------")
    print(Text.GREEN +"Congratulations!!!!" + Text.END + "Your answer is correct.")
    print(f"Number of guesses: {guesses}")
    print("--------------------")

def display_menu():
    print("")
    print("MAIN MENU")
    print("--------------------")
    print(Text.BOLD_START +"1."+ Text.END + Text.GREEN +"Adding Random Numbers"+ Text.END)
    print(Text.BOLD_START +"2."+ Text.END + Text.YELLOW +"Subtracting Random Numbers"+ Text.END)
    print(Text.BOLD_START +"3."+ Text.END + Text.RED +"Exit"+ Text.END)
    print("--------------------")

def main():
    print(Text.RED + "Welcome to Math Quiz!" + Text.END)
    while True:
        display_menu()
        choice = input("Please choose one of the menu options: ")
        if choice == "1":
            add_numbers()
        elif choice == "2":
            subtract_numbers()
        elif choice == "3":
            print("Thank you for playing...Bye!!")
            print("--------------------")
            break
        else:
            print(Text.RED +"Error: not a vaild enty.\nPlease choose again."+ Text.END)
            print("--------------------")

if __name__ == "__main__":
    main()

