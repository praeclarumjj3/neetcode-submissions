class PrefixTree:

    def __init__(self):
        self.graph = {}
        

    def insert(self, word: str) -> None:
        
        idx = 1
        while idx <= len(word):
            w = word[0:idx]
            if w not in self.graph:
                self.graph[w] = [word]
            elif word not in self.graph[w]:
                self.graph[w].append(word)
            idx += 1


    def search(self, word: str) -> bool:
        return word in self.graph and word in self.graph[word]
        

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.graph
        
        