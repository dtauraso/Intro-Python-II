# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
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

