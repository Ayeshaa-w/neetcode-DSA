class Solution:
    def addTwoNumbers(self, l1, l2):
        # Convert linked list to number
        def to_number(node):
            num = 0
            place = 1
            while node:
                num += node.val * place
                place *= 10
                node = node.next
            return num

        n1 = to_number(l1)
        n2 = to_number(l2)

        total = n1 + n2

        # Convert number back to linked list
        dummy = ListNode(0)
        curr = dummy

        # Special case if total = 0
        if total == 0:
            return ListNode(0)

        while total > 0:
            digit = total % 10
            curr.next = ListNode(digit)
            curr = curr.next
            total //= 10

        return dummy.next