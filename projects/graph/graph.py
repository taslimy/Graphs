"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue
        q = Queue()
        # Create list of visited nodes
        visited = set()
        # Put starting node in the queue
        q.enqueue(starting_vertex)
        # While: queue not empty
        while q.size() > 0:
            # Pop first node out of queue
            vertex = q.dequeue()
            # If not visited
            if vertex not in visited:
                visited.add(vertex)
                print("breadth-first:",vertex)
        #     Mark as visited
        #     Get adjacent edges and add to back of queue
                for next_vert in self.vertices[vertex]:
                    q.enqueue(next_vert)
        #     Go to top of loop

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a queue
        stack = Stack()
        # Create a list of visted nodes
        visited = set()
        # put a starting node in the queue
        stack.push(starting_vertex)
        # While: queue not empty
        while stack.size() > 0:
            # pop first node out of queue
            vertex = stack.pop()
            # if not visited
            if vertex not in visited:
                visited.add(vertex)
                print("depth-first:", vertex)
                # mark as visited
                # get adjacent edges and add to list
                for next_vert in self.vertices[vertex]:
                    stack.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # Check if its visited
        if visited is None:
            visited = set()
        # if node hasn't been visited:
        if starting_vertex not in visited:
            # check if the node is visited
            visited.add(starting_vertex)
            print(f"DFT RECURSIVE: {starting_vertex}")
            # loop over it for each child
            for child_vert in self.vertices[starting_vertex]:
                self.dft_recursive(child_vert, visited)
        return visited

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty Q and ENQ to the starting vertex
        qq = Queue()
        qq.enqueue([starting_vertex])
        # Create empty set to store visted nodes
        visited = set()
        # while Q is not empty:
        while qq.size() > 0:
            # DQ the first one
            path = qq.dequeue()
            # get the last vertex
            vertex = path[-1]
            # if vertex is equal destination
            if vertex is destination_vertex:
                #return path
                return path
            # if the vertex has not been visited
            if vertex not in visited:
                # mark it visted
                visited.add(vertex)
                #print('BFS:', vertex)
                # add the adjacents to all of them
                for next_vert in self.vertices[vertex]:
                    # make a copy of path
                    copy_path = list(path)
                    # Append adjacents to the back of it
                    copy_path.append(next_vert)
                    # ENQ copy_path
                    qq.enqueue(copy_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty Q and ENQ to the starting vertex
        stack = Stack()
        stack.push([starting_vertex])
        # Empty set to store the visited nodes
        visited = set()
        # while Q is not empty:
        while stack.size() > 0:
            # DQ the first one
            path = stack.pop()
            # get the last vertex
            vertex = path[-1]
            # if vertex is equal destination_vertex
            if vertex is destination_vertex:
                #return path
                return path
            # if the vertex has not been visited
            if vertex not in visited:
                # mark it visted
                visited.add(vertex)
                # print('DFS:', vertex)
                # add the adjacents to all of them
                for next_vert in self.vertices[vertex]:
                    # make a copy of path
                    copy_path = list(path)
                    # Append adjacents to the back of it
                    copy_path.append(next_vert)
                    # ENQ copy_path
                    stack.push(copy_path)



if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("BFS:", graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("DFS", graph.dfs(1, 6))
