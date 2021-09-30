import datetime
from Hash_Table import Hash_Table
from Read_File import read_package
from Read_File import read_distance


# Create a function to search for distance cell in distance list.
# Take row value and column value as parameters.
# The function uses row and column value to search for distance cell in
#   distance list (by calling read_distance() function), when the correct distance
#   cell is found, the function returns that distance value as floating number.
# Time complexity: O(N)
def current_distance(row_value, column_value):
    distance = float(read_distance()[row_value][column_value])
    return distance


# Create a function to search for address's row value in distance table (list).
# Take an address and a list as parameters.
# Use for loop to iterate over enumerate object with list as parameter,
#   then compare address with enumerate object, if matched, return row value in that enumerate object.
# Time complexity: O(N)
def find_row(address, target_list):
    for list_value in enumerate(target_list):
        if address == list_value[1][27]:
            row_value = list_value[0]
            break
    return row_value


## Create a function to sort package IDs in truck for shortest route and return the optimized list
#  using a greedy algorithm. The function return a list with package IDs in optimized order.
## Takes truck_list, optimized_list, and row_value as parameters.
## Firstly, the function will iterate over distance from HUB (with row value = 0) to each package's location and add
#  its distance value to a list, when the shortest distance to HUB is found, the package ID relates to that shortest distance
#  is popped from truck_list to optimized_list and the 1st package's row value is saved in a variable.
## The row value of 1st package is then used to find shortest distance of 2nd and 3rd package's location
#  with the same procedure like above, the package IDs of 2nd and 3rd package is popped from truck_list to optimized_list
#  respectively, and the row value of 3rd package is saved.
## After that, the 3rd package's row value is used in a recursive call to find the next closest package's location,
#  then popped its package ID to optimized list.
## The recursive call is processed until there's only package ID left in truck_list, the function will then
#  pop that last ID to optimized_list and return the optimized_list.
## Time complexity : O(N^2)
def optimized_truck(truck_list, optimized_list, row_value):
    # create a list for package's row value
    # create a list for package's address
    # create a list for package's distance
    row_list = []
    address_list = []
    dist_list = []

    hash_table = read_package(Hash_Table()) # Read and insert package object to hash table
    distance_table = read_distance()  # Insert distance table to distance_table

    # Add address of each package to address_list
    # Time complexity: O(N)
    for pack_id in truck_list:
        package = hash_table.get(int(pack_id))  # Get package object
        address_list.append(package.address)

    # Add row value of package to row list using find_row() function with address_list
    #   and distance table as parameters
    # Time complexity: O(N)
    for i in range(len(address_list)):
        row_list.append(find_row(address_list[i], distance_table))

    global first_pack_row  # Set first_pack_row global to use in different loops.
    global saved_row_value  # Set saved_row_value global to use in different loops.

    # conditions to find shortest distance from HUB to 1st package.
    # while optimized truck list is empty, use a for loop to iterate and add distance value to a list,
    #   use min() function to find the shortest distance in that list, then
    #   pop package ID with shortest distance from truck_list to optimized_list
    # Save row value of package ID for the next iteration.
    # Time complexity: O(N^2)
    while len(optimized_list) == 0:
        for i in range(len(row_list)):
            dist = current_distance(row_value, row_list[i]) # row_value = 0
            dist_list.append(dist)
        shortest_hub = min(dist_list)   # Get shortest distance to HUB
        index = dist_list.index(shortest_hub)   # Get index of package in distance list
        optimized_list.append(truck_list.pop(index))  # Add 1st package ID to optimized_list (remove from truck_list)
        first_pack_row = row_list.pop(index)    # Get row value of 1st package
        dist_list.clear()   # Clear distance list for the next iteration

    # Conditions to find shortest distance from last package to HUB.
    # if truck_list only have one package ID left, pop that package ID to optimized list.
    # Time complexity: O(1)
    if len(truck_list) == 1:
        optimized_list.append(truck_list.pop(0))
        row_list.pop(0)

    # Conditions to find shortest distance from previous package to current package
    # Time complexity: O(N^2)
    else:
        # Find shortest distance from 1st to 2nd package.
        # If optimized list has one item (previous package ID), use for loop to iterate and
        #   add distances from previous package ID to other package ID's location, find shortest distance
        #   from that previous package's location to the next one using min() function on dist_list, then
        #   pop that package ID from truck_list to optimized list, and finally
        #   save row value of current package ID for the next iteration.
        # Time complexity: O(N)
        if len(optimized_list) == 1:
            for i in range(len(row_list)):
                dist = current_distance(first_pack_row, row_list[i])
                dist_list.append(dist)
            shortest = min(dist_list)   # Shortest distance for second package
            index = dist_list.index(shortest)   # get package index in distance list
            optimized_list.append(truck_list.pop(index))  # Add second package to optimized_list
            saved_row_value = row_list.pop(index)     # Get row value of second package
            dist_list.clear()   # Clear distance list for the next iteration

        # Find shortest distance from 2nd package to 3rd package.
        # Use the same procedure when finding shortest distance from 1st to 2nd package,
        #   when the shortest distance is found, pop 3rd package ID from truck_list to optimized_list,
        #   then save 3rd package's row_value for recursive call.
        # Time complexity: O(N)
        else:
            for i in range(len(row_list)):
                dist = current_distance(saved_row_value, row_list[i])
                dist_list.append(dist)
            shortest = min(dist_list)
            index = dist_list.index(shortest)
            optimized_list.append(truck_list.pop(index))
            saved_row_value = row_list.pop(index)
            dist_list.clear()

        # use recursive call to find next package with shortest distance until there's only
        # one item left in truck_list
        # Time complexity: O(N^2)
        optimized_truck(truck_list, optimized_list, saved_row_value)
    return optimized_list


