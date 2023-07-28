# Course Schedule II
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mapping = defaultdict(list)
        for course, prereq in prerequisites:
            mapping[course].append(prereq)

        res = []
        visited, cycle = set(), set()
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)
            for prereq in mapping[course]:
                if dfs(prereq) == False:
                    return False
            cycle.remove(course)
            visited.add(course)
            res.append(course)
            return True
        for course in range(numCourses):
            if dfs(course) == False:
                return []
        return res
# Time: O(V+E) Space: O(V+E)
# We use DFS to find if there is a cycle in the graph.
# We start with all the courses in the graph and then we keep on checking the adjacent coursesed and mark them as visited.
# 