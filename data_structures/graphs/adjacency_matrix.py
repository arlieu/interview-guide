class AdjacencyMatrix:
    def __init__(self, n):
        self.n = n
        self.matrix = [[0]*n for i in range(0, n)]

    def __validPos(self, start, end=0):
        if (start < 0) or (start > self.n-1) or (end < 0) or (end > self.n-1):
            print("Invalid position")
            return False

        return True

    def __edgePaths(self, start):
        res = []
        for j in range(0, self.n):
            if self.matrix[start][j] == 1:
                res.append(j)

        return res

    def addEdge(self, start, end):
        if self.__validPos(start, end) != True:
            return

        self.matrix[start][end] = 1

    def removeEdge(self, start, end):
        if self.__validPos(start, end) != True:
            return

        self.matrix[start][end] = 0

    def hasEdge(self, start, end):
        if self.__validPos(start, end) != True:
            return

        return self.matrix[start][end]

    def edgePaths(self, start):
        if self.__validPos(start) != True:
            return

        paths = self.__edgePaths(start)
        if len(paths) == 0:
            print(str(start) + ": [ ]")

        else:
            print(str(start) + ": [", end = "")
            print(str(paths[0]), end = "")
            for i in paths[1:]:
                print(", " + str(i), end = "")
            print("]")

    def __len__(self):
        return self.n

    def __str__(self):
        # printing only formatted correctly for matrices of n < 11
        res = ""
        for row in range(0, len(self.matrix)):
            if row == 0:
                res += "    "
                for i in range(0, self.n):
                    res += " " + str(i)

                dashes = "    " + "-" * self.n * 2 + "-"
                res += "\n" + dashes + "\n"

            res += str(row) + "| "
            res += "[ " + str(self.matrix[row][0]) + " "
            for col in range(1, len(self.matrix[row])):
                res += str(self.matrix[row][col]) + " "

            res += "]\n"

        return res


if __name__ == "__main__":
    x = AdjacencyMatrix(6)
    x.addEdge(3, 2)
    x.addEdge(4, 1)
    x.addEdge(7, 2)
    print(x)
