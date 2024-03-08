# Imports
import random
import os
import pandas as pd

# Variables

# Specify the file path
csv_file_path = 'Bot-Hand-Model.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Display the DataFrame
print(df)

    
# Deck includes all suites, and possible cards in a 52 deck of cards
deck = ["H2","H3","H4","H5","H6","H7","H8","H9","HT","HJ", "HQ", "HK", "HA",
        "D2","D3","D4","D5","D6","D7","D8","D9","DT","DJ", "DQ", "DK", "DA",
        "C2","C3","C4","C5","C6","C7","C8","C9","CT","CJ", "CQ", "CK", "CA",
        "S2","S3","S4","S5","S6","S7","S8","S9","ST","SJ", "SQ", "SK", "SA",]

# Player data
playerHand = []
position = 1

# Store opposing player data
opposingHands = {}
opposingPositions = {}

# Functions
def playGame():
    for i in range(len(opposingPositions)):
        x = 10

def deal(handCount): # Function to deal hands

    for i in range(handCount + 1):
        posCycle = i + 1 # Variable to store the cycling positions

        if posCycle == position: # Check if looping over the player's position
            print("Player's pos")
            for i in range(2):
                # Draw cards
                draw = random.choice(deck)
                playerHand.append(draw)

                # Remove them from the deck
                deck.remove(draw)
        else:
            # Draw cards and remove them
            draw1 = random.choice(deck)
            deck.remove(draw1)
            draw2 = random.choice(deck)
            deck.remove(draw2)

            # Give cards to opposing player(s)
            opposingHands[f"hand_{posCycle}"] = [draw1, draw2]
    
    for key, value in opposingHands.items():
        print(f"{key}; {value}")


# Main Game Loop

while True:
    action = input("Welcome to Poker! Ready to begin (Y/N): ") # Begin the game for the player

    if action.upper() == "Y":
        while True:
            action = int(input("How many players would you like to play against?: ")) # Determine the number of opponents

            if action < 1:
                print("You cannot play against less than one player!")
                continue
            elif action > 8:
                print("You cannot play with more than 8 players!")
                continue
            else:
                deal(action) # Deal hands
    else:
        continue