class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = {course: [] for course in range(numCourses)}
        reqd = [0] * numCourses

        for p in prerequisites:
            graph[p[0]].append(p[1])
            reqd[p[0]] += 1
        

        can_take = []
        taken = []

        for idx in range(len(reqd)):
            if reqd[idx] == 0:
                can_take.append(idx)
        
        while len(can_take):
            c = can_take.pop()
            taken.append(c)

            for k in graph:
                if reqd[k] == 0:
                    continue
                if c in graph[k]:
                    reqd[k] -= 1
                if reqd[k] == 0 and k not in taken:
                    can_take.append(k)
        
        if len(taken) == numCourses:
            return taken
        else:
            return []

