# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
    def __str__(self):
        return f" -->{self.name}, room description: {self.description}<--"
    
    def get_description(self):
        return (self.description).format(self = self)
    
    def check_items(self):
        return self.items
    
    def loose_items(self, taking):
        taken_room_item = ""
        # print(taking)
        for index, item in enumerate(self.items):
            # print(taking)
            # print(item)
            if(item.name == taking):
                taken_room_item = item
                del self.items[index]
        return taken_room_item
    
    def add_items(self, received):
        self.items.append(received)
        return print(f"You placed {received.name} in {self.name}")