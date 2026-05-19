import time  


class BaseEntity:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Product(BaseEntity):
    pass


class Customer(BaseEntity):
    def __init__(self, id, name, zipcode):
        super().__init__(id, name)
        self.zipcode = zipcode
        self.purchased = []
    def __str__(self):
        return f"customer id: {self.id}, customer Name: {self.name}, zipcode: {self.zipcode}"


class Shop(BaseEntity):
    def __init__(self, id, name, zipcode):
        super().__init__(id, name)
        self.zipcode = zipcode
        self.inventory = {}


class DeliveryAgent(BaseEntity):
    def __init__(self, id, name, zipcode):
        super().__init__(id, name)
        self.zipcode = zipcode
        self.delivered = 0


customers = []   # we have added a customer
products = []   # we have added a product 
shops = []
agents = []      # now we add these remaining  3... #### Note the zipcode should match with the all entites then only we can process the order kk na 
orders = []


def find_by_id(lst, id):
    for item in lst:
        if item.id == id:
            return item
    return None


def create_customer():
    id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    zipc = int(input("Enter Zipcode: "))
    customers.append(Customer(id, name, zipc))


def create_product():
    id = int(input("Enter Product ID: "))
    name = input("Enter Product Name: ")
    products.append(Product(id, name))


def create_shop():
    id = int(input("Enter Shop ID: "))
    name = input("Enter Name: ")
    zipc = int(input("Enter Zipcode: "))
    shops.append(Shop(id, name, zipc))


def create_agent():
    id = int(input("Enter Agent ID: "))
    name = input("Enter Name: ")
    zipc = int(input("Enter Zipcode: "))
    agents.append(DeliveryAgent(id, name, zipc))


def delete_entity(lst, label):
    if not lst:
        print("No entities available")
        return

    for item in lst:
        print(f"{item.id} -> {item.name}")

    id = int(input(f"Enter {label} ID to delete: "))

    for i in range(len(lst)):
        if lst[i].id == id:
            lst.pop(i)
            print("Deleted")
            return

    print("ID not found")


def add_inventory():
    shop_id = int(input("Shop ID: "))
    product_id = int(input("Product ID: "))
    qty = int(input("Quantity: "))

    shop = find_by_id(shops, shop_id)

    if shop:
        shop.inventory[product_id] = shop.inventory.get(product_id, 0) + qty
        print("Inventory updated")
    else:
        print("Invalid Shop")


def add_order():
    cid = int(input("Customer ID: "))
    pid = int(input("Product ID: "))

    customer = find_by_id(customers, cid)
    product = find_by_id(products, pid)

    if not customer:
        print("Invalid Customer")
        return

    if not product:
        print("Invalid Product")
        return

    orders.append((cid, pid))
    print("Order added successfully")


def process_order():
    if not orders:
        print("No orders")
        return

    print("Processing order", end="", flush=True)
    for _ in range(3):
        time.sleep(1)
        print(".", end="", flush=True)
    print("\n")

    cid, pid = orders.pop(0)

    customer = find_by_id(customers, cid)
    if not customer:
        print("Invalid customer")
        return

    valid_shop = None
    for shop in shops:
        if shop.zipcode == customer.zipcode and shop.inventory.get(pid, 0) > 0:
            valid_shop = shop
            break

    if not valid_shop:
        print("Order cannot be fulfilled")
        return

    if not agents:
        print("No agents available")
        return

    print("Assigning delivery agent...", end="", flush=True)
    time.sleep(1)
    print(" Done")

    agent = agents[0]
    for a in agents:
        if a.delivered < agent.delivered:
            agent = a

    print(f"{agent.name} is delivering your order...", end="", flush=True)
    time.sleep(2)
    print(" Delivered!")

    valid_shop.inventory[pid] -= 1
    customer.purchased.append(pid)
    agent.delivered += 1

    print(f"\n Order successfully delivered by {agent.name}")


def list_purchases():
    cid = int(input("Customer ID: "))
    customer = find_by_id(customers, cid)

    if customer:
        print("Purchased:", customer.purchased)
    else:
        print("Customer not found")


def shop_inventory():
    sid = int(input("Shop ID: "))
    shop = find_by_id(shops, sid)

    if shop:
        print("Inventory:", shop.inventory)
    else:
        print("Shop not found")

def display_customers():
    a=0
    for z in customers:
        a+=1
        print("\t",a,".",z,sep="")

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Create Customer")
        print("2. Create Product")
        print("3. Create Shop")
        print("4. Create Agent")
        print("5. Delete Customer")
        print("6. Delete Product")
        print("7. Delete Shop")
        print("8. Delete Agent")
        print("9. Add Inventory")
        print("10. Add Order")
        print("11. Process Order")
        print("12. Customer Purchases")
        print("13. Shop Inventory")
        print("14. display customers")
        print("0. Exit")

        try:
            ch = int(input("Enter choice: "))
        except:
            print("Invalid input")
            continue

        if ch == 1:
            create_customer()
        elif ch == 2:
            create_product()
        elif ch == 3:
            create_shop()
        elif ch == 4:
            create_agent()
        elif ch == 5:
            delete_entity(customers, "Customer")
        elif ch == 6:
            delete_entity(products, "Product")
        elif ch == 7:
            delete_entity(shops, "Shop")
        elif ch == 8:
            delete_entity(agents, "Agent")
        elif ch == 9:
            add_inventory()
        elif ch == 10:
            add_order()
        elif ch == 11:
            process_order()
        elif ch == 12:
            list_purchases()
        elif ch == 13:
            shop_inventory()
        elif ch == 14:
            display_customers()
        elif ch == 0:
            print("Exiting...")
            break
        else:
            print("Invalid choice")


menu()
