# Question 1 Task 1 
place = input("Choose a place: forest or cave? ")
action = input("Do you want to climb a tree or cross a river? ")
action2 = input("Do you want to light a torch or proceed in the dark ")

if place == "forest":
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    print("You found a hidden treasure!")

# Question 1 Task 2
if place == "cave":
    if action2 == "light a torch":
        print("You can see all the hidden treasures")
    elif action2 == "proceed in the dark":
        print("You might fall or get hurt.")

# Question 1 Task 3 
else: 
    pass