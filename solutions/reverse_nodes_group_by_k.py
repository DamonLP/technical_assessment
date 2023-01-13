import sys

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseNodesGroupByK(self, head, k):
        # Add dummy head to avoid edge case
        # e.g. head = 1->2->3, k=2
        ## new_head = 0->1->2->3
        new_head = ListNode(0, head)
        shifted_head = new_head

        while True:
            # e.g. shifted_k_head = 2->3
            shifted_k_head = self.shifting_k(shifted_head, k)
            # if no group of k remaining in shifted_head, return
            if shifted_k_head == None:
                break
            
            # Reference point for when to stop reversing group of k
            # e.g. shifted_k_head_next = 3
            shifted_k_head_next = shifted_k_head.next
            
            # Active point to update 'next'
            # e.g. current = 1->2->3
            current = shifted_head.next
            # Previous point of current point
            # e.g. previous = 3
            previous = shifted_k_head.next
            # reversing the first group of k, stop if current == shifted_k_head_next
            # e.g. in result shifted_k_head = 2->1->3
            while current != shifted_k_head_next:
                next = current.next
                current.next = previous
                previous = current
                current = next

            # Update shifted_head to the next group of k previous head
            next = shifted_head.next
            shifted_head.next = shifted_k_head
            shifted_head = next

        # return result without dummy head
        return new_head.next

    def shifting_k(self, head, k):
        while head != None and k > 0:
            head = head.next
            k -= 1
        return head

def printListNode(listnode):
    vals = []
    while listnode:
        vals.append(listnode.val)
        listnode = listnode.next
    print(vals)

solution = Solution()
test = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print('head=[1,2,3,4,5], k=2')
result_node = solution.reverseNodesGroupByK(test, 2)
printListNode(result_node)
test = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print('head=[1,2,3,4,5], k=3')
result_node = solution.reverseNodesGroupByK(test, 3)
printListNode(result_node)