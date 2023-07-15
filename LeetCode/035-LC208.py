# Implement Trie (Prefix Tree)

class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True



# Time: O(1) 
# Create a TrieNode
# Init: Start with empty trie node since we have now words yet.
# Insert: Iterate through each letter if it does not exist in the children add it. Always continue to the next letter.
# Search: Iterate through each letter and check if it exists. At the end check if that node's word property is true.
# StartsWith: Same as Search except we return True at the end instead of checking curr.word.