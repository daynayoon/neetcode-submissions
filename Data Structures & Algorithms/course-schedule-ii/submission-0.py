class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # bfs: take no prerequisite first and take the course that has taken course as prerequisite
        prerequisite = [[] for i in range(numCourses)] # the list of courses that has pre as prerequisite
        indegree = [0] * numCourses # the number of prerequisites that crs has

        for crs, pre in prerequisites:
            prerequisite[pre].append(crs)
            indegree[crs] += 1

        # put all no prerequisite courses to the queue
        q = deque(i for i in range(numCourses) if indegree[i] == 0)
        res = []

        while q:
            crs = q.popleft()
            res.append(crs)
            for nxt in prerequisite[crs]:
                indegree[nxt] -= 1 
                if indegree[nxt] == 0: # took all the prerequisite
                    q.append(nxt)

        return res if len(res) == numCourses else []
