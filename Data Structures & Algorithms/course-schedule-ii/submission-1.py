from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        #Edge: course -> prereq (meaning we must clear prereqs before finishing course)
        for course, prereq in prerequisites:
            adj[course].append(prereq)

        #0 = unvisited, 1 = visiting(in recursion stack), 2 = visited
        state = [0] * numCourses
        order = []

        def has_cycle(node: int) -> bool:
            if state[node] == 1:
                return True
            if state[node] == 2:
                return False

            state[node] = 1

            for neighbor in adj[node]:
                if has_cycle(neighbor):
                    return True
                
            state[node] = 2
            #All prerequisites for this course are fully explored, so we can record it!
            order.append(node)
            return False
        
        for course in range(numCourses):
            if state[course] == 0:
                if has_cycle(course):
                    return [] #Cycle found, impossible to finish

        return order
