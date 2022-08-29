class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a = r = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                a.next = list1
                list1, a = list1.next, list1
            else:
                a.next = list2
                list2, a = list2.next, list2
                
        if list1 or list2:
            a.next = list1 if list1 else list2
            
        return r.next