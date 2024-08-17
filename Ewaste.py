import datetime

# User class to handle user information
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def list_inventory(self):
        if not self.inventory:
            print("No items in inventory.")
        else:
            for item in self.inventory:
                print(item)

# E-Waste item class to handle individual electronic items
class EWasteItem:
    def __init__(self, item_id, name, purchase_date):
        self.item_id = item_id
        self.name = name
        self.purchase_date = purchase_date
        self.disposal_date = None

    def mark_as_disposed(self):
        self.disposal_date = datetime.datetime.now()

    def __str__(self):
        return f"{self.item_id}: {self.name} (Purchased: {self.purchase_date}, Disposal: {self.disposal_date})"

# Collection request class
class CollectionRequest:
    def __init__(self, user, request_date):
        self.user = user
        self.request_date = request_date
        self.status = "Pending"

    def complete_request(self):
        self.status = "Completed"

    def __str__(self):
        return f"Request for {self.user.name} on {self.request_date} is {self.status}"

# Main class to manage the application
class EWasteMonitoringSystem:
    def __init__(self):
        self.users = {}
        self.collection_requests = []

    def register_user(self, user_id, name):
        user = User(user_id, name)
        self.users[user_id] = user
        print(f"User {name} registered successfully.")

    def add_inventory_item(self, user_id, item_id, name, purchase_date):
        if user_id in self.users:
            item = EWasteItem(item_id, name, purchase_date)
            self.users[user_id].add_item(item)
            print(f"Item {name} added to user {self.users[user_id].name}'s inventory.")
        else:
            print("User not found.")

    def schedule_collection(self, user_id):
        if user_id in self.users:
            request = CollectionRequest(self.users[user_id], datetime.datetime.now())
            self.collection_requests.append(request)
            print(f"Collection scheduled for user {self.users[user_id].name}.")
        else:
            print("User not found.")

    def list_collection_requests(self):
        if not self.collection_requests:
            print("No collection requests.")
        else:
            for request in self.collection_requests:
                print(request)

    def generate_report(self):
        for user_id, user in self.users.items():
            print(f"Report for {user.name}:")
            user.list_inventory()
            print()

# Main program
system = EWasteMonitoringSystem()

while True:
    print("\nE-Waste Monitoring System")
    print("1. Register User")
    print("2. Add E-Waste Item")
    print("3. Display E-Waste Items")
    print("4. Recycle E-Waste Item")
    print("5. Schedule Collection")
    print("6. List Collection Requests")
    print("7. Generate Report")
    print("8. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        user_id = int(input("Enter user ID: "))
        name = input("Enter user name: ")
        system.register_user(user_id, name)
    elif choice == '2':
        user_id = int(input("Enter user ID: "))
        item_id = int(input("Enter item ID: "))
        name = input("Enter item name: ")
        purchase_date = input("Enter purchase date (YYYY-MM-DD): ")
        system.add_inventory_item(user_id, item_id, name, purchase_date)
    elif choice == '3':
        user_id = int(input("Enter user ID: "))
        if user_id in system.users:
            system.users[user_id].list_inventory()
        else:
            print("User not found.")
    elif choice == '4':
        user_id = int(input("Enter user ID: "))
        if user_id in system.users:
            item_id = int(input("Enter item ID to recycle: "))
            for item in system.users[user_id].inventory:
                if item.item_id == item_id:
                    item.mark_as_disposed()
                    print(f"Item {item.name} has been marked as recycled.")
                    break
            else:
                print("Item not found.")
        else:
            print("User not found.")
    elif choice == '5':
        user_id = int(input("Enter user ID: "))
        system.schedule_collection(user_id)
    elif choice == '6':
        system.list_collection_requests()
    elif choice == '7':
        system.generate_report()
    elif choice == '8':
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please try again.")
