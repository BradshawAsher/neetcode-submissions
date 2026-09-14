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
        nodes = [self.root]
        for ch in word:
            next_nodes = []
            for node in nodes:
                if ch == ".":
                    next_nodes.extend(node.children.values())
                elif ch in node.children:
                    next_nodes.append(node.children[ch])
            
            if not next_nodes:
                return False
            
            nodes = next_nodes
        
        return any(node.is_end_of_word for node in nodes)