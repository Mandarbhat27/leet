class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:

        car = 0
        dig = ListNode(0)
        cur = dig

        while l1 or l2:

            if l1 is not None:
                v1 = l1.val
            else:
                v1 = 0

            if l2 is not None:
                v2 = l2.val
            else:
                v2 = 0

            tot = v1 + v2 + car

            digit = tot % 10
            car = tot // 10

            cur.next = ListNode(digit)
            cur = cur.next

            if l1 is not None:
                l1 = l1.next

            if l2 is not None:
                l2 = l2.next

        if car > 0:
            cur.next = ListNode(car)

        return dig.next