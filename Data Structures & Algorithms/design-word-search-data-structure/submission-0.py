class TrieNode:
    def __init__(self):
        #Maps character -> TrieNode
        self.children = {}

        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                #make a child
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end_of_word = True
        
    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, idx: int) -> bool:
            #Base case: reached the end of the word
            if idx == len(word):
                return node.is_end_of_word
            
            ch = word[idx]

            #wildcard: explore all existing child branches
            if ch == ".":
                for child_node in node.children.values():
                    if dfs(child_node, idx + 1):
                        return True
                
                return False
            
            #exact character match
            if ch not in node.children:
                return False

            
            return dfs(node.children[ch], idx + 1)
        return dfs(self.root, 0)
