class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insertFront(self, val):
        new_node = ListNode(val)
        if self.head == None:      
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node
        
    def insertEnd(self,val):
        new_node = ListNode(val)
        if self.head == None:      
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
        self.tail = new_node
        
    def deleteFront(self):
        if self.head == None:
            return
        else:
            new_head = self.head.next
            self.head.next = None
            self.head = new_head
        
    def deleteEnd(self):
        if self.head == None:
            return
        else:
            new_tail = self.tail.prev         
            self.tail.prev = None
            self.tail = new_tail
            
            if new_tail:                
                new_tail.next = None
                
        
    def traverse(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next

dll = DLL()

# dll.insertFront(5)
# dll.insertFront(6)
# dll.insertFront(7)

dll.insertEnd(1)
dll.insertEnd(2)
dll.insertEnd(3)
dll.deleteFront()

dll.traverse()
        