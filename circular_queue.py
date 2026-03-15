class CircularQueue:
    def __init__(self, size):
        self.size = size
        # Pre-allocate the list with None to represent empty slots
        self.items = [None] * size
        self.front = -1
        self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front


    def is_empty(self):
        return self.rear == -1

    def enqueue(self, value):
        if self.is_full():
            print(f"Error: Queue is full. Cannot insert {value}")
            return False

            # If this is the very first element being added
        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.items[self.rear] = value

    def dequeue(self):
        if self.is_empty():
            print("the list is empty")
            return None

        remove = self.items[self.front]
        self.items[self.front] = None

        if self.rear == self.front:
            self.rear = -1
            self.front = -1


    def display(self):



# --- TEST DRIVE ---
# 1. Create a queue of size 3
cq = CircularQueue(3)

# 2. Fill it up
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.display()

# 3. Try to add to a full queue
cq.enqueue(40)

# 4. Remove one item (10)
cq.dequeue()
cq.display()

# 5. Wrap Around: Add 40 again (it will now go into index 0!)
cq.enqueue(40)
cq.display()