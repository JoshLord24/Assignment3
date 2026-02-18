# Supply Chain Tracker

def main():
    
    # inventory dictionary
    warehouses = [
    {"name": "Warehouse A", "inventory": {"apples": 100, "bananas": 150}},
    {"name": "Warehouse B", "inventory": {"apples": 200, "bananas": 100}},
    {"name": "Warehouse C", "inventory": {"apples": 400, "bananas": 250}},
    {"name": "Warehouse D", "inventory": {"apples": 700, "bananas": 425}}
    ]

    # separates products and sums them
    total_inventory = {}
    for warehouse in warehouses:
        for product, amount in warehouse["inventory"].items():
            if product in total_inventory:
                total_inventory[product] += amount
            else:
                total_inventory[product] = amount

    for product, total in total_inventory.items():
        print(f"{product}: {total}")
    
main() 