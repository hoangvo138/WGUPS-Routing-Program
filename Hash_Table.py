import csv


# Create a hash table class in order to load package into hash table.
# Time complexity: O(N)
class Hash_Table:
    # Initialize Hash table with given size (equals to number of packages in csv file)
    # Create an array to store data in
    # Time complexity: O(N)
    def __init__(self):
        # Get total number of packages in csv file
        # Time complexity: O(N)
        with open('PackageInfo.csv') as csvPackage:
            package_size = [row for row in csv.reader(csvPackage)]
        pack_size = int(len(package_size))

        self.size = pack_size + 1   # set number of cells in hash table
        self.map = [None] * self.size   # Set every cell equals to None

    # Make a private getter and create hash key
    #   then returns array index for the key
    # Time complexity: O(1)
    def _get_hash(self, key):
        return key % self.size

    # Create an insert function
    # Time complexity: O(N)
    def insert(self, key, value):
        key_hash = self._get_hash(key)  # Assign key's array index to key_hash
        key_value = [key, value]        # Constructing a list of key and value that passing in

        if self.map[key_hash] is None:  # Check if cell is empty
            self.map[key_hash] = list([key_value])
            return True
        else:                           # If cell is not empty
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] == value
                    return True
                self.map[key_hash].append(key_value)
                return True

    # Create a get function to look up the key's value
    # Time complexity: O(N)
    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return 'Key not found!'

    # Create a delete function to delete value using key
    # Time complexity: O(N)
    def delete(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)  # Remove key's value with pop
                return True
            else:  # No match
                return False