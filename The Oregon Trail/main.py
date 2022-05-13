# Jorden Dickerson
# 10-08-21
# The Oregon Trail

##imports
import random
from oregon_art import *

creator = "Jorden Dickerson and Dylan Langford"
tm = "©2021 Jorden Dickerson and Dylan Langford"
playing = False

NAMEBANK = (
    "Tamara",
    "Kierra",
    "Haiden",
    "Salvador",
    "Anaya",
    "Maurice",
    "Henry",
    "Dante",
    "Nico",
    "Marcel",
    "Brock",
    "Maggie",
    "Brynlee"
)
random.choice(NAMEBANK)
ILLNESS = (
    "None",
    "Dysentery",
    "None",
    "Smallpox",
    "None",
    "Measles",
    "None",
    "a broken arm",
    "None",
    "a broken leg",
    "None",
    "None",
    "None"
)
random.choice(ILLNESS)
WEATHER = (
    "clear",
    "rain",
    "snow"
)
random.choice(WEATHER)

# function defs
# Splash screen
def splash_screen():
    print(logo)
    print("\t\t" + creator)
    print("\t\t" + tm)
    print()
    print()


# Menu template
def display_menu(options):
    while True:
        print(RIBBON)
        for i in range(len(options)):
            print(str.format("\t{0} ...... {1:<30}", i + 1, options[i]))
        print(RIBBON)
        choice = input("What would you like to do?   ")
        if choice.isnumeric():
            if int(choice) <= len(options):
                choice = int(choice)
                return choice
            else:
                print("that's not an option!")
        else:
            print("that's not an option!")


# game menu
def game_menu():
    print(title)
    while True:
        options = ["Travel the Trail", "Learn about the Trail", "Quit Game"]  # define the choices to be made
        choice = display_menu(options)  # display the menu and get back the players choice
        # check the choice and run the correct option
        if choice == 1:
            playing = True
            return playing
        elif choice == 2:
            print("display info,\n info will be added at a later date")  # add real info later
            input("press enter to continue")
        elif choice == 3:
            ask = input("are you sure you want to quit?   ")
            if ("y" in ask) or ("Y" in ask):
                playing = False
                return playing
        else:
            print("that's not an option")


# Character select
def character_select():
    while True:
        options = [" Be a Banker from Ohio ", "be a Carpenter from Florida  ", "Be a Farmer from Texas ", ""]
        choice = display_menu(options)
        if choice == 1:
            profession = "Banker"
            money = 1600.00
            difficulty = "Easy"

            return profession, money, difficulty
        elif choice == 2:
            profession = "Carpenter"
            money = 800.00
            difficulty = "Medium"

            return profession, money, difficulty
        elif choice == 3:
            profession = "Farmer"
            money = 400.00
            difficulty = "hard"

            return profession, money, difficulty
        else:
            print("That's not an option!")

def party_naming():
    party = [None, None, None, None]
    while True:
        player_name = input("Enter party leader name: ")
        if player_name == (""):
            print("You have to enter a name!")
            return player_name, party_naming()
        party_1 = input("Enter the name of your 2nd party member: ")
        if party_1 == (""):
            party_1 = random.choice(NAMEBANK)
        party_2 = input("Enter the name of your 3rd party member: ")
        if party_2 == (""):
            party_2 = random.choice(NAMEBANK)
        party_3 = input("Enter the name of your 4th party member: ")
        if party_3 == (""):
            party_3 = random.choice(NAMEBANK)
        party_4 = input("Enter the name of your 5th party member: ")
        if party_4 == (""):
            party_4 = random.choice(NAMEBANK)
        print("Party names: Leader- "+player_name+", 2nd party member- "+party_1+", 3rd party member- "+party_2+",4th party member- "+party_3+",5th party member- "+party_4)
        confirm = input("Are these correct? (y/n): ")
        if confirm == ("y"):
            return player_name, party
        elif confirm ==("n"):
            return player_name, party_naming()
        else:
            print("Please put 'y' or 'n'.")


