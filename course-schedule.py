# Time O(V+E)
# Space O(V+E)
from queue import Queue
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        independent_map = {} # Which courses are dependent on this course
        course_dependency_count = [0] * numCourses # How many prerequites need to be completed for this course
        q = Queue()
        for course_a, course_b in prerequisites:
            if course_b in independent_map:
                independent_map[course_b].append(course_a)
            else:
                independent_map[course_b] = [course_a]
            course_dependency_count[course_a] += 1

        for i in range(numCourses):
            if course_dependency_count[i] == 0:
                q.put(i)
        count = 0
        while not q.empty():
            course = q.get()
            count += 1
            if course in independent_map:
                for dependent_course in independent_map[course]:
                    course_dependency_count[dependent_course] -= 1
                    if course_dependency_count[dependent_course] == 0:
                        q.put(dependent_course)
        return True if count == numCourses else False

