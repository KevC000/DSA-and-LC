#Unique Number of Occurrences
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        occurences = [n for n in freq.values()]
        print(occurences)

        visited = set()
        for n in occurences:
            if n in visited:
                return False
            visited.add(n)
        return True

# Time: O(N) Space: O(N)
# We create a frequency dictionary of the array.
# We create a list of the values of the frequency dictionary.
# We create a set to keep track of the visited values.
# We iterate through the list of values.