from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [
                         Item('frog', 'It\'s just a frog')
                     ]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
    [
        Item('orb', 'floating'),
        Item('painting', 'on an isle')

    ]
),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
[
    Item('diamond', 'shiny')
]
),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
my_player = Player('me', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def is_cardinal_direction(command):
    return (command == 'n' or
            command == 's' or
            command == 'e' or
            command == 'w')
def is_quit(command):
    return command == 'q'
# def show_items(command):
#     return command == 'show items'

# def take_all_from_room(command):
#     return command == 'take items'
def main_game():


    while(True):

        print(my_player.current_room)

        command = input(f'enter a command. The current directions allowed are: {my_player.current_room.get_directions()} ')

        # parse the command
        command_segments = command.split(' ')
        # print(command_segments)
        if(len(command_segments) == 1):

            if(is_cardinal_direction(command)):

                if(my_player.is_movable_in_direction(command)):
                    my_player.movie_in_direction(command)

            else:
                if(command == 'p'):
                    my_player.print_inventory()
                else:

                    print(f'{my_player.name} can\'t go {command}')
            if(is_quit(command)):
                break

        else:
            if(command_segments[0] == 'get'):
                item_name = command_segments[1]
                # print(command_segments)
                if(my_player.current_room.has_item(item_name)):
                    item = my_player.current_room.get_item(item_name)

                    my_player.take_item_from_room(item)
                    if(my_player.has_item(item_name)):
                        print('player got', item_name)
                else:
                    print('We can\' get an item we not in the room')

            if(command_segments[0] == 'drop'):
                item_name = command_segments[1]
                if(my_player.has_item(item_name)):
                    item = my_player.get_item(item_name)

                    my_player.put_item_into_room(item)
                    if(my_player.current_room.has_item(item_name)):
                        print('player put', item_name, 'into room')
                else:
                    print('We can\' drop an item we don\'t have')
            # if(show_items(command)):
            #     all_items = my_player.current_room.get_all_items()
            #     [print(item) for item in all_items]
            # if(take_all_from_room(command)):
            #         my_player.take_all_items_from_room()

        

main_game()