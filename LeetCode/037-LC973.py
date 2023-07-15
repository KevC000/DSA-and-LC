#Closest Points to Origin

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_to_point = {}
        distances = []
        result = []

        for i, point in enumerate(points):
            x, y = point
            distance = (x**2 + y**2)**0.5
            heapq.heappush(distances, distance)
            if distance not in distance_to_point:
                distance_to_point[distance] = []
            distance_to_point[distance].append(i)
        
        for i in range(k):
            closest =  heapq.heappop(distances)
            point_index = distance_to_point[closest].pop()
            point = points[point_index]

            result.append(point)
        return result

# Time: O(N), Time O(N)
# Store each points's distance to a heap and use a dictionary to map the distances to the indices of the original array
# Since the same distances can be the same between different coordinates the value in the hashmap should be a list.
# We pop elements from the heap k times and get the original coordinate using the mapping to the original points list.
# We append that value to the resulting array.