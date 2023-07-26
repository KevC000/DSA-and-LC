# Course Scehdule

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        mapping = defaultdict(list)
        for course, prereq in prerequisites:
            mapping[course].append(prereq)
    
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if not mapping[course]:
                return True
            visited.add(course)
            for prereq in mapping[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            mapping[course] = []
            return True
        for course in list(mapping):
            if not dfs(course):
                return False
        return True
    
# Time: O(V+E) Space: O(V+E)
# We use DFS to find if there is a cycle in the graph.
# We start with all the courses in the graph and then we keep on checking the adjacent coursesed and mark them as visited.
# We keep on doing this until there are no more courses left.