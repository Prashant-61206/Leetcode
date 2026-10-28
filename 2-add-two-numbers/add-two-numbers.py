# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        num_sum=self.collectNumbers(l1)+self.collectNumbers(l2)
        newlist=self.NewList(num_sum)
        return newlist
    def collectNumbers(self,slist:ListNode):
            value=[]
            pointer=slist
            while pointer!=None:
                value.append(pointer.val)
                pointer=pointer.next
            num=''
            for i in value:
                num=num+str(i)

            return int((num)[::-1])
    def NewList(self,value:int|None):
        valuestr=(str(value))
        dumpy=ListNode(0)
        current=dumpy
        for i in reversed(valuestr):
            current.next=ListNode(int(i))
            current=current.next
        return dumpy.next
            
        