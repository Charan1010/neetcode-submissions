# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:


        list3, list3_head = None, None

        while list1 != None and list2 != None:

            if list1.val <= list2.val:

                if list3 == None:
                    list3 = list1
                    list3_head = list3
                else:
                    list3.next = list1
                    list3 = list3.next

                list1 = list1.next

            else:

                if list3 == None:
                    list3 = list2
                    list3_head = list3
                else:
                    list3.next = list2
                    list3 = list3.next
                    
                list2 = list2.next

            print(list3)

        if list2 != None :
            if list3 == None:
                list3 = list2
                list3_head = list3
            else:
                list3.next = list2
        elif list1 != None:
            if list3 == None:
                list3 = list1
                list3_head = list3
            else:
                list3.next = list1

        return list3_head
        