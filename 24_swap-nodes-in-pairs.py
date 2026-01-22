class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head
        # 1234
        #  21 43
        curr = head
        result = head.next # 2
        prev = None
        while curr and curr.next:
            first = curr
            second = curr.next
            
            next_pair = second.next
            
            second.next = first
            first.next = next_pair

            if prev:
                prev.next = second
            prev = first
            curr = next_pair
        return result

# 这个写过很多次了，但是每一次都会忘记细节，尤其是prev的处理
# 比如一个情况是1-2-3-4，但是如果没有prev的话，2-1-4-3就断开了 会变成2-1-3 