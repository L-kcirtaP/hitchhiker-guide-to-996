class Trie:
    class TrieNode:
        def __init__(self, val, isWord=False):
            self.val = val
            self.isWord = isWord
            self.children = []
    root = None

    def __init__(self):
        """
        Initialize your data structure here.
        """
        return
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """

        return
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """

        return
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """

        return
        


word = 'hello'
prefix = 'hell'
# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert(word)
param_2 = obj.search(word)
param_3 = obj.startsWith(prefix)