class Trie:

    class TrieNode:
        def __init__(self, val, isWord=False):
            self.val = val
            self.isWord = isWord
            self.children = []

    def __init__(self):
        self.root = self.TrieNode('')
        

    def _constructWordTree(self, word: str) -> TrieNode:
        if not word:
            return None

        root = self.TrieNode(word[0])
        next_node = self._constructWordTree(word[1:])
        if not next_node:
            root.isWord = True
        else:
            root.children.append(next_node)
        return root


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if not word:
            return

        root = self.root
        for i in range(len(word)):
            flg = False
            for child in root.children:
                if word[i] == child.val:
                    root = child
                    flg = True
                    if i == len(word) - 1:
                        root.isWord = True
            if not flg:
                break

        root.children.append(self._constructWordTree(word[i:]))


    def _searchTree(self, root: TrieNode, word: str) -> bool:
        if not word:
            return root.isWord

        for child in root.children:
            if word[0] == child.val:
                root = child
                return self._searchTree(root, word[1:])

        return False

   
    def search(self, word: str) -> bool:
        return self._searchTree(self.root, word)
        

    def _startsWith(self, root: TrieNode, word: str) -> bool:
        if not word:
            return True

        for child in root.children:
            if word[0] == child.val:
                root = child
                return self._startsWith(root, word[1:])

        return False


    def startsWith(self, prefix: str) -> bool:
        return self._startsWith(self.root, prefix)
        


word = 'hello'
prefix = 'hel'
# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert(word)
param_2 = obj.search(word)
print(param_2)
param_3 = obj.startsWith(prefix)
print(param_3)
obj.insert('haha')
