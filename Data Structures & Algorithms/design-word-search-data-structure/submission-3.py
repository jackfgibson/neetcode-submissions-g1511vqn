class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.end = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            node = root
            for i in range(j, len(word)):
                if word[i] == ".":
                    for child in node.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                if word[i] in node.children:
                    node = node.children[word[i]]
                else:
                    return False
            return node.end
        return dfs(0, self.root)