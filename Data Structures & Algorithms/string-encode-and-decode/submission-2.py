class Solution:

    def encode(self, strs: List[str]) -> str:
        
        # if not hasattr(self, vocab):
        #     self.vocab = {}
        
        string = ""
        if len(strs) == 0:
            return ""
        for st in strs:
            # if st not in self.vocab:
            #     self.vocab[len(self.vocab)] = st
            # idx = self.vocab.index(st)
            string = string + "|"*200 + st
        
        return string

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        strings = s.split("|"*200)
        return strings[1:]

