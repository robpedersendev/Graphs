"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            # print("Error: Vertex does not exist")
            raise ValueError("Error: Vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            # print("Error: Vertex does not exist")
            raise ValueError("Error: Vertex does not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        # Create a queue
        q = Queue()
        # Enqueue the starting vertex
        q.enqueue(starting_vertex)
        # Create a set store visited vertices
        visited = set()
        # While the queue is not empty
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # Check if visited
            # If not visited
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Enqueue all of its  neighbors
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        # Create a stack
        s = Stack()
        # Enqueue the starting vertex
        s.push(starting_vertex)
        # Create a set store visited vertices
        visited = set()
        # While the stack is not empty
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # Check if visited
            if v not in visited:
                # If not visited
                visited.add(v)
                print(v)
                # Mark it as visited
                for next_vertex in self.get_neighbors(v):
                    # Push all of its  neighbors on to the stack
                    s.push(next_vertex)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Check if the node has been visited
        if visited is None:
            # If not, create a set as visited
            visited = set()
        # Add the starting vertex to visited set
        visited.add(starting_vertex)
        # print it
        print(starting_vertex)
        # Loop through the vertices of starting_index
        for child_vert in self.vertices[starting_vertex]:
            # If the child vert is not in visited
            if child_vert not in visited:
                # Run this again
                # If not
                # Call dft_recursive with the child vertices and visited
                self.dft_recursive(child_vert, visited)

        # Mark it as visited


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue
        queue = Queue()
        # Enqueue the starting vertex
        # Add a list as a PATH
        queue.enqueue([starting_vertex])
        # Create a set store visited vertices
        visited = set()
        # While the queue is not empty
        while queue.size() > 0:
            # Pop the first vertex
            path = queue.dequeue()
            vertex = path[-1]
            # Check if visited
            if vertex not in visited:
                # If not visited
                if vertex == destination_vertex:
                    # Return path
                    return path
                # Mark it as visited
                visited.add(vertex)
                for next_vertex in self.get_neighbors(vertex):
                    # Push all of its  neighbors on to the stack by copying data, not a reference of it
                    new_path = list(path)
                    new_path.append(next_vertex)
                    queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a stack
        stack = Stack()
        # Enqueue the starting vertex
        # Add a list as a PATH
        stack.push([starting_vertex])
        # Create a set store visited vertices
        visited = set()
        # While the stack is not empty
        while stack.size() > 0:
            # Pop the first vertex
            path = stack.pop()
            vertex = path[-1]
            # Check if visited
            if vertex not in visited:
                # If not visited
                if vertex == destination_vertex:
                    # Return path
                    return path
                # Mark it as visited
                visited.add(vertex)
                for next_vertex in self.get_neighbors(vertex):
                    # Push all of its  neighbors on to the stack by copying data, not a reference of it
                    new_path =list(path)
                    new_path.append(next_vertex)
                    stack.push(new_path)

    def dfs_recursive(self, starting_vertex, target_value, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Check if the node has been visited
        if visited is None:
            # If not, create a set as visited
            visited = set()
        if path is None:
            path = []

        # Add the starting vertex to visited set
        visited.add(starting_vertex)
        path = path+[starting_vertex]
        if starting_vertex == target_value:
            return path
        # Loop through the vertices of starting_index
        for child_vert in self.vertices[starting_vertex]:
            # If the child vert is not in visited
            if child_vert not in visited:
                new_path=self.dfs_recursive(child_vert, target_value,visited,path)
                if new_path:
                    return new_path

        return None



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
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
