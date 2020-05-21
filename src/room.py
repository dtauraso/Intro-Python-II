# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = [] if items == None else items

    def __str__(self):
        return f'{self.name} {self.description} Items: {self.get_items()}'
    def get_items(self):
        return ''.join([f'{i.name} {i.description}|' for i in self.items])
    def get_directions(self):

        # I don't know how to make this cleaner
        n = f'n -> {self.n_to.name}' if self.n_to else None
        s = f's -> {self.s_to.name}' if self.s_to else None
        e = f'e -> {self.e_to.name}' if self.e_to else None
        w = f'w -> {self.w_to.name}' if self.w_to else None

        directions = [n, s, e, w]
        return [i for i in directions if i]

    def has_item(self, item_name):
        # print(self.items, item_name)
        return item_name in [i.name for i in self.items]
    def get_item(self, item_name):
        return [i for i in self.items if i.name == item_name][0]

    def add_item(self, new_item):
        self.items.append(new_item)
    def get_all_items(self):
        return self.items