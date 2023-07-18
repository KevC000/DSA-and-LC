#Task Scheduler

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        tasks_counts = [-count for count in counts.values()]
        heapq.heapify(tasks_counts)
        q = deque()
        time = 0

        while q or tasks_counts:
            time+=1

            if not tasks_counts:
                time = q[0][1]
            else:
                count = 1 + heapq.heappop(tasks_counts)
                if count:
                    q.append([count, time+n])
            if q and time == q[0][1]:
                heapq.heappush(tasks_counts, q.popleft()[0])            
        return time

        
# Time O(N) Space O(1)
# We want to perform tasks that have higher frequency first to reduce having the chance to perform multiple of the same tasks in a row later.
# We use a heap to keep track of the items with most frequency, and a queue to keep track of avaialble tasks that went on cooldown.
# each iteration