# Create a function to deliver packages on each truck using greedy algorithm.
# Takes truck_list, hash table, and time leave hub as parameters.
# The function use for loop to to get package index and row value of each package in order to calculate
#   the distance truck need to travel to deliver each package, then add that distance to total_distance.
# At the same time, the function records the time that truck leaves hub for each package and calculate
#   the time period it has traveled to each location, and records the time that packages is delivered.
# The function then returns total distance that truck has traveled.
# Time complexity: O(N^2)
def delivery_package(opt_truck_list, hash_table, time_leave_hub):

    # using timedelta, convert string to time format in order to
    #   calculate the time each package get delivered
    # Assign time_leave_hub to time_travel
    (h, m, s) = time_leave_hub.split(':')
    time_leave_hub = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    time_travel = time_leave_hub

    distance_list = read_distance()  # Insert distance table to distance list
    total_distance = 0

    # Use for loop to iterate over package ID in truck list and get package index (of truck list)
    #   and use find_row() function with package's address and distance list to find row value.
    # Time complexity: O(N^2)
    for pack_Id in opt_truck_list:
        my_package = hash_table.get(int(pack_Id))  # Call package objects from hash table
        package_index = opt_truck_list.index(pack_Id)  # get index of package (index 0-15)
        row_value = find_row(my_package.address, distance_list)  # index 0-27

        # Find distance from HUB to 1st package's location by checking if package package index = 0 and
        #   compare package address with address value in distance list.
        # If all conditions are met, get distance from HUB to 1st package's location by
        #   using current_distance() function. Use that distance to calculate the time truck has traveled and
        #   convert to minutes, then assign that time to distance_in_minutes.
        # Assign time_at_hub to package's time_leave for the time that truck leaves HUB
        # Add distance_in_minutes to time_travel and assign to package object's time_deli for delivery time of package
        # Add the distance that truck has traveled to total distance
        # Time complexity: O(1)
        if package_index == 0 and my_package.address == distance_list[row_value][27]:
            distance = current_distance(row_value, 0)
            truck_time = distance / 18
            distance_in_minutes = datetime.timedelta(hours=truck_time)
            my_package.time_leave = time_leave_hub
            time_travel += distance_in_minutes
            my_package.time_deli = time_travel
            my_package.status = 'Delivered'
            total_distance += distance

        # Find distance from last package's location to HUB checking if package index equals to last index of
        #   truck_list and compare package's address with address value in distance_list.
        # If all conditions are met, use the same procedure like above to find distance and the time period that
        #   truck has traveled. Assign time_leave_hub to package's time leave hub, convert time period to minutes
        #   and assign to distance_in_minutes variable.
        # Add distance_in_minutes to time_travel and assign to package object's time_deli for delivery time.
        # Assign time_at_hub to package's time_leave for the time truck leaves HUB.
        # Add distance truck traveled to total distance.
        # Time complexity: O(1)
        elif package_index == (len(opt_truck_list) - 1) and my_package.address == distance_list[row_value][27]:
            distance = current_distance(row_value, 0)
            truck_time = distance / 18
            distance_in_minutes = datetime.timedelta(hours=truck_time)
            my_package.time_leave = time_leave_hub
            time_travel += distance_in_minutes
            my_package.time_deli = time_travel
            my_package.status = 'Delivered'
            total_distance += distance

        # Find distance from previous package to next package's location after the 1st package has been delivered.
        # Use a for loop iterate over package ID in truck list and get new package objects, then compare to see
        #   if ID of previous package matched ID in package objects.
        # If condition is met, proceed to find row value of previous package and assign to column_value variable.
        # use row_value of current package and column value of previous package to find distance
        #   to the current package's location. Use that distance to calculate the time truck has traveled,
        #   then convert that time to minutes and assign to distance_in_minutes.
        # Add distance_in_minutes to time_travel and assign to package object's time_deli for delivery time of package.
        # Assign time_at_hub to package's time_leave for the time truck leaves HUB.
        # Add current distance that truck traveled to total distance.
        # Time complexity: O(N)
        else:
            if my_package.address == distance_list[row_value][27]:
                prev_index = package_index - 1  # index of previous package on truck (index 0-15) (integer)
                prev_ID = opt_truck_list[prev_index]  # assign previous package ID to prev_ID (string)
                for pack in opt_truck_list: # Find row_value of previous package
                    my_package_2 = hash_table.get(int(pack))
                    if prev_ID == my_package_2.packageId:
                        column_value = find_row(my_package_2.address, distance_list)  # row_value of prev pack
                        distance = current_distance(row_value, column_value)
                        truck_time = distance / 18
                        distance_in_minutes = datetime.timedelta(hours=truck_time)
                        my_package.time_leave = time_leave_hub
                        time_travel += distance_in_minutes
                        my_package.time_deli = time_travel
                        my_package.status = 'Delivered'
                        total_distance += distance
                        break
    return total_distance

