import sys

from department import Department
from product import Product
from user import User
from store import Store

# user will pass in either 0 or 1 command-line arguments to the program
num_args = len(sys.argv)
# if they pass in 0, we'll default their money to 100 
if num_args == 1:
    user = User(100)
# if they pass in 1 argument (a number), set their money to that amount 
elif num_args == 2:
    user = User(int(sys.argv[1]))
else:
    print("Usage: store.py [money]")
    sys.exit(1)

departments = {
    23: Department(23, "Groceries", [Product("Bananas", 1), Product("Avocados", 2), Product("Watermelons", 4)]),
    9: Department(9, "Books", [Product("Game of Thrones", 10), Product("Working in Public", 25), Product("Twilight", 10)]), 
    13: Department(13, "Electronics", [Product("Samsung 4K TV", 300), Product("iPhone SE", 400), Product("Pixel 4A", 350)]), 
    7: Department(7, "Clothes", [Product("Graphic T's", 20), Product("Kanye Sweater", 700), Product("Sketchers High Tops", 50)]), 
    15: Department(15, "Toys", [Product("Lightsaber", 200), Product("Nerf Guns", 200), Product("Settlers of Catan", 40), Product("Nintendo Lego Set", 150)]) 
}

store = Store("Quarantine Store", departments)

# print the store's welcome message
print(store)

# print user's status
print(user, '\n')

while True:
    # print departments 
    store.print_departments()

    selection = input("Which department would you like to visit? ")

    if selection == 'quit' or selection == 'q':
        break

    # expect user to type in a number that is read in as a string 
    # parse it into an int, and then check if the int is a valid 
    dep_num = int(selection)

    if dep_num not in departments:
        print("\nThat is not a valid department.\n") 
        continue

    selected_dep = departments[dep_num]

    print(f"\nYou picked department number {dep_num}, the {selected_dep.name} department.\n")

    selected_dep.print_products()
   
    # we want the user to be able to add products to their cart
    product_selection = int(input("What would you like to add to your cart? "))

    possible_products = selected_dep.products

    # index into the current department's list of products using the `product_selection`
    selected_product = possible_products[product_selection]

    user.add_to_cart(selected_product)