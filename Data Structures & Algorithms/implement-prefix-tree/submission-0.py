class Node:
    def __init__(self, end):
        self.children = {}
        self.end = end

class PrefixTree:

    def __init__(self):
        #create tree root node
        self.root = Node(False)

    def insert(self, word: str) -> None:
        # check to see how much of the word (up to how many characters of the start) exist
        # insert remaining chars
        node = self.root
        for i in range(len(word)):
            if node.children.get(word[i]):
                if i == len(word)-1:
                    if node.children[word[i]].end == True:
                        return
                    else:
                        node.children[word[i]].end = True
                node = node.children[word[i]]
            else:
                if i == len(word)-1:
                    node.children[word[i]] = Node(True)
                else:
                    node.children[word[i]] = Node(False)
                    node = node.children[word[i]]



    def search(self, word: str) -> bool:
        # if all subsequent chars of a word are children of the previous char
        # final char must have node.end==True
        node = self.root
        for i in range(len(word)):
            if node.children.get(word[i]):
                if i == len(word)-1 and node.children[word[i]].end == True:
                    return True
                node = node.children[word[i]]
        return False

    def startsWith(self, prefix: str) -> bool:
        # see if sequence of chars that makes up prefix exists in tree
        # dont need to pay attention if final char is node.end==True
        node = self.root
        for i in range(len(prefix)):
            if node.children.get(prefix[i]):
                node = node.children[prefix[i]]
            else:
                return False
        return True
        