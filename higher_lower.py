import random
from game_data import data
from art import logo, vs

print(logo)

#option1 selects the dictionary from the list - data, with the details of first choice
option1 = random.choice(data)

score_count = 0

while True:
    #option2 selects the dictionary from the list - data, with the details of second choice
    option2 = random.choice(data)

    #This while loop checks and makes sure that option1 and option2 are not the same, incase they are it reassigns it a different value
    while option1 == option2:
        option2 = random.choice(data)

    option1_followers = option1['follower_count']
    option2_followers = option2['follower_count']

    print("\n"*2 + f"OPTION 1: {option1['name']}, {option1['description']}, from {option1['country']}")
    print(vs)
    print(f"OPTION 2: {option2['name']}, {option2['description']}, from {option2['country']}")

    #Here we take input from the user and make sure that the input is of correct data type and is one of the two choices(i.e '1' or '2')
    while True:
        try:
            user_choice = int(input("'1' for Option 1 and '2' for Option 2:"))
            if user_choice in [1, 2]:
                break
            else:
                print("\n\n\n\nInvalid Input, please select either '1' or '2'\n\n\n\n")
        except ValueError:
            print("\n\n\n\nInvalid Input, please select either '1' or '2'\n\n\n\n")
    
    #When the user guesses the correct option with higher followers we get rid of the higher follower option and make room for the next choice
    if user_choice == 1 and option1_followers > option2_followers:
        option1 = option2
        score_count += 1
    elif user_choice == 2 and option2_followers > option1_followers:
        score_count += 1
    
    #Incase the option chosen is incorrect loop breaks and the code ends
    if (user_choice == 1 and option2_followers > option1_followers) or (user_choice == 2 and option1_followers > option2_followers):
        print(f"Sorry, that was wrong 🥲.\nYour Score: {score_count}")
        break