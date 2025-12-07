class LinkedList:
    def __init__(self):
        self.head = None  # initially empty list

    # Insert at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # empty list
            self.head = new_node
            return
        last = self.head
        while last.next:  # traverse till last node
            last = last.next
        last.next = new_node

    # Insert at beginning
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Delete a node
    def delete(self, key):
        temp = self.head

        # If head node itself holds the key
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:  # not found
            return
        prev.next = temp.next
        temp = None

    # Search a value
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    # Print list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
