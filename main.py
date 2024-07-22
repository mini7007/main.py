class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            
    def traverse(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()
    
    def to_list(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return values
        
    def from_list(self, values):
        self.head = None
        for value in values:
            self.insert(value)
            
    def sort(self, ascending=True):
        values = self.to_list()
        for i in range(len(values)):
            for j in range(0, len(values) - i - 1):
                if (ascending and values[j] > values[j + 1]) or (not ascending and values[j] < values[j + 1]):
                    values[j], values[j + 1] = values[j + 1], values[j]
        self.from_list(values)
        
    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

if __name__ == "__main__":
    linked_list = LinkedList()
    
    # Take numbers as input
    numbers = [int(x) for x in input("Enter the numbers separated by spaces: ").split()]
    
    for number in numbers:
        linked_list.insert(number)
    
    # Print the numbers by traversing the linked list
    print("Original list:")
    linked_list.traverse()
     
    # Sort in ascending order and print
    linked_list.sort(ascending=True)
    print("Sorted in ascending order:")
    linked_list.traverse()
     
    # Sort in descending order and print
    linked_list.sort(ascending=False)
    print("Sorted in descending order:")
    linked_list.traverse()
     
    # Search for a specific number
    search_number = int(input("Enter number to search: "))
    if linked_list.search(search_number):
        print(f"{search_number} is present in the list")
    else:
        print(f"{search_number} is not present in the list")
