'''
web dev...
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def insertAtbeg(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        
        # insert new_node
        else:         
            new_node.next = self.head
            self.head= new_node

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return 

        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new_node

    def total_lenght(self):
        temp = self.head
        count = 0
        while temp:
            count+=1
            temp = temp.next
        print("Total lenght: ")
        return count
    
    def find_element(self, k):
        temp = self.head
        index = 0
        while temp:
            if temp.data == k:
                return index, temp.data
            index  += 1
            temp = temp.next

        return False
        
  
    def insert_at_position(self,position, value):
        new_node = Node(value)
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        count = 1
        while temp and count < position -1:
            temp = temp.next
            count += 1
        if temp is None:
            print("Position out of range")
            return
        
        new_node.next = temp.next
        temp.next = new_node

    def deleteByvalue(self, value):
        if self.head is None:
            return 
        
        current = self.head
        prev= None
        if current.data == value:
            self.head = current.next
            return
        while current:
            if current.data == value:
                prev.next = current.next

                return
            prev = current
            current = current.next

    # using loop...........................   
    def reverselist(self):
        if self.head is None:
            return 
        
        prev =None
        current= self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev
        return True

    def reverselist2(self, head):
        if head is None:
            return 
        
        prev =None
        current= head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        return prev
        
    # using recursion.......................
    def reverseList_recursion(self,node):
        def help_reverse(node):
            if node is None or  node.next is None:
                return node
            new_head = help_reverse(node.next)
            node.next.next = node
            node.next = None
            return new_head

        self.head = help_reverse(self.head)
        return True
    
    # worst case.......................................
    def middleNode(self):
        temp = self.head
        total = 0
        while temp:
            total += 1
            temp = temp.next
        mid = total // 2
        value = self.head
        for i in range(mid):
            value = value.next
        return value.data
    
    # best case......................................
    def middle_best(self):
        slow =self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data
            

    #worst case.....................................:

    def find_nth_node_fromEnd(self,Nth):
        if not self.head :
            return False
        temp = self.head
        total = 0
        while temp:
            total +=1 
            temp = temp.next
        value = self.head
        if total < Nth:
            return False
        rangee = total-(Nth-1)

        for _ in range(1,rangee):
            value = value.next
        return f"result: {value.data}"
     
    # Best case using two pointer....................

    def find_nth_node_fromEnd(self, Nth):
        if not self.head or Nth <= 0:
            return False  # invalid input
        
        first = self.head
        second = self.head

        # Move 'first' Nth steps ahead
        for _ in range(Nth):
            if not first:   # list shorter than Nth
                return False
            first = first.next

        # Move both pointers until 'first' reaches the end
        prev = None
        while first is not None:
            prev = second
            first = first.next
            second = second.next

        return second.data
    
    # delete node from the end BRUTE force......................
    def deleteNode_from_end(self, Nth):
        temp = self.head
        total_lenght = 0
        while temp:
            total_lenght += 1
            temp = temp.next

        if total_lenght < Nth:
            return -1
        new_length = (total_lenght-Nth)+1

        if new_length == 1:
            self.head = self.head.next
            return  self.head.data
        # loop to the destination....
        new_temp = self.head
        prev = None
        for i in range(1,new_length):
            prev = new_temp
            new_temp = new_temp.next
        
        prev.next = new_temp.next
        return self.head
    
    # best approach using two pointer......

    def delete_node_from_end_best(self, nth):
        first  = self.head
        second = self.head

        for i in range(nth):
            if not first:
                return -1
            first = first.next
        if not first:
            self.head = self.head.next
            return 
        prev = None
        while first:
            prev = second
            first = first.next
            second = second.next
        prev.next = second.next


    # remove duplicate sorted  element;
    def duplicate(self):
        current = self.head
        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next
                
            else:
                current = current.next
       
    # day 28..........................................................................................................
    
    # remove duplicate unsorted list: Brute force.....
    def removeDuplicates(self):
        current = self.head
        
        while current != None:
            runner = current
            while runner.next != None:
                if runner.next.data == current.data:
                    runner.next = runner.next.next   # delete duplicate
                else:
                    runner = runner.next
            current = current.next
        
        return current
    
    # best case : remov duplicate unsorted list ..

    def removeduplicates(self):
        seen = set()
        current = self.head
        prev = None

        while current:
            if current.data in seen:
                prev.next = current.next
            else:
                seen.add(current.data)
                prev = current

            current = current.next

    def deleteAllDuplicates_bruteforce__part_II(self):  # 1 1 1 2 3 3 --> 2 (only unique element) (Brute froce........)
            if not self.head:
                return None

            # 1st pass: count frequencies
            freq = {}
            curr = self.head
            while curr:
                freq[curr.data] = freq.get(curr.data, 0) + 1
                curr = curr.next

            # 2nd pass: remove duplicates (careful with head)
            while self.head and freq[self.head.data] > 1:
              
                self.head = self.head.next   # move head forward if duplicate
   
            curr = self.head
            while curr and curr.next:
               
                if freq[curr.next.data] > 1:   # if next node is duplicate
                    curr.next = curr.next.next
                else:
                    curr = curr.next
            return self.head

    # .........................................................................................................

    # DAY 29......
    # Dummy Node concept .../////

    def deleteAllDuplicates_bruteforce__part_II_using_dummy(self):
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        current = self.head

        while current:
            if current.next and current.data == current.next.data:
                while current.next and current.data == current.next.data:
                    current = current.next
                prev.next = current.next
            else:
                prev = prev.next

            current = current.next

        self.head = dummy.next

    #brute force........................................using hasmap
    def detect_loop(self):
        seen = set()
        temp = self.head

        while temp:
            if temp in seen:
                return temp.data  # Deceted loop and return the starting node of the circle
            else:
                seen.add(temp)
                temp = temp.next
        return False
    # best approach ............ using  (Floyd’s cycle detection)
    def detect_cycle(self):
        fast  = self.head
        slow = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return slow.data
            
        return False
    

    # day 1 septeber........................................................................................................

    def intersection(self, head1, head2):
        #https://leetcode.com/problems/intersection-of-two-linked-lists/
        pass

    # merget two sorted linked list using extra space ........................brute force..
    def mergeTwosortedArray(self, head1, head2):
       
        first = head1
        second = head2
        arr = []

        while first or second:
            if first:
                arr.append(first.data)
                first = first.next

            if second:
                arr.append(second.data)
                second = second.next

        sorted_arr = sorted(arr)
        
        head = Node(sorted_arr[0])
        current= head

        for value in sorted_arr[1:]:
            current.next = Node(value)
            current = current.next

        self.head= head

    # Optimal solution of the merge two sorted list  using dummy node..........................
    # Iterative way.................................
    def merge(self, headA, headB):
        first, second = headA,headB
        dummy = Node(0)
        current = dummy

        while first and second:
            if first.data < second.data:
                current.next = first
                first = first.next

            else:
                current.next = second
                second = second.next

            current = current.next

        current.next = first or second
        return dummy.next
    

    # Sort a linked list............
    # Recursion way...........................................................:
    def merge_recursion(self, headA, headB):
        if not headA:
            return headB
        if not headB:
            return headA

        if headA.data <= headB.data:
            headA.next = self.merge_recursion(headA.next, headB)
            return headA
        else:
            headB.next = self.merge_recursion(headA, headB.next)
            return headB


    def get_middle(self, head):
        if not head:
            return 

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow   # ✅ middle node


    def split(self, head):
        if not head or not head.next:
            return head

        middle = self.get_middle(head)
        middle_next = middle.next
        middle.next = None  # split list

        left = self.split(head)
        right = self.split(middle_next)

        return self.merge_recursion(left, right)


    def sort(self ):
        self.head = self.split(self.head)   # ✅ update head

    def addTwoNo(self, headA, headB):
        first, second = headA, headB
        dummy = Node(0)
        current = dummy
        carry = 0
        while first or second or carry:
            val1 = first.data if first else 0
            val2 = second.data if second else 0

            result = val1 + val2 + carry
            carry = result // 10
            current.next = Node( result % 10)
            current = current.next

            first = first.next if first else None
            second = second.next if second else None

        self.head = dummy.next

    # Check palindrome.....................................

    def palindrome(self, headA):
        if not headA or not headA.next:
            return True
        
        # find the middle of the node:.......

        fast, slow = headA, headA
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half................
        second_half = self.reverselist2(slow)

        first, second = headA, second_half

        while second:
            if first.data != second.data:
                return False
            first = first.next
            second = second.next

        return True
    

    # day 2 .............................................................................................................

    def rotate_by_k(self, k):
        if not self.head or not self.head.next or k == 0 :
            return self.head
        
        length = 1
        tail = self.head
        while tail.next :
            length += 1
            tail = tail.next

        # find k (jaga)...
        k = k % length
        if k == 0:
            return self.head
        
        new_tail = self.head
        for _ in range(length - k - 1):
            new_tail = new_tail.next                # 1      2     3     @4       5 
        
        new_head = new_tail.next

        # Step 4: Break and reconnect

        new_tail.next = None
        tail.next = self.head
        
        self.head = new_head






    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next
        print("None")

    # def diplay(self):
    #     temp = self.head
    #     while temp:
    #         print(temp.data, end='-->')
    #         temp = temp.next

    #     print("None")


ll = LinkedList()
ll2 = LinkedList()
# for _ in range(1):
#     ll.insertAtbeg(int(input()))
limit= int(input("Enter how elements do you want to insert"))
for _ in range(limit):
    ll.insert_at_end(int(input()))

# limit2= int(input("Enter how elements do you want to insert"))

# for _ in range(limit2):
#     ll2.insert_at_end(int(input()))
# ll.move_last_elementinfront()
# print(ll.total_lenght())
# print(ll.find_element(int(input("Enter the element to search: "))))
# ll.insert_at_position(3,9)
# ll.deleteByvalue(int(input("Enter the value to delete: ")))
# ll.reverselist()
# print(ll.reverseList_recursion(ll.head))
# print(ll.middle_best())
# print(ll.find_nth_node_fromEnd(int(input("Enter the nth node: "))))
ll.rotate_by_k(int(input("Enter the no to rotate: ")))

# print(ll.deleteNode_from_end(int(input("Enter the value to delete the node from the end: "))))
# ll.delete_node_best(int(input("Enter the value to delete the node from the end: ")))
# ll.duplicate()
# ll.removeDuplicates() brute force...
# ll.removeduplicates()

# print(ll.deleteAllDuplicates_bruteforce__part_II())
# ll.deleteAllDuplicates_bruteforce__part_II_using_dummy()

# ll.deleteNode_dummy(int(input("Enter the value to delete: ")))
# ll.deleteAllDuplicates_bruteforce__part_II_using_dummy()
# ll.detect_cycle()
# result = ll.intersection(ll.head,ll2.head) # pass the head of the list ...
# print(result)
# result = ll.mergeTwosortedArray(ll.head, ll2.head)
# ll.merge_recursion(ll.head, ll2.head)
# ll.sort()
# ll.addTwoNo(ll.head,ll2.head)
# result = ll.palindrome(ll.head)
# print(result)
ll.display()