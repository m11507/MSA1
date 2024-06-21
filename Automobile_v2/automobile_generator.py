import automobile

def main():
    #create automobile objects
    auto1 = automobile.Automobile("Ford", "Focus", "1234", 2.2, "Alice", 2013)
    auto2 = automobile.Automobile("Honda", "Accord", "23456", 3.0, "Bob", 2017)

    auto1.print_info()

    #change auto2 year
    auto1.set_owner("Cyd")

    automobile_list = []

    automobile_list.append(auto1)
    automobile_list.append(auto2)

    print("\nGetting Automobiles from a list----------------")
    for auto in automobile_list:
        auto.print_info()


main()