def month_select():
    while True:
        month = input("Would you like to start in March, April, May, June, or July? ")
        if month == ("March" or "march"):
            startMonth = "March"
            return startMonth
        elif month == ("April" or "april"):
            startMonth = "April"
            return startMonth
        elif month == ("May" or"may"):
            startMonth = "May"
            return startMonth
        elif month == ("June" or "june"):
            startMonth = "June"
            return startMonth
        elif month == ("July" or "july"):
            startMonth = "July"
            return startMonth
        else:
            print("That's not an option! Make sure to use proper capitalization!")

def shop(money,oxen,food,clothes,ammo,parts):
    global cost, parts_cost
    bill = 0
    partsinventory = []
    choices = ["Oxen","Food","Clothes","Ammunition","Wagon parts","Check Out"]
    spent_on_items = [0.00,0.00,0.00,0.00,0.00,bill]

    print("Before leaving Independence you should buy Equipment and Supplies.")
    print(str.format("You have ${:.2f} in cash to make this trip.", money))
    print("Remember you can buy supplies along the way, so you dont have to spend it all now.")
    input("Press any key to Continue")

    while True:
        spent_on_items[len(spent_on_items)-1] = bill
        print("Welcome to the General Store")
        print("Here is a list of things you can buy")
        print(RIBBON)
        print()
        for i in range(len(choices)):
            print (str.format("\t{:<2}: {:<20} ${:<.2f}",i+1,choices[i],spent_on_items[i]))
        print(str.format("Total Bill so far     ${:<.2f}",bill))
        print(str.format("Total funds available:     ${:<.2f}",money - bill))

        choice = int(input("What item would you like to buy?"))
        if choice == 1:
            bill -= spent_on_items[0]
            oxen = 0
            spent_on_items[0]= 0.00
            print("""
            There are 2 oxen in a yoke;
            I recommend at least 3 yokes.
            I charge $40 a yoke
            """)

            print(str.format("Total Bill so far     ${:<.2f}", bill))
            answer = int(input("How many Yoke do you want? "))
            cost = answer * 40
            oxen = answer * 2
            bill += cost
            spent_on_items[0] = cost



        elif choice == 2:
            bill -= spent_on_items[1]
            food = 0
            spent_on_items[1]= 0.00
            print("""
            I recommend you take at least 200 pounds of food for each person in your family;
            I see that you have 5 people in all;
            You'll need flour, sugar, bacon, and coffee. My price is 20 cents a pound.
            """)

            print(str.format("Total Bill so far     ${:<.2f}", bill))
            answer = int(input("How many pounds of food do you want?"))
            cost = answer * 0.20
            food = answer * 200
            bill += cost
            spent_on_items[1]= cost



        elif choice == 3:
            bill -= spent_on_items[2]
            clothes = 0
            spent_on_items[2] = 0.00
            print("""
            You'll need warm clothing in the mountains. I recommend taking at least 2 sets of clothes per person:
            Each set is $10.00""")

            print(str.format("Total Bill so far     ${:<.2f}", bill))
            answer = int(input("How many sets of clothes do you want?"))
            cost = answer * 10
            clothes = answer * 10
            bill += cost
            spent_on_items[2] = cost



        elif choice == 4:
            bill -= spent_on_items[3]
            ammo = 0
            spent_on_items[3] = 0.00
            print("""
            i sell ammunition in boxes;
            of 20 bullets. Each box;
            costs $2.00""")

            print(str.format("Total Bill so far     ${:<.2f}", bill))
            answer = int(input("How many boxes do you want?"))
            cost = answer * 0.20
            ammo = answer * 200
            bill += cost
            spent_on_items[3] = cost


        elif choice == 5:
            cost = 0.00
            bill -= spent_on_items[4]
            parts = 0
            spent_on_items[4] = cost
            print("""
            It is a good idea to have a few
            spare parts for your wagon on hand.
            You never know when you'll need to replace a broken part.
            """)
            partsinventory = []
            parts_bill = 0.00
            parts = ["Wagon Wheel", "Wagon Axle", "Wagon Tongue", "Back to main shop"]
            parts_cost = [10.00,20.00,50.00,parts_bill]
            while True:
                parts_cost[len(parts_cost) - 1] = parts_bill
                #display parts menu
                print(parts)

                parts_choice = input("What is your choice?")
                if parts_choice == "1":
                    wheelAnswer = int(input("How many Wagon Wheels do you want? "))
                    for i in range(wheelAnswer):
                        partsinventory.append("Wagon Wheel")
                    parts_bill += parts_cost[0] * wheelAnswer
                elif parts_choice == "2":
                    axleAnswer = int(input("How many Wagon Axles do you want? "))
                    for i in range(axleAnswer):
                        partsinventory.append("Wagon Axle")
                    parts_bill += parts_cost[1] * axleAnswer
                elif parts_choice == "3":
                    tongueAnswer = int(input("How many Wagon Axles do you want? "))
                    for i in range(tongueAnswer):
                        partsinventory.append("Wagon tongue")
                    parts_bill += parts_cost[2] * tongueAnswer
                elif parts_choice == "4":
                    bill += parts_bill
                    spent_on_items[4] = parts_bill
                    break

                else:
                    print("Something went wrong!")

        elif choice == 6 or "":
            if bill <= money:
                money -= bill
                return money,oxen,food,clothes,ammo,parts
            else:
                print("You don't have that much money, alter your shopping list.")
        else:
            print("Something went wrong")

