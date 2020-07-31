# Grab the queue from the util.py file
class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)

# Import our graph to use it in the earliest ancestor file.
class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
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


def earliest_ancestor(ancestors, starting_node):
    # Depth first solution

    # Build our graph through initialization
    graph = Graph()

    # Link children to the parents with a loop and add them as a connected edge to the graph
    for pair in ancestors:
        # Parent vertex
        graph.add_vertex(pair[0])
        # Child Vertex
        graph.add_vertex(pair[1])

        # Link kids to their parents, pointing upstream
        graph.add_edge(pair[1], pair[0])

    # Instantiate a few base/needed values to be used shortly

    # Create a queue
    queue = Queue()
    # Store path as a list, within the queue
    queue.enqueue([starting_node])

    # Set longest path
    max_path_length = 1
    # Per spec, return -1 if there is no parents
    earliest_ancestor = -1

    # Loop through the entire queue as long as there is at least something in the starting_node value
    while queue.size() > 0:
        # Set path equal to dequeue'ing from the queue
        path = queue.dequeue()
        # print(path, "path")
        # Set vertex to be the last item in the list of path
        vertex = path[-1]
        # print(vertex, "vertex")
        # If there is a tie, take the PATH with the lowest numerical id per the spec
        if (len(path) >= max_path_length and vertex < earliest_ancestor) or (len(path) > max_path_length):
            # Reassign the earliest ancestor to be the value of vertex
            earliest_ancestor = vertex
            # Reassign the earliest ancestor to be the value of length of path
            max_path_length = len(path)

        # After checking the above
        # Grab the vertex at the index of the vertex
        for neighbor in graph.vertices[vertex]:
            # Create a copy of the path as a list
            path_copy = list(path)
            # Add to the copy of the path with neighbor, otherwise known as the vertex
            path_copy.append(neighbor)
            # Add this copy of the path to the queue
            queue.enqueue(path_copy)

    # Return the earliest ancestor
    return earliest_ancestor

