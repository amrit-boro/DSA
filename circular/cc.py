class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # make list circular at a given node value
    def make_circular(self, value):
        join_node = None
        temp = self.head
        last = None

        # find node with the given value and also the last node
        while temp:
            if temp.data == value:
                join_node = temp
            last = temp
            temp = temp.next

        if last and join_node:
            last.next = join_node   # make circular

    # display with limit to avoid infinite loop
    def display(self, count=15):
        temp = self.head
        c = 0
        nodes = []
        while temp and c < count:
            nodes.append(str(temp.data))
            temp = temp.next
            c += 1
        print(" -> ".join(nodes))

    # display first node ..........................................
    # using hashing technique..

    def displayfirstNodeofCircle(self):
        seen= set()
        current = self.head

        while current:
            if current in seen:
                return current.data
            else:
                seen.add(current)
                current = current.next

        return False
    

    # using fast slow pointer..............................
    def detect_cycle_and_gives_first_node(self):
        fast  = self.head
        slow = self.head
        count = 0

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                slow = self.head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow.data
                

        return False
    

    def lenght_of_circle(self):
        fast  = self.head
        slow = self.head
        

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
               count = 1
               temp = slow.next

               while temp != slow:
                   count += 1
                   temp = temp.next

               return count
    


# Example usage
ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)

print("Before circular:")
ll.display(10)

ll.make_circular(2)  # make circular at node with value 2



result = ll.lenght_of_circle()
print(result)
# print("Is circular: \n")
# print(ll.displayfirstNodeofCircle())
# print(ll.detect_cycle_and_gives_first_node())