def display_travel_screen(day):
    pass

def display_supplies(money,oxen,food,clothes,ammo,parts):
    while True:
        print(RIBBON)
        print("\t\t\tSUPPLIES")
        print("Oxen: " + str(oxen))
        print("Food: " + str(food))
        print("Clothes: " + str(clothes))
        print("Ammo: " + str(ammo))
        print("Parts: " + str(parts))
        print(RIBBON)
        input("Press enter to return to menu.")
        break


def change_pace():
    print(RIBBON)
    print("You can change the pace at which you travel. Here are your options:")
    print("1. A steady pace (requires less food)")
    print("2. A strenuous pace (requires more food)")
    print("3. A grueling pace (requires most food)")
    pace_choice = input("What is your choice? ")
    if pace_choice == "1":
        print("Pace set to 'Steady'.")
        pace = 1
        return pace
    elif pace_choice == "2":
        print("Pace set to 'Strenuous'.")
        pace = 1.5
        return pace
    elif pace_choice == "3":
        print("Pace set to 'Grueling'.")
        pace = 3
        return pace
    else:
        print("Pace set to 'Steady'.")
        pace = 1
        return pace


def change_rations(rations):
    print(RIBBON)
    print("The amount of food the people in your party eat each day can change. These amounts are:")
    print("1. Filling - meals are large and generous.")
    print("2. Meager - meals are small, but adequate.")
    print("3. Bare Bones - meals are very small; everyone stays hungry.")
    rations_change = input("What is your choice")
    if rations_change == "1":
        print("Rations changed to 'Filling'.")
        rations = 2
        return rations
    elif rations_change == "2":
        print("Rations changed to 'Meager'.")
        rations = 1
        return rations
    elif rations_change == "3":
        print("Rations changed to 'Bare Bones'.")
        rations = .50
        return rations
    else:
        print("That's not an option!")

def rest(health):
    print("You stopped to rest.")
    if health < 100:
        health += 10
    else:
        print("Your health is full!")

def trade(money,oxen,food,clothes,ammo,parts):
    print(RIBBON)
    display_supplies(money,oxen,food,clothes,ammo,parts)
    print("You meet another emigrant who wants 2 wagon tongues. She will trade you 1 ox.")
    trade = input("Are you willing to trade?")
    if trade == ("yes"):
        pass
    if trade == ("no"):
        pass
def hunt():
    pass

