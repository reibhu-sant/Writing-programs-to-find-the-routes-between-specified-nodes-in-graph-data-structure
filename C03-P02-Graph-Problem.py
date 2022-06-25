import csv


class System:
    steps = [
        [-1, 0],  # Top Step
        [0, 1],  # Right Step
        [1, 0],  # Bottom Step
        [0, -1]  # Left Step
    ]

    def __init__(self):
        self.star_city = list()
        self.star_city_rows = 0
        self.star_city_cols = 0

    def config_system(self, file):
        data_file = open(file, 'r')
        reader = csv.reader(data_file)
        self.star_city = list()
        for row in reader:
            self.star_city.append(row)
        self.star_city_rows = len(self.star_city)
        self.star_city_cols = len(self.star_city[0])

    def check_limits(self, row_num, col_num):
        if 0 <= row_num < self.star_city_rows and 0 <= col_num < self.star_city_cols:
            return True
        return False

    def get_neighbours(self, row, col):
        neighbours = []
        # loop through top, right, bottom and left adjacent nodes to get the neighbor
        # only if the altitude of adjacent node is lower or equal to the current node 
        # and is not already present in neighbors list
        for i in System.steps:
            if self.check_limits(row + i[0], col + i[1]):
                if self.star_city[row + i[0]][col + i[1]] <= self.star_city[row][col] and (
                        row + i[0], col + i[1]) not in neighbours:
                    neighbours.append((row + i[0], col + i[1]))
        return neighbours

    def find_route(self, source, destination):

        if source == destination:
            return True

            # Mark all the vertices as not visited
        visited = [[False] * (len(self.star_city) + 1)] * (len(self.star_city) + 1)

        # Create a queue for BFS
        queue = [source]
        path = []
        # Mark the current node as visited and
        # enqueue it
        visited[source[0]][source[1]] = True
        while queue:

            # Dequeue a vertex from queue
            s = queue.pop(0)
            path.append(s)

            neighbours = self.get_neighbours(s[0], s[1])

            for i in neighbours:
                if i == destination:
                    return path
                if not visited[i[0]][i[1]]:
                    queue.append(i)
                    visited[i[0]][i[1]] = True

    def Bluevalley_to_Smallville_route(self):
        global i
        r = self.star_city_rows
        c = self.star_city_cols - 1
        for i in range(r):
            source = (i, 0)
            for j in range(r):
                destination = (j, c)
                path = [self.find_route(source, destination)]
                if path[0] is not None:
                    route = path
                    break
        # source = (3,0)
        # destination = (3,4)
        # paths.append(self.find_route(source, destination))
        print(f"\n\nTo reach city Smallville from city Blue Valley the nodes traversed are-")
        k = 0
        for node in route:
            for i in node:
                if k != len(node)-1:
                    print(f"{i} ---->", end=" ")
                    k = k+1
                else:
                    print(f"{i} ", end=" ")
        return True


if __name__ == "__main__":
    test_system1 = System()

    # Getting data in 2D matrix
    test_system1.config_system('city_data.csv')

    # Finding path between Source node to Destination node
    route = test_system1.find_route((3, 0), (4, 2))
    print(f"\n\nTo reach Node (4,2) from Node (3,0) the nodes traversed are-")
    for node in route:
        print(f"({node[0]},{node[1]}) ---->", end=" ")
    print((4, 2))

    # Finding path between Bluevalley to Smallville
    test_system1.Bluevalley_to_Smallville_route()
