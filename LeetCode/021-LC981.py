#Time Based Key-Value Store


class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = '', self.map.get(key,[])
        l,r = 0, len(values)-1

        while l<=r:

            mid = (r+l)//2

            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l =  mid+1
            else:
                r = mid-1
        return res


# set: Time: O(1)
# get: Time: O(logN)
# We store the key as a key in hashmap, and the value/timestamp as a nested array as a pair.
# Set is just appending the new value if it exists along with the timestamp
# Get we find the greatest timestamp that is less than or equal to the given timestamp using binary search.
