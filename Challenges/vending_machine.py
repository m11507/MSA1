def main():
    print("Vending Machine")
    print("---------------")
    amount_due=50
    coin_value = 0
    while(amount_due > 0):
        print(f"Amount Due: {amount_due}")
        try:
            coin_value = int(input("Insert Coin: "))
        except:
            print("Please enter a valid coin value! (1,5,10,25)")
        if (coin_value in [1,5,10,25]):
            amount_due -= coin_value
        else:
            print("Please enter a valid coin value! (1,5,10,25)")
        print()
    print(f"Change Owed: {-1 * amount_due}")

main()
