class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
            
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def print_list(self):
        if self.head is None:
            print("List is empty")
            return
            
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    def delete_nth(self, n):
        if self.head is None:
            raise ValueError("Cannot delete from empty list")
            
        if n < 1:
            raise ValueError("Index must be positive")
            
        if n == 1:
            self.head = self.head.next
            return
            
        current = self.head
        count = 1
        
        while current and count < n - 1:
            current = current.next
            count += 1
            
        if current is None or current.next is None:
            raise ValueError("Index out of range")
            
        current.next = current.next.next

# Test the implementation
if __name__ == "__main__":
    # Create a new linked list
    llist = LinkedList()
    
    # Add some elements
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(4)
    
    print("Original list:")
    llist.print_list()
    
    # Test deletion
    try:
        print("\nDeleting 2nd node:")
        llist.delete_nth(2)
        llist.print_list()
        
        print("\nTrying to delete node at invalid index:")
        llist.delete_nth(10)
    except ValueError as e:
        print(f"Error: {e}")
    
    # Test deletion from empty list
    try:
        empty_list = LinkedList()
        empty_list.delete_nth(1)
    except ValueError as e:
        print(f"\nError: {e}")