def pick_illness(health, party):
    sickness = random.choice(ILLNESS)
    if sickness == "None":
        pass
    else:
        print("A party member has " + sickness)
        health -= 5
        if health == 0:
            print(random.choice(party) + "has died.")
            party -= 1
            health = 100
            return party
        else:
            pass
        return health
def weather_conditions(weather, weather_condition):
    weather_condition = random.choice(WEATHER)
    if weather_condition == "snow":
        weather = .25
        return weather, weather_condition
    elif weather_condition == "rain":
        weather = .50
        return weather, weather_condition
    else:
        weather = 1
        return weather, weather_condition

def travel_trail(trail_length, miles_traveled, health, pace, weather, weather_condition, rations, food):
    print(oxen_art)
    # noinspection PyUnreachableCode
    if trail_length > 0:
        travel = (((oxen * 2) * pace) * weather)
        miles_traveled += travel
        trail_length -= miles_traveled


        print("Miles traveled: " + str(miles_traveled))
        print("Miles left: " + str(trail_length))
        print("weather:" + str(weather_condition))
        print("Health: " + str(health))
        return miles_traveled, trail_length
    else:
        pass
    if rations == 2:
        food -= 10
        return food
    elif rations == 1:
        food -= 5
        return food
    else:
        food -= 3
        return food





def main():
    # define game variable
    global day, oxen
    playing = True
    # display splash screen
    splash_screen()
    input("Press enter to Continue")
    while playing:
        # game variables
        player_name = None
        profession = None
        money = None
        difficulty = None
        party = [None, None, None, None]
        #party_1 = None
        #party_2 = None
        #party_3 = None
        #party_4 = None
        startMonth = ""
        health = 100
        day = 1
        date = (startMonth + "/" + str(day))
        oxen = 0
        food = 0
        clothes = 0
        ammo = 0
        parts = []
        weather = 1 #1, .25, .50
        weather_condition = None
        pace = 1 #1, 2, .50
        rations = 1 #1, 2, .50
        trail_options = ["Continue on Trail", "Check Supplies", "Change Pace", "Change Rations", "Rest", "Trade","Hunt"]
        trail_length = 2170
        miles_traveled = 0
        dailyMiles = 0
        travel = ((((oxen * 2) * pace) * weather) * health)
        broke_down = None




        # start the game
        playing = game_menu()
        if not playing:
            break
        #user assigned values
        profession, money, difficulty = character_select()
        player_name, party = party_naming()
        startMonth = month_select()

        #shopping
        money,oxen,food,clothes,ammo,parts = shop(money,oxen,food,clothes,ammo,parts)

        #Travel the trail
        while trail_length > miles_traveled and len(party) >= 1:
            trail_options = ["Continue on Trail", "Check Supplies", "Change Pace", "Change Rations", "Rest", "Trade",
                             "Hunt"]
            sick = pick_illness(health, party)
            weather_condition = weather_conditions(weather, weather_condition)
            display_travel_screen(day)
            choice = display_menu(trail_options)
            if choice == 1:
                #travel
                if oxen >= 1 and not broke_down:
                    miles_traveled, trail_length = travel_trail(trail_length, miles_traveled, health, pace, weather, weather_condition, rations, food)
                else:
                    print("You can't travel at this time")
                    if oxen < 1:
                        print("You have no oxen")
                    else:
                        print("You have a broken"+ str(broke_down))
                    continue
            elif choice == 2:
                display_supplies(
                    money,oxen,food,clothes,ammo,parts)
                continue
            elif choice == 3:
                pace = change_pace()
            elif choice == 4:
                rations = change_rations(rations)
            elif choice == 5:
                day += 1
                health = rest(health)
            elif choice == 6:
                trade(money,oxen,food,clothes,ammo,parts)
            elif choice == 7:
                food += hunt()
        if trail_length <= miles_traveled:
            print("Good job, you made it to Oregon!")
        else:
            print("Your choices cost your family their lives.")

    print("Game Over")


main()

input()
