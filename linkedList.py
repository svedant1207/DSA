class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class CircularLinkedList:

    def __init__(self):
        self.head = None


    # Display
    def display(self):

        if not self.head:
            return

        temp = self.head

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(back to head)")

    def insert_begin(self,val):
        new = Node(val)
        if not self.head:
            self.head = new
            new.next = new

        new.next = self.head
        self.head = new

    def insert_pos(self,val):
