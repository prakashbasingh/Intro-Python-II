# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, items):
        self.name = name
        self.current_room = current_room
        self.items = items

    def __str__(self):
        inventory = ""
        for item in self.items:
            inventory = inventory + " " + item + "|"
        return f"{self.name} is in {self.current_room.name}, and items are: {inventory}"
    
    def check_items(self):
        return self.items
      
    def take_items(self, item):
        self.items.append(item)
        # return print(f"You picked up {item}")
    
    def drop_items(self, received):
        dropping_item = ""
        for index, item in enumerate(self.items):
            if received == item:
                dropping_item = item
                del self.items[index]
        return dropping_item
    