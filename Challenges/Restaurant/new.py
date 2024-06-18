#Function to load menu items from the file
def get_menu_items():
    data_file = open("menu.txt", "r")
    menu_items = {}
    for line_of_darta in data_file:
        keys_and_values = line_of_darta.split(",")
        menu_items[keys_and_values[0]]=keys_and_values[1]
    
    data_file.close()
    return menu_items


    #create a file handle that gives us access to the file
    #create an empty dictioinary to store menu items and prices
    #Loop through data in the file and read the file one line at a time
    #Split line of data at the comma using split

def main():
    menu_items = get_menu_items()
    total_cost = 0

    while(True):
        order = input("Item: \n").title()
        if (order.lower() == "end"):
            break
        try:
            total_cost += float(menu_items[order])
        except:
            print("That's not a valid order")
        print(f"Total: ${total_cost:.2f}")

    
main()