class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertElement(self, value=None):
        new_node=  Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def print(self):
        temp = self.head

        while temp:
            print(temp.data,end="-->")
            temp = temp.next

        print("None")


    def merge2sortedLL(self, first, second):
        if first is None:
            return second
        if second is None:
            return first
        
        if first.data <= second.data:
             first.next = self.merge2sortedLL(first.next, second)
             return first
        else: 
            second.next = self.merge2sortedLL(first, second.next)
            return second
        
    def printlist(self, head=None):
        temp = head if head else self.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next
        print("None")

    # duplicate value removal.................................................
    def remove_from_sorted_list(self):
        current = self.head

        while current and current.next:
            if current.data == current.next.data:
               current.next = current.next.next
            
            else:
                current = current.next    


    def reverseList(self):

        if self.head is None:
            return False

        prev = None
        current = self.head

        while current:
            next = current.next
            current.next = prev
            prev = current
            current  =next

        self.head = prev
        return True
    
    def move_last_elementinfront(self):

        if self.head is None or self.head.next is None:
            return False
        
        prev = None
        current = self.head

        while current.next:
            prev = current
            current = current.next

        
        prev.next = None
        current.next = self.head
        self.head = current

        return True

        

        








firstList = LinkedList()
secondList= LinkedList()

print("Enter five elements for first list: \n")
for _ in range(5):
        firstList.insertElement(int(input()))
# merged_head = firstList.merge2sortedLL(firstList.head, secondList.head)
# firstList.print(merged_head)
# firstList.remove_from_sorted_list()
# firstList.print()

# firstList.reverseList()
# firstList.print()
firstList.move_last_elementinfront()
firstList.print()