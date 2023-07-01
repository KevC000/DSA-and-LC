class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, str):
        curr = self.root
        
        for c in str:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]      
        curr.word = True
    
    def search(self, str):
        curr = self.root
        
        for c in str:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word
    
    def prefix(self, str):
        curr = self.root
        
        for c in str:
            if c not in curr.children[c]:
                return False
            curr = curr.children[c]
        return True