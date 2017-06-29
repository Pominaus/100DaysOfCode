import random
from os import name as nom
from os import system as command

# Global vars
#-----------------
room_sprite = "|_"
visited_sprite = "|#"
player_sprite =  "|$"
monster_sprite = "|@"
door_sprite = "|>"
default_monster_sprite = "|@"
default_door_sprite = "|>"
dungeon_width = 6 #3 is min
dungeon_height = 6 #3 is min
rooms = []
room_contents = {}
direction_dict = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
    }
move_list = list(direction_dict.keys())
debug = False
score = 0
continue_message= "Press Return to Continue"


# Functions
#-----------------

# Setup functions:

def build_dungeon(room, width, height):
    return [[room for x in range(width)] for y in range(height)]
    
def set_room_contents(dungeon, num_rooms):
    x_vals = random.sample(range(len(dungeon)), num_rooms)
    y_vals = random.sample(range(len(dungeon[0])), num_rooms)
    return tuple(zip(x_vals, y_vals))
    
def initiate_vars():
    global rooms 
    rooms = build_dungeon(room_sprite, dungeon_width, dungeon_height)
    (room_contents["player"],
    room_contents["monster"], 
    room_contents["door"]) = set_room_contents(rooms, 3)
    update_room_contents(rooms, 
                        room_contents["door"],
                        door_sprite)
    update_room_contents(rooms, 
                        room_contents["monster"],
                        monster_sprite)
    update_room_contents(rooms, 
                        room_contents["player"],
                        player_sprite)
  
# Display functions:

def clear():
    command("cls" if nom == "nt" else "clear")
    
def draw_dungeon(dungeon):
    gap = " " * 5
    print(gap + " _" * dungeon_width)
    for row in dungeon:
        print(gap + "".join(row) + "|")
    print("KEY:\nPlayer: {}\n".format(player_sprite[1]) +
          "Unvisited Rooms:{}\n".format(room_sprite + "|") +
          "Visited Rooms: {}".format(visited_sprite + "|"))
    if debug:
        print("Monster: {}\n".format(monster_sprite[1]) + 
              "Exit: {}".format(door_sprite[1]))
    print("SCORE: {}".format(score))
      
def print_titles():
    clear()
    bars = "#" * 50
    gap = "\n\n"
    titles = "  W E L C O M E   T O   T H E   D U N G E O N"
    print(gap, bars, gap, titles, gap, bars, gap)
    input((" " * 15) + ">{}<".format(continue_message))
    
def print_menu():
    print_titles()
    bars = ("=" * 40)
    gap = "\n\n"
    option = """
                1: Default Game\n
                2: Debug Game\n
                3: Quit Game
                """
    while True:
        clear()
        print(gap, bars, gap, option, gap, bars, gap)
        try:
            selection = int(input("Choose Game mode [1/2]\n>"))
        except ValueError:
            print("Oops! Please Enter the Number of the Option Desired!")
            input(continue_message)
        else:
            if selection in (1, 2, 3):
                return selection
    

def show_result(result):
    bars = "=" * 12
    clear()
    print(bars, end = "\n\n")
    print("  " + ("Whoo!" if result == "won" else "Uh Oh!"))
    print("\n You {}!\n\nSCORE: {}".format(result.capitalize(), score))
    print(bars)
    pause_flow = input("\n{}".format(continue_message))
    clear()
    
# Movement functions:

def update_room_contents(dungeon, position, value):
    y, x = position
    dungeon[y][x] = value
  
def move_character(character, vector, dic):
    old_y, old_x = character
    new_y, new_x  = dic[vector]
    return old_y + new_y, old_x + new_x
    
def move_options(character, possible_moves):
    y, x = character
    valid_list = possible_moves[:]
    if x == 0:
        valid_list.remove("left")
    if x == dungeon_width - 1:
        valid_list.remove("right")
    if y == 0:
        valid_list.remove("up")
    if y == dungeon_height - 1:
        valid_list.remove("down")
    return valid_list
    
# Game Logic:

def check_room(room_dict):
    global score
    end_game = False
    result = "won"
    player_room = room_dict["player"]
    for key, value in room_dict.items():
        if value == player_room:
            if key == "monster":
                result = "lose"
                end_game = True
            elif key == "door":
                end_game = True
                score += 490
    if not end_game:
      score += 10
    return end_game, result
    
    
# Gameplay functions:

def main_menu():
    global monster_sprite
    global door_sprite
    global debug
    initiate_vars()
    while True:
        selection = print_menu()
        if selection == 3:
            return False
        elif selection == 1:
            monster_sprite = room_sprite
            door_sprite = room_sprite
            debug = False
            return True
        elif selection == 2:
            monster_sprite = default_monster_sprite
            door_sprite = default_door_sprite
            debug = True
            return True
    
    
def game_loop():
    clear()
    player = room_contents["player"]
    draw_dungeon(rooms)
    valid_moves = move_options(player, move_list)
    move_string = (", ".join(valid_moves)).title()
    print("\nAvailble moves: {}".format(move_string))
    direction = input(">").lower()
    if direction == "quit":
        return False
    elif direction in valid_moves:
        update_room_contents(rooms, player, visited_sprite)
        player = move_character(player, direction, direction_dict)
        update_room_contents(rooms, player, player_sprite)
        room_contents["player"] = player
        end, result = check_room(room_contents)
        if end:
            show_result(result)
            return False 
    elif direction in move_list:
        print("Oops! That's a wall, try again!:")
        input(continue_message)
    else:
        print("Uh-Oh, {}'s not a direction!".format(direction))
        input(continue_message)
    return True


# Run Game
#-----------------

#GameLoop
while main_menu():
    while game_loop():
        continue
    print("Game Over!")
    score = 0
    
    
    
    