# Create a function to report all package information and delivery status for a choosing time.
# Use hash table and time as parameters.
# Use a for loop with hash table to iterate over package's time leave hub and delivery time
#   with the following conditions:
#     -> If timeframe >= delivery time, print package object.
#     -> If time leave HUB > timeframe, change package status to 'At hub' and delivery time to 'N/A', then print package.
#     -> If time leave hub < timeframe < delivery time, change status to 'en route' and delivery time to 'N/A', print
#        packages.
# Time complexity: O(N)
def time_report(hash_call, timeframe):
    hash_size = int(len(hash_call.map)) # Get length of hash table
    for i in range(1, hash_size):  # iterate over 40 package IDs and get package objects
        my_package = hash_call.get(i)

        # print package delivered if time deli <= timeframe (package delivered correctly)
        if my_package.time_deli <= timeframe:
            print(my_package)

        # print package at hub if time leave hub > than timeframe
        elif my_package.time_leave > timeframe:
            my_package.status = 'At HUB'
            my_package.time_deli = 'N/A'
            print(my_package)

        # print package en route if time leave hub < timeframe and time deli > timeframe
        elif my_package.time_leave < timeframe < my_package.time_deli:
            my_package.status = 'en route'
            my_package.time_deli = 'N/A'
            print(my_package)