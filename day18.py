class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_begining(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_last(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert_at_position(self,position, value):
        new_node = Node(value)
        
        # case 1:
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return  
        
        temp = self.head
        count = 1
        while temp and count < position - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Position out of range..")
            return 
        
        new_node.next = temp.next
        temp.next = new_node

        if new_node.next is None:
            self.tail = new_node

    # deletion by value..............................................
    def deletion_by_value(self, value):
        if self.head is None:
            return 
        
        current = self.head

        if current.data == value:
            self.head = current.next
            if self.head is None:
                self.tail = None
            return 
        
        prev = None

        while current:
            if current.data == value:
                prev.next = current.next
                if current == self.tail:
                    self.tail = prev
                return 
            prev = current
            current = current.next

    def deletion_by_position(self, position):
        if self.head is None or position < 0:
            return False
        
        if position == 0:
            self.head = self.head.next
            return True

        current = self.head
        count = 0
        while current.next  and count < position - 1:
            current = current.next
            count += 1

        if current is None or current.next is None:
            return False
        
        current.next = current.next.next
        return True
        
        
    def print(self):
        current = self.head
        while current :
            print(current.data , end='-->')

            current = current.next

        print("None")

    def findElement(self, value):
        temp = self.head

        while temp:
            if temp.data == value:
                return True
            
            temp = temp.next
            
        return False
    
ll = LinkedList()
ll.insert_at_begining(1)
ll.insert_at_last(2)
ll.insert_at_last(3)
ll.insert_at_last(4)
ll.insert_at_begining(0)

# result = ll.deletion(int(input("Enter the value to delete: ")))
# print(result)


# result = ll.findElement(int(input("Enter the element to search: ")))
# print(result)


ll.print()
ll.deletion_by_position(int(input("Enter the position to delete: ")))
ll.print()
