import csv
from Package_Object import Package
from Hash_Table import Hash_Table


# Create a function to get number of packages in csv file
# Time complexity: O(N)
def get_package_size():
    with open('PackageInfo.csv') as csvPackage:
        size = [row for row in csv.reader(csvPackage)]
    return len(size)


# Create a function to read package info in csv file with hash table as parameter,
#   then use a for loop to load info into hash table as objects,
#   using package ID as key and package object as value.
# The function returns hash table
# Time complexity: O(N)
def read_package(hash_table):
    with open('PackageInfo.csv') as csvPackage:
        readPackage = csv.reader(csvPackage, delimiter=',')

        # Make package object and add into hash table
        # with package ID as key.
        for row in readPackage:
            package = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], 'At hub', 'N/A', 'N/A')
            hash_table.insert(int(package.packageId), package)
    return hash_table


# Create a function to read distance table in csv file,
#   then add distance cell to a list and return that list.
# Time complexity: O(N)
def read_distance():
    with open('DistanceTable.csv') as csvDistance:
        distance_value = [row for row in csv.reader(csvDistance)]
    return distance_value

# Create a function to load package ID to truck based on delivery deadline and note constraints.
# Take three truck lists as parameters.
# First, the function read_package function to call up hash table,
#   then use a for loop to call and assign package object to my_package variable.
#   The package object is used to call up package notes and compare it with
#   conditions of if/else statements in order to load package ID to each truck list.
# Time complexity: O(N^3)
def loading_truck(first_truck_list, second_truck_list, third_truck_list):
    hash_table = read_package(Hash_Table())  # Read and insert package object to hash table
    hash_size = int(len(hash_table.map))     # Get length of hash table

    # Load package onto trucks with constraints for each truck using if/else statement and for loop
    # Time complexity: O(N^3)
    for i in range(1, hash_size):
        my_package = hash_table.get(i)

        # Set a while loop True to sort package to truck base on each package's constraint
        # Time complexity: O(N^2)
        while True:
            # Conditions to load first truck:
            # While length of truck list < 16, check if package ID not in second truck or third truck, then
            # if package's note contains 'Must', or package's deadline contains '10:30' or '9:00', add package ID to first truck.
            # Time complexity: O(N)
            while(len(first_truck_list) < 16):
                if my_package.packageId not in second_truck_list and my_package.packageId not in third_truck_list:
                    if 'Must' in my_package.note:
                        first_truck_list.append(my_package.packageId)
                    elif '10:30' in my_package.deadline:
                        first_truck_list.append(my_package.packageId)
                    elif '9:00' in my_package.deadline:
                        first_truck_list.append(my_package.packageId)
                break

            # Conditions to load second truck:
            #   While length of truck list < 16, check if package ID not in first truck or third truck, then
            #   if package's note contains 'only' or 'None, add package ID to second truck.
            # Time complexity: O(N)
            while(len(second_truck_list) < 16):
                if my_package.packageId not in first_truck_list and my_package.packageId not in third_truck_list:
                    if 'only' in my_package.note:
                        second_truck_list.append(my_package.packageId)
                    elif 'None' in my_package.note:
                        second_truck_list.append(my_package.packageId)
                break

            # Conditions to load third truck:
            # While length of truck list < 16, check if package ID not in second truck or first truck, then
            # if package's note contains 'Delayed' or 'None' or 'Wrong', add package ID to third truck.
            # Time complexity: O(N)
            while (len(third_truck_list) < 16):
                if my_package.packageId not in first_truck_list and my_package.packageId not in second_truck_list:
                    if 'Delayed' in my_package.note:
                        third_truck_list.append(my_package.packageId)
                    elif 'Wrong' in my_package.note:
                        third_truck_list.append(my_package.packageId)
                    elif 'None' in my_package.note:
                        third_truck_list.append(my_package.packageId)
                break
            break

        # Using if/else statement to check for unloaded package
        # If package is not loaded in any truck, and the length of any truck is not equals 16, add package to that truck.
        # Time complexity: O(1)
        if my_package.packageId not in first_truck_list and my_package.packageId not in second_truck_list and my_package.packageId not in third_truck_list:
            if len(first_truck_list) < 16:
                first_truck_list.append(my_package.packageId)
            elif len(second_truck_list) < 16:
                second_truck_list.append(my_package.packageId)
            elif len(third_truck_list) < 16:
                third_truck_list.append(my_package.packageId)
