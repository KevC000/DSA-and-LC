#Encode and Decode Strings

class Codec:
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
        
    def decode(self, s):
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res
    
# Time: Encode: O(N); Decode: O(N) 
# Space:  Encode: O(1); Decode: O(1) 

# We need to create  delitmiter for the strings, but that delimiter may occur in the string.
# So we use a number to indicate the length of the string an we can use it to slice the portion of the encoded string into the resultiong array when decoding.
# When we decode we we grab the portion before the delimiter as an int until we reach a # and using the int we use string slicing to grab the word, adn repeat.