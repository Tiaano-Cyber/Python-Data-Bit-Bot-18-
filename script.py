import json

# Collecting user information
name = input("Hello! My Name Is Bot 18. I Am Here To Collect Your Information. What Is Your Name? ")
print(f"Nice to meet you, {name}!")
age_input = input("How old are you? ") 
age = int(age_input)
bot_age = 3
print(f"You are {age}. I'm only {bot_age} years old!")
color = input("What's Your Favourite Color? ")
print(f"Oh {color} is a beautiful color!")

# The rest of the interaction
print("Press Enter To Continue")
input()
print(f"Hello This Is {name} Right? If yes, press Enter.")
input()
print("Your Detailed Information Here")
print(f"Your Name Is {name}")
print(f"You Are {age} years old ")
print(f"Your Favourite Color Is {color}")

# Preparing data to save only 'name' and 'age'
data = {
    "name": name,
    "age": age
}

# Saving the specified data to JSON file
with open("data.json", 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("Your name and age have been saved to data.json")