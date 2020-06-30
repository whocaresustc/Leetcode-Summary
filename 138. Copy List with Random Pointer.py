# O(N) O(N)
class Solution:
    def __init__(self):
        self.visited = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        if head in self.visited:
            return self.visited[head]
        node = Node(head.val, None, None)
        self.visited[head] = node
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node