class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        dists = []
        for p in points:
            dist = p[0]** 2 + p[1]** 2
            dists.append((p, dist))
        
        dists = sorted(dists, key= lambda x: x[1])
        return [d[0] for d in dists[:k]]