def get_season(month):
    if (month == 12):
        return "Winter"
    elif (month >= 9):
        return "Fall"
    elif (month >= 6):
        return "Summer"
    elif (month >= 3):
        return "Spring"
    else:
        return "Winter"

def main():
    month=1
    while(month <= 1) and (month <= 12):
        try:
            month = int(input("Enter a month."))
        except:
            print("Please enter an integer between 1 and 12.")
            continue
        if (month<1) or (month > 12):
            print("Enter an integer between 1 and 12.")
            month=0
    print(get_season(month))

main()
