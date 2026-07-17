class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)

        strings = []
        string = ""

        for i in range(len(s)):
            string += s[i]
            count[s[i]] -= 1

            if all([count[st] == 0 for st in string]):
                strings.append(string)
                string = ""
        
        return [len(st) for st in strings]
            

        