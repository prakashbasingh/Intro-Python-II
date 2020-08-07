class Store:
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments

    def __str__(self):
        return f"Welcome to the Quarantine Store! Have a nice shopping experience!"

    def print_departments(self):
        for id in self.departments:
            print(self.departments[id])
        print()