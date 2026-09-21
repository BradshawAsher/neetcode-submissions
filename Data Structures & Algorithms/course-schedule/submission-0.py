from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #prereq[i] = [a, b] means you have to take b before a
        #return true if we can do all courses, otherwise false

        #this is a graph problem?

        #there are numCourses courses you have to take, labeled 0 to numCourses-1

        #O(V+E) time and O(V+E) space, where V is # of courses(nodes) and E is the number of prereqs (edges)

        #isn't this just a cycle detection problem? Like if you can do it then there is no cycle and if you can't do it then there is a cycle?
        
        #prereq[i] = [course, prereq] -> edge goes from prereq -> course
        adj = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degree[course] += 1

        #Queue all courses with zero prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        completed = 0

        while queue:
            node = queue.popleft()
            completed += 1

            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        #If we completed all courses, no cycle existed
        return completed == numCourses
        

