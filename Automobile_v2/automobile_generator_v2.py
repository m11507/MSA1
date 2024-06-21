import automobile as auto
#function load vehicle data from file
#input: path to file
#output: list of automobiles
def load_vehicles(file_name):
    #create an empty list to store automobile data
    #open the file
    list_of_automobiles = []
    auto_file = open(file_name, "r")
    auto_file.readline()

    line_number = 1
    for line_of_data in auto_file:
        vehicle_data = line_of_data.split(",")
        line_number += 1
        try:
            if len(vehicle_data) != 6:
                raise Exception(f"There is an error in your data file")
        except Exception as err:
            print(str(err))
            continue

        try:
            make = vehicle_data[0]
            model = vehicle_data[1]
            vin = vehicle_data[2]

            if vehicle_data[3].lower() == "electric":
                engine_size = 0
            else: 
                engine_size = float(vehicle_data[3])
            owner = vehicle_data[4]
            year = int(vehicle_data[5])
        except Exception as err:
            print(f"Error: {err} on line {line_number}")
            continue


        new_auto = auto.Automobile(make, model, vin, engine_size, owner, year)
        list_of_automobiles.append(new_auto)
        auto_file.close()
        return list_of_automobiles

    #read each line of the file in a for loop
    #split each line at the comma to get the values
    #get individual values from the resulting list
    #create automobile aobjects 

def main():
    automobile_list = load_vehicles("vehicle_data.csv")

    for vehicle in automobile_list:
        vehicle.print_info()

main()