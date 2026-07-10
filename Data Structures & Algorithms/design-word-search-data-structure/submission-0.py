class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]

        node["*"] = True

    def search(self, word: str) -> bool:

        def dfs(node, i):
            if i == len(word):
                return "*" in node

            if word[i] != ".":
                if word[i] not in node:
                    return False
                return dfs(node[word[i]], i + 1)

            # Wildcard: try every child
            for c, child in node.items():
                if c == "*":
                    continue
                if dfs(child, i + 1):
                    return True

            return False

        return dfs(self.root, 0)