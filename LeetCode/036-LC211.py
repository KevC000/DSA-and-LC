# Design Add and Search Words Data Structure
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        def dfs(x, root):
            curr = root
            for i in range(x, len(word)):
                c = word[i]
                if c == '.':
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.word
        return dfs(0, self.root)
        
# Search is O(N) Time and space, everything else is O(1) Time and Space.
# Everything else is the same as a regular trie except for search because we can have '.' as a place holder.
# If we have '.' as a place holder we search the children if it contaains the remainder of the letters.
# For this we designa recusive function to search for the letters after '.'.