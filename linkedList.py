class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList:

    def __init__(self):
        self.head = None


    # Display the list
    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


    # Insert at beginning
    def insert_at_beginning(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new


    # Insert at end
    def insert_at_end(self, data):
        new = Node(data)

        if not self.head:
            self.head = new
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new


    # Insert at specific position
    def insert_at_position(self, pos, data):

        if pos == 0:
            self.insert_at_beginning(data)
            return

        new = Node(data)

        temp = self.head
        count = 0

        while temp and count < pos - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Position out of range")
            return

        new.next = temp.next
        temp.next = new


    # Delete first node
    def delete_at_beginning(self):

        if not self.head:
            return

        self.head = self.head.next


    # Delete last node
    def delete_at_end(self):

        if not self.head:
            return

        if not self.head.next:
            self.head = None
            return

        temp = self.head

        while temp.next.next:
            temp = temp.next

        temp.next = None


    # Search element
    def search(self, data):

        temp = self.head

        while temp:
            if temp.data == data:
                return True
            temp = temp.next

        return False


    # Find length
    def length(self):

        temp = self.head
        count = 0

        while temp:
            count += 1
            temp = temp.next

        return count


    # Check if list is empty
    def is_empty(self):
        return self.head is None


ll = SinglyLinkedList()

ll.insert_at_beginning(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_end(40)

ll.display()