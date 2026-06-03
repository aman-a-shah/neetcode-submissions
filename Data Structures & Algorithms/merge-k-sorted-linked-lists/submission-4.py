# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        currs = [curr for curr in lists]
        dummy = ListNode()
        curr = dummy

        while len(currs) > 0:
            # find min val in currs -> remove 'None'
            # set next to that curr index in currs
            # push that curr forward
            # save prev

            min_so_far = currs[0]
            min_index = 0
            for i, curr1 in enumerate(currs):
                if curr1.val < min_so_far.val:
                    min_so_far = curr1
                    min_index = i
            
            curr.next = min_so_far
            curr = curr.next
            if min_so_far.next is not None:
                currs[min_index] = min_so_far.next
            else:
                currs.pop(min_index)

        return dummy.next
