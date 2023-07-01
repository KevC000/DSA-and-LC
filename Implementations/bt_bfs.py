from collections import deque

def bfs(root):
    if not root: return
    q = deque([root])
    while len(q) > 0:
        for i in range(len(q)):
            top = q.popleft()
            print(top.val)
            if top.left:
                q.append(top.left)
            if top.right:
                q.append(top.right)
        
            