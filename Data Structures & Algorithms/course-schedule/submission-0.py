class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # if there is cycle, return false -> dfs
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set() # course on curren DFS

        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []: # already verified or no prerequisite
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

        # I used seen and got wrong -> what I caught: have I visited this node?
        # what visiting does: is this node on the track for current dfs run?

        # e.g., B 경로로 D를 방문한 뒤 C 경로로 D에 다시 와도 사이클이 아님
        # A → B → D
        # A → C → D