import random
import datetime


# Categories Data


data = {
    "funny": {
        "subjects": [
            "A Mumbai Cat",
            "A Group of Monkeys",
            "Black dog with muddy mouth",
            "Joker"
        ],
        "actions": [
            "dances with",
            "steals",
            "throws",
            "hides"
        ],
        "places": [
            "at India Gate",
            "inside a circus tent",
            "during a wedding",
            "at Red Fort"
        ]
    },

    "sports": {
        "subjects": [
            "Virat Kohli",
            "Rohit Sharma",
            "MS Dhoni"
        ],
        "actions": [
            "launches",
            "announces",
            "wins",
            "loses"
        ],
        "places": [
            "during IPL match",
            "at Wankhede Stadium",
            "in World Cup final"
        ]
    },

    "political": {
        "subjects": [
            "Prime Minister",
            "Nirmala Sitharaman",
            "Chief Minister"
        ],
        "actions": [
            "declares",
            "announces",
            "launches",
            "bans"
        ],
        "places": [
            "at Red Fort",
            "in Parliament",
            "at India Gate"
        ]
    }
}

adjectives = [
    "Shocking",
    "Unbelievable",
    "Mysterious",
    "Breaking",
    "Unexpected",
    "Controversial"
]


# Program Starts


print(" Welcome to Fake News Headline Generator......")

count = 0

while True:

    print("\nAvailable Categories: funny / sports / political")
    category = input("Choose a category: ").lower()

    if category not in data:
        print("Invalid category! Try again.")
        continue

    subject = random.choice(data[category]["subjects"])
    action = random.choice(data[category]["actions"])
    place = random.choice(data[category]["places"])
    adjective = random.choice(adjectives)

    current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    headline = f"{adjective}! {subject} {action} {place}"

    print("\n")
    print( current_time)
    print("BREAKING NEWS:", headline)
    print("-----------------------------------")

    # Save to file
    with open("headlines.txt", "a") as file:
        file.write(current_time + " - " + headline + "\n")

    count += 1

    # Mini Game
    truth = random.choice(["REAL", "FAKE"])
    guess = input("\nIs this REAL or FAKE? ").upper()

    if guess == truth:
        print("Correct Guess!")
    else:
        print(f"Wrong! It was {truth}")

    user_input = input("\nDo you want another headline? (yes/no): ").lower()

    if user_input == "no":
        break

print("\nTotal Headlines Generated:", count)
print("Thanks for using the Fake News Headline Generator")