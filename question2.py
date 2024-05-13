# Question 2 Task 1 
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

# Question 2 Task 2
facilities = "audio system" if attendees > 100 else "projector"
print(facilities)

# Question 2 Task 3
food_preference = input("What is your food preference? (Vegetarian/Non-Vegetarian) ")
food = "Veggie Delight Caterers" if food_preference == "Vegetarian" else "Gourmet Meals Caterers"
print(food)