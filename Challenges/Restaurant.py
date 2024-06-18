def main():
    menu_items = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total_cost = 0

    while(True):
        order = input("Item: \n").title()
        if (order.lower() == "end"):
            break
        try:
            total_cost += menu_items[order]
        except:
            print("That's not a valid order")
        print(f"Total: ${total_cost:.2f}")
main()
