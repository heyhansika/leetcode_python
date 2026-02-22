class Solution:
    def deleteDuplicates(self, head):
        # Dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:
            # Check if current node has duplicates
            if curr.next and curr.val == curr.next.val:
                # Skip all nodes with this duplicate value
                dup_val = curr.val
                while curr and curr.val == dup_val:
                    curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next

        return dummy.next
