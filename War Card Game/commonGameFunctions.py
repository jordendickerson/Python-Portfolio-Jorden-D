
die_size = 6

# ask yes no question
def ask_yes_no(question):
    """asks the user  yes or no"""
    answer = input(question)
    if("y" in answer.lower()) and ("n" in answer.lower()):
        print("not a valid option")

    elif ("y" in answer.lower()):
        answer = "yes"
        return answer
    elif ("n" in answer.lower()):
        answer = "no"
        return answer
    else:
        print("not a valid option")

def ask_number(question):
    answer = input(question)
    return answer
# flip coin roll dice
def roll_dice(die_size):
    """Rolls a dice to get 1, 2, 3, 4, 5, or 6"""
    import random
    roll = random.randint(1,die_size)
    return roll
def flip_coin():
    """Flips a coin and returns Heads or Tails"""
    import random
    result = random.choice["Heads", "Tails"]
    return result
# get number in range

lowNum = 0
highNum = 0
number = 0

def number_in_range(lowNum, highNum, number):
    """Allows user to enter a range of numbers and chooses a random number from it"""
    import random
    while True:
        try:
            lowNum = int(input("Enter the lowest number in the range: "))
            highNum = int(input("Enter the highest number in the range: "))
            number = random.randint(lowNum, highNum)
            print(number)
        except:
            print("That's not a valid option!")


def get_number_in_range(question, low, high):
    """Has the user choose a number between a low and high"""
    while True:
        answer = input(question)
        try:
            answer = int(answer)
            if answer >= low:
                if answer <= high:
                    return answer
                else:
                    print("Too high!")
            else:
                print("Too low!")
        except:
            print("That's not a valid option!")

def menu(prompt, options):
    """takes in a list of options and asks the player which they would like to do."""
    print(prompt)
    while True:
        for i in range(len(options)):
            print(str(i+1)+" "+options[i])
        answer = input("What would you like to do? ")
        try:
            answer = int(answer)
            if answer <= len(options) and answer > 0:
                return answer
            else:
                input("Invalid input, press enter to try again.\n")


        except:
            input("Invalid input, press enter to try again\n")
# sum = 0
# for i in range(3):
#     dieRoll = roll_dice(die_size)
#     sum += dieRoll
#     print("Roll: " + str(dieRoll))
#     print("Sum: " + str(sum))
#     print("Average: " + str(sum / 3))


if __name__ == "__main__":
    print("This is not a program try importing and using the classes.")
    input("\n\nPress the enter key to exit")