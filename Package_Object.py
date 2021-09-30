# Create a Package class with package's properties in order to create package objects
# Time complexity: O(1)
class Package:
    def __init__(self, packageId, address, city, state, zipCode, deadline, mass, note, status, time_leave, time_deli):
        self.packageId = packageId
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.deadline = deadline
        self.mass = mass
        self.note = note
        self.status = status
        self.time_leave = time_leave
        self.time_deli = time_deli

    # Create a __str__ function in order to print the string presentation of package object
    # Time complexity: O(1)
    def __str__(self):
        return ('Package #' + self.packageId + ' | Delivery address: ' + self.address + ', ' + self.city +
                ', ' + self.state + ' ' + self.zipCode + ' | Deadline: ' + self.deadline + ' | Weight: ' +
                self.mass + 'kgs \n    --> Time leave HUB: ' + str(self.time_leave) + ' | Status: ' +
                self.status + ' | Delivery time: ' + str(self.time_deli) + ' <--\n')