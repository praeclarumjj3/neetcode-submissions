from typing import List
from collections import deque

class Solution:
    def canFinish(
        self,
        numCourses: int,
        prerequisites: List[List[int]]
    ) -> bool:

        graph = {course: [] for course in range(numCourses)}
        indegree = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        queue = deque()

        # Courses with no prerequisites can be taken immediately
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        courses_taken = 0

        while queue:
            course = queue.popleft()
            courses_taken += 1

            for next_course in graph[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)

        return courses_taken == numCourses