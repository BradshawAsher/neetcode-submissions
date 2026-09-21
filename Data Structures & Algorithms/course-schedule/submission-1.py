from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for course, prereq in prerequisites:
            adj[course].append(prereq)

        #0 = unvisited, 1 = visiting (in recursion stack), 2 = completely visited
        state = [0] * numCourses

        def has_cycle(node: int) -> bool:
            if state[node] == 1:
                return True #Found a back-edge (cycle)
            
            if state[node] == 2:
                return False #Already verified safe

            state[node] = 1 #Mark as currently visiting
            for neighbor in adj[node]:
                if has_cycle(neighbor):
                    return True
                

            state[node] = 2 #Done exploring, safe
            return False

        #Run DFS from every node to cover disconnected graphs components
        for course in range(numCourses):
            if state[course] == 0:
                if has_cycle(course):
                    return False

        return True
        

