
def create_item(name:str, quantity:int, price:float):
    item = {}
    item["name"] = name
    item["quantity"] = quantity
    item["price"] = price
    return dict(item)

def calc_total(items:list):
    total = 0
    for item in items:
        total += item["quantity"] * item["price"]
    return total



def print_invoice(customer:str, items:list):
    print("Customer:", customer)
    print("------------------------------------------------")
    print(f"Product        Qty         Price       Subtotal")
    for item in items:
        print(f"{item['name']:<15} {item['quantity']:<10} ${item['price']:<10} {item['price']*item['quantity']}")
    print("-------------------------------------------------")
    print("TOTAL: ", calc_total(items))


items = []
item1 = create_item("Pen", 2, 5.0)
item2 = create_item("Notebook", 1, 15.0)
items.append(item1)
items.append(item2)

customer = input("Enter customer's name: ")
print_invoice(customer, items)
