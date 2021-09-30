'''Student name: Hoang M Vo'''
'''Student ID: 001126686'''

import datetime
from Hash_Table import Hash_Table
from Read_File import loading_truck
from Read_File import read_package
from Distance_Calc import optimized_truck
from Distance_Calc import delivery_package
from Distance_Calc import time_report

class Main:
    # Create empty list for normal trucks
    first_truck = []
    second_truck = []
    third_truck = []

    # Create empty list for optimized trucks
    opt_first_truck = []
    opt_second_truck = []
    opt_third_truck = []

    # Load packages onto each normal truck with specific conditions from package's notes and delivery deadline
    loading_truck(first_truck, second_truck, third_truck)

    # Sort and add packages to optimized truck list to get the shortest route
    opt_first_truck = optimized_truck(first_truck, opt_first_truck, 0)
    opt_second_truck = optimized_truck(second_truck, opt_second_truck, 0)
    opt_third_truck = optimized_truck(third_truck, opt_third_truck, 0)

    # Call hash table and assign to hash_map
    hash_map = read_package(Hash_Table())

    # Get total distances of all trucks with specific time when they leave HUB
    # Time complexity: O(N^2)
    total_distance = delivery_package(opt_first_truck, hash_map, '8:00:00') + \
                     delivery_package(opt_second_truck, hash_map, '9:05:00') + \
                     delivery_package(opt_third_truck, hash_map, '10:30:00')


    # Create a function to check if package has been delivered on time
    # Take hash table as parameter
    # The function uses a for loop to call up package object in hash table,
    #   then uses condition statements to compare package delivery deadline and
    #   the time package was delivered. If package deadline is EOD, count plus 1.
    #   If package delivery time is smaller than deadline, count plus 1.
    # Time complexity: O(N)
    def check_time(hash_call):
        count = 0
        for i in range(1, 41):
            package = hash_call.get(i)
            if package.deadline == 'EOD':
                count += 1
            elif package.deadline == '10:30' or package.deadline == '9:00':
                (h, m) = (package.deadline).split(':')
                deadline_time = datetime.timedelta(hours=int(h), minutes=int(m))
                if package.time_deli <= deadline_time:
                    count += 1
                else:
                    print("The package that was not delivered on time")
                    print(package)
        return count

    # Check if all packages are delivered on time
    total_package = check_time(hash_map)

    # Create an interface for the user when the program is running
    # Print the total distance that all trucks have traveled
    # Prompt user to input keyword to navigate the interface
    print('\nWelcome to the Western Governor University Parcel Service - WGUPS')
    print('Total distance for all trucks to deliver 40 packages is: %.1f miles' % total_distance)

    # Check if all 40 packages are delivered on time, if correct, print to let user know
    # all packages were delivered on time, if not correct, let user know total number of
    # packages that were delivered on time and print the package that was not delivered on time.
    if total_package == 40:
        print('All packages were delivered on time!')
    else:
        print('Only %d packages were delivered on time!' % total_package)

    print()
    print('Please enter the following keywords to navigate the interface: \n' +
          '   - "report" -> print all package status at three specific time (9:20, 10:20, 13:10) \n' +
          '   - "timestamp" -> print all package status at a specific time \n' +
          '   - "lookup" -> print information and delivery status of a specific package. \n' +
          '   - "exit" -> exit the program \n')

    # Using a while loop to check for incorrect input from user, if incorrect input happens,
    #   prompt user to input correct keywords and loop back to prompt screen,
    #   if input is correct, break the loop and go to the next statement.
    # Time complexity: O(N)
    while True:
        user_input = input('User input: ')
        if user_input != 'report' and user_input != 'timestamp' and user_input != 'lookup' and user_input != 'exit':
            print('Please enter the correct keyword.\n')
            continue
        else:
            break

    # If input is 'lookup', use a while loop to prompt user to input package ID in integer,
    #   if input is not an integer or integer input is out of range, prompt user to enter
    #   an integer within acceptable range (1 to 40) and loop back to asking for input prompt.
    # If input is correct, use for loop to call up package object in hash table and compare
    #   package ID with user input, then print out package object with matched ID and
    #   break the loop.
    # Time complexity: O(N^2)
    if user_input == 'lookup':
        while True:
            try:
                lookup_input = int(input('Please enter a package ID: '))
                if lookup_input > 40 or lookup_input < 1:
                    print('Out of range, please enter an integer from 1 to 40 \n')
                    continue
                else:
                    hash_size = int(len(hash_map.map)) # Get length of of hash table
                    for i in range(1, hash_size):
                        my_package = hash_map.get(i)
                        if my_package.packageId == str(lookup_input):
                            print()
                            print(my_package)
                    print('Thank you for choosing WGUPS!')
                    break
            except ValueError:
                print('Invalid input, please enter an integer \n')
                continue

    # if input is 'report', proceed to print all package information in three timeframes.
    # Use timedelta to convert timeframe in string to HH:MM:SS time format, then prompt user
    #   to input an integer in the range 1-3 to get package status at each timeframe,
    #   using a while loop to check for correct input format.
    # If integer input is correct, use time_report function to compare delivery time and
    #   time leave hub of package WITH timeframe.
    # If timeframe >= delivery time, print package object.
    # If time leave HUB > timeframe, change package status to 'At hub' and delivery time to 'N/A', then print package.
    # If time leave hub < timeframe < delivery time, change status to 'en route' and delivery time to 'N/A', print
    #   packages and break while loop.
    # Time complexity: O(N^2)
    elif user_input == 'report':
        hash_1 = hash_map
        hash_2 = hash_map
        hash_3 = hash_map
        time_one = '9:20:00'
        time_two = '10:20:00'
        time_three = '13:10:00'
        (a, b, c) = time_one.split(':')
        (h, m, s) = time_two.split(':')
        (x, y, z) = time_three.split(':')
        time_frame_one = datetime.timedelta(hours=int(a), minutes=int(b), seconds=int(c))
        time_frame_two = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        time_frame_three = datetime.timedelta(hours=int(x), minutes=int(y), seconds=int(z))
        print('Enter "1" for package status at 9:20:00 \n'
              'Enter "2" for package status at 10:20:00 \n'
              'Enter "3" for package status at 13:10:00 \n')

        while True:
            try:
                report_input = int(input('Input: '))
                if report_input > 3 or report_input < 1:
                    print('Out of range, please enter an integer from 1 to 3 \n')
                    continue
                else:
                    if report_input == 1:   # Check package status with timeframe one
                        print('\nPackage status at 9:20:00\n')
                        time_report(hash_1, time_frame_one)
                    elif report_input == 2: # Check package status with timeframe two
                        print('\nPackage status at 10:20:00\n')
                        time_report(hash_2, time_frame_two)
                    else:   # Check package status with timeframe three
                        print('\nPackage status at 13:10:00\n')
                        time_report(hash_3, time_frame_three)
                    print('Thank you for choosing WGUPS!')
                    break
            except ValueError:
                print('Invalid input, please enter an integer \n')
                continue

    # If user input is 'timestamp', prompt user to input time in format HH:MM:SS
    # Use a while loop to check for incorrect format, if input incorrect, prompt user to input
    #   the right format and loop back to prompt input.
    # If input format correct, use timedelta to convert time in string to time format,
    #   then user that time format in time_report function compare with package's time leave hub
    #   and delivery time. Proceed to print out all package status at that time and break while loop
    # Time complexity: O(N^2)
    elif user_input == 'timestamp':
        while True:
            try:
                time_input = input('Please input a time (format HH:MM:SS): ')
                (h, m, s) = time_input.split(':')
                time_stamp = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                print()
                time_report(hash_map, time_stamp)
                print('Thank you for choosing WGUPS!')
                break
            except ValueError:
                print('Invalid input, please enter timestamp in format HH:MM:SS\n')
                continue

    # If user input is 'exit', exit program
    elif user_input == 'exit':
        print('Thank you for choosing WGUPS!')
        exit()