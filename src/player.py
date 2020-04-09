# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item
class Player():
    def __init__(self, name, current_room, items=None):
        self.name = name
        self.current_room = current_room

        self.items = [] if items == None else items

    def get_name(self):
        return self.name

    def get_room(self):
        return self.current_room
    def is_movable_in_direction(self, direction):

        # print(direction)
        if(direction == 'n'):
            return self.current_room.n_to != None

        elif(direction == 's'):
            return self.current_room.s_to != None

        elif(direction == 'e'):
            return self.current_room.e_to != None

        elif(direction == 'w'):
            return self.current_room.w_to != None
        else:
            return False

    def movie_in_direction(self, direction):
        if(direction == 'n'):
            self.current_room = self.current_room.n_to

        elif(direction == 's'):
            self.current_room = self.current_room.s_to

        elif(direction == 'e'):
            self.current_room = self.current_room.e_to

        elif(direction == 'w'):
            self.current_room = self.current_room.w_to
    def has_item(self, item_name):
        return item_name in [i.name for i in self.items]
    def get_item(self, item_name):
        return [i for i in self.items if i.name == item_name][0]

    def take_item_from_room(self, item):
        self.items.append(item)
        self.current_room.items = [i for i in self.current_room.items
                                        if i.name != item.name]

    def put_item_into_room(self, item):
        self.current_room.items.append(item)
        self.items = [i for i in self.items
                            if i.name != item.name]
    def print_inventory(self):
        print(f'players inventory')
        [print(i) for i in self.items]