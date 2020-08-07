import sys

from room import Room
from player import Player
from item import Item

# Declare all the rooms
room = {
    "outside":  Room("\n Outside Cave Entrance", "North of you, the cave mount beckons \n", [Item("torch", "Do not forget to carry AAA batteries")]),

    "foyer":    Room("\n Foyer", """Dim light filters in from the south. Dusty passages run north and east.""", [Item("golden_sword", "Sword is necessary if there is monster")]),

    "overlook": Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""", [Item("nightvision_binocular", "need to see whats out there beyond the chasm")]),

    "narrow":   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air.""", [Item("Holly_water", "Drink it, Makes you stronger")]),

    "treasure": Room("Treasure Chamber", """You"ve found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""", [Item("Six Infinity Stones", "earlier adventurer missed it now You can change the universe for goooooooooood")]),
}

# Link rooms together
room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

#
# Main
#

# Make a new player object that is currently in the "outside" room.

# getting player information
name = input("\n what is your name player??? \n").lower().strip()
new_player = Player(name, room["outside"], [])
print(f"\n Hey {name}!!! Welcome to the adventure game")
# name = input("what is your name player???").lower().strip()
# player.name = name

# starts
print(f"\n Hello {name}! Let's explore the rooms \n")
print("lets start the game!!!")
answer = input("\n Shall we begin? y/n: ")
if answer.lower().strip() == "y":
    print(f" \n-->You are currently in {new_player.current_room} \n")

# Write a loop that:
while True:
    #
    # * Prints the current room name
    current_room = new_player.current_room
    
    room_items = ""
    for i in current_room.check_items():
        room_items = i.name
        item_description = i.description
    if room_items == "":
        room_items = "nothing"
    print (f"-- Search and Find {room_items} --")
    print(f"-- {item_description} -- \n")
    # * Prints the current description (the textwrap module might be useful here).
    # * Waits for user input and decides what to do.
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn"t allowed.
    inputs = ["n", "s", "e", "w", "q"]
    # If the user enters "q", quit the game.
    command = input("> ").split(",")

    if command[0] == "q":
        answer = input("are you sure: y/n: ")
        if(answer == "y"):
            sys.exit()
        continue
    elif command[0] == "n":
        if(current_room.n_to != None):
            print("Moving North.")
            new_player.current_room = current_room.n_to
            print(f"\n Now You Are In {new_player.current_room} <<< \n")
        else:
            print("Can not go this way, try another way!!!")
    elif command[0] == "s":
        if(current_room.s_to != None):
            print("Moving South.")
            new_player.current_room = current_room.s_to
            print(f"\n Now You Are In {new_player.current_room} <<< \n")
        else:
            print("Can not go this way, try another way!!!")        
    elif command[0] == "e":
        if(current_room.e_to != None):
            print("Moving East.")
            new_player.current_room = current_room.e_to
            print(f"\n Now You Are In {new_player.current_room} <<< \n")
        else:
            print("Can not go this way, try another way!!!") 
    elif command[0] == "w":
        if(current_room.w_to != None):
            print("Moving West.")
            new_player.current_room = current_room.w_to
            print(f"\n Now You Are In {new_player.current_room} <<<\n")
        else:
            print("Can not go this way, try another way!!!")
    elif command[0] == "take":
        if(command[0]):
            new_player.take_items(current_room.loose_items(command[0]))
            print(f"you took {room_items} from {current_room.name}\n")
        else:
            print("Oops!!! plz write 'take ......' <-- item name here")
    elif command[0] == "drop":
        if(command[0]):
            current_room.add_items(new_player.drop_items(command[0]))
            print(f"you dropped the {room_items} into the {current_room.name}")
        else:
            print("Oops!!! plz write 'take ......' <-- item name here")
    elif command[0] == "check-items":
        inventory = "bag: "
        for item in new_player.check_items():
            inventory = inventory + room_items + ", "
        print(inventory)

# elif command[0] == "n":
# # check if the player can move to the north 
# # if there is, set that north room as the player"s location