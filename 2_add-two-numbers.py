
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0, None)
        result = head
        add_one = 0

        while l1 and l2:
            curr = (l1.val + l2.val + add_one) % 10
            if l1.val + l2.val + add_one >= 10:
                add_one = 1
            else:
                add_one = 0
            head.next = ListNode(curr)
            head = head.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            curr = (l1.val + add_one) % 10
            if l1.val + add_one >= 10:
                add_one = 1
            else:
                add_one = 0
            head.next = ListNode(curr)
            head = head.next
            l1 = l1.next

        
        while l2:
            curr = (l2.val  + add_one) % 10
            if l2.val  + add_one >= 10:
                add_one = 1
            else:
                add_one = 0
            head.next = ListNode(curr)
            head = head.next
            l2 = l2.next
        if add_one == 1:
            head.next = ListNode(1)
        return result.next

# 优化后：
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # 使用哑节点简化头部处理
        curr = dummy
        carry = 0  # 进位

        # 只要还有节点没处理完，或者还有进位，就继续循环
        while l1 or l2 or carry:
            # 如果节点为空，则取值为 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # 计算总和与进位
            total = val1 + val2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            
            # 移动指针
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2.next
            
        return dummy.next