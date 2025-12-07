from typing import Optional

class ListNode:
    def __init__(self, value, next= None):
        self.value= value;
        self.next= next;
    
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """         
        merged_arr= []
        i, j= 0, 0;
        while (i< len(list1) and j< len(list2)):
            if list1[i] < list2[j]:
                merged_arr.append(list1[i])
                i+=1
            else:
                merged_arr.append(list2[j])
                j+=1
        merged_arr.extend(list1[i:])
        merged_arr.extend(list2[j:])
        return merged_arr
    
    def mergeTwoListNode(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        if not list1:
            return list2
        if not list2:
            return list1
        dummyNode= ListNode(-1)
        currentNode= dummyNode
        ptr1, ptr2= list1, list2
        while(ptr1 and ptr2):
            if (ptr1.value < ptr2.value):
                currentNode.next= ptr1
                ptr1= ptr1.next
            else:
                currentNode.next= ptr2
                ptr2= ptr2.next
            currentNode= currentNode.next
        if ptr1:
            currentNode.next=ptr1
        if ptr2:
            currentNode.next= ptr2
        return dummyNode.next
    def displayLinkedList(self, head:Optional[ListNode]):
        if not head:
            print("Not Found")
        ptr= head;
        while ptr:
            print(ptr.value, end="->")
            ptr= ptr.next;
        print()
            
list1= ListNode(1)   
list1.next= ListNode(3) 
list1.next.next= ListNode(5) 
list1.next.next.next= ListNode(7) 
    
list2= ListNode(2)   
list2.next= ListNode(4) 
list2.next.next= ListNode(6) 
list2.next.next.next= ListNode(8) 

obj= Solution()
sorted_node=obj.mergeTwoListNode(list1, list2)
print(sorted_node)

obj.displayLinkedList(list1)
obj.displayLinkedList(list2)
obj.displayLinkedList(sorted_node)

        