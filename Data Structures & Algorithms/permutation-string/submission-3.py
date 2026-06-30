class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if s1 == s2:
            return True
        elif len(s1) > len(s2):
            return False


        s1_dict = {}

        for c in s1:
            if c not in s1_dict:
                s1_dict[c] = 1
            else:
                 s1_dict[c] += 1
        
        s2_dict = {}

        for c in s2:
            if c not in s2_dict:
                s2_dict[c] = 1
            else:
                 s2_dict[c] += 1
        
        check_dict = s1_dict

        left = 0
        cl = s2[left]

        while cl not in check_dict:
            left += 1
            if left == len(s2):
                return False
            cl = s2[left]
        check_dict[cl] -= 1
        if check_dict[cl] == 0:
            del check_dict[cl]
            if len(check_dict.keys()) == 0:
                return True
        
        right = left + 1

        while right < len(s2):
            cr = s2[right]
            if cr in check_dict:
                check_dict[cr] -= 1
                if check_dict[cr] == 0:
                    del check_dict[cr]
                if len(check_dict.keys()) == 0:
                    return True
            else:
                break
            right += 1
        
        if right < len(s2):    
            return self.checkInclusion(s1, s2[left+1:])
        else:
        

            return len(check_dict.keys()) == 0
        