# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name, current_room, items=None):
        self.name = name
        self.current_room = current_room

        if(items == None):
            self.items = []
        else:
            self.items = items


    def is_movable_in_direction(self, direction):

        if(direction == 'n'):
            return self.current_room.n_to != None

        elif(direction == 's'):
            return self.current_room.s_to != None

        elif(direction == 'e'):
            return self.current_room.e_to != None

        elif(direction == 'w'):
            return self.current_room.w_to != None

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
        return item_name in self.items
    
    def take_item_from_room(self, item_name):
        self.items.append(item_name)
        self.current_room.items = [i for i in self.current_room.items
                                        if i != item_name]
    def put_item_into_room(self, item_name):
        self.current_room.items.append(item_name)
        self.items = [i for i in self.items
                            if i != item_name]
    # def take_all_items_from_room(self):
        # transfer all items from the current room to the players inventory