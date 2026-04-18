class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        curr = self.head
        count = 0
        while count < index:
            if curr is None:
                return -1
            
            curr = curr.next
            count += 1
        if curr is None:
            return -1
        return curr.val

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head
        self.head  = newNode

    def insertTail(self, val: int) -> None:
        endNode = ListNode(val)
        if self.head is None:
            self.head = endNode
            return 
        
        curr = self.head
        while curr.next is not None:
                curr = curr.next
        curr.next = endNode


    def remove(self, index: int) -> bool:
        if index == 0:
            if self.head is None:
                return False

            self.head = self.head.next

            return True

        curr = self.head
        count = 0 
        while count < index - 1:
            if curr is None:
                return False

            curr = curr.next
            count += 1

        if curr is None or curr.next is None:
            return False
        curr.next = curr.next.next
        return True 

    def getValues(self) -> List[int]:
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.val)
            curr = curr.next
        return result