





class Order:
    def __init__(self, order_id, customer_name, dish_ids, status):
        self.order_id = order_id
        self.customer_name = customer_name
        self.dish_ids = dish_ids
        self.status = status    

def menuItem(name, id, price, avail):
    obj = {}
    obj["name"] = name
    obj["id"] = id
    obj["price"] = price
    obj["availability"] = avail
    return obj


class Staf:
    def __init__(self):
       self.menu=[]
       self.orders=[]
       self.next_order_id=1

    def addDish(self, dish):
        self.menu.append(dish)
        print(f"Dish '{dish['name']}' has been added to the menu.")

    def removeDish(self, id):
        for dish in self.menu:
            if dish['id'] == id:
                self.menu.remove(dish)
                print(f"Dish '{dish['name']}' has been removed from the menu.")
                return
        print("Dish not found in the menu.")

    def updateAvail(self, id, avail):
        for d in self.menu:
            if d['id'] == id:
                d['availability'] = avail
                print(f"Dish '{d['name']}' availability has been updated.")
                return
        print("Dish not found in the menu.")

    def takeOrder(self, cName, dish_ids):
        dishes = []
        for id in dish_ids:
            found = False
            for dish in self.menu:
                if dish['id'] == id:
                    found = True
                    if dish['availability'] == 'yes':
                        dishes.append(dish)
                    else:
                        print(f"Dish '{dish['name']}' is not available.")
                    break
            if not found:
                print(f"Dish with ID '{id}' not found in the menu.")

        if dishes:
            order_id = self.next_order_id
            order = Order(order_id, cName, dish_ids, "received")
            self.orders.append(order)
            self.next_order_id += 1
            print(f"Order placed successfully. Order ID: {order_id}")

    def update_order_status(self, id, status):
        for o in self.orders:
            if o.order_id == id:
                o.status = status
                print(f"Order ID {id} status has been updated to '{status}'.")
                return
        print("Order not found.")

    def review_orders(self):
        if self.orders:
            print("All orders:")
            for order in self.orders:
                print(f"Order ID: {order.order_id}, Customer: {order.customer_name}, Status: {order.status}")
        else:
            print("No orders found.")

def print_menu():
    print("\nMenu:")
    for dish in staf_zomato.menu:
        print(f"Dish ID: {dish['id']}, Name: {dish['name']}, Price: {dish['price']}, Availability: {dish['availability']}")

def print_options():
    print("\nOptions:")
    print("1. Add dish to the menu")
    print("2. Remove dish from the menu")
    print("3. Update dish availability")
    print("4. Take a new order:")
    print("5. Update order status")
    print("6. Review all orders")
    print("7. Exit")

# create an instance of Staf
staf_zomato = Staf()

# main program loop
while True:
    print_options()
    choice = input("Enter your choice: ")
    if choice == "1":
        dish_id = input("Enter dish ID: ")
        dish_name = input("Enter dish name: ")
        price = float(input("Enter dish price: "))
        availability = input("Enter dish availability (yes/no): ")
        dish = menuItem(dish_name, dish_id, price, availability)
        staf_zomato.addDish(dish)

    elif choice == "2":
        dish_id = input("Enter dish ID to remove: ")
        staf_zomato.removeDish(dish_id)
    elif choice == "3":
        dish_id = input("Enter dish ID to update availability: ")
        availability = input("Enter dish availability (yes/no): ")
        staf_zomato.updateAvail(dish_id, availability)

    elif choice == "4":
        customer_name = input("Enter customer name: ")
        dish_ids = input("Enter dish IDs (comma-separated): ").split(",")
        staf_zomato.takeOrder(customer_name, dish_ids)

    elif choice == "5":
        order_id = input("Enter order ID to update status: ")
        status = input("Enter new status: ")
        staf_zomato.update_order_status(order_id, status)

    elif choice == "6":
        staf_zomato.review_orders()

    elif choice == "7":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")