# Sol 1

# head = [1,2,3,4,5]

# def reverseLL(head):
#     current = head
#     prev = None
#     while current:
#         next = current.next
#         current.next = prev
#         prev = current
#         current = next
#     return prev
# print(reverseLL(head))

# sol 2

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLL(head):
    current = head
    prev = None

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev

# Convert the list [1, 2, 3, 4, 5] into a linked list
head = ListNode(1)
current = head
for val in [2, 3, 4, 5]:
    new_node = ListNode(val)
    current.next = new_node
    current = new_node

# Reverse the linked list
reversed_head = reverseLL(head)

# Print the reversed linked list values
while reversed_head:
    print(reversed_head.val)
    reversed_head = reversed_head.next
