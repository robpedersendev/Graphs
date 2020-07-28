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
    # Recursive Depth first solution

    # Build our graph through initialization
    graph = Graph()

    for pair in ancestors:
        # Parent vertex
        graph.add_vertex(pair[0])
        # Child Vertex
        graph.add_vertex(pair[1])

        # Link kids to their parents, pointing upstream
        graph.add_edge(pair[1], pair[0])

    # Create a queue
    queue = Queue()
    # Store path as a queue
    queue.enqueue([starting_node])

    # Set longest path
    max_path_length = 1
    # Per spec, return -1 if there is no parents
    earliest_ancestor = -1

    while queue.size() > 0:
        path = queue.dequeue()
        vertex = path[-1]
        # If there is a tie, take the path with the lowest numerical id
        if (len(path) >= max_path_length and vertex < earliest_ancestor) or (len(path) > max_path_length):
            earliest_ancestor = vertex
            max_path_length = len(path)

        for neighbor in graph.vertices[vertex]:
            path_copy = list(path)
            path_copy.append(neighbor)
            queue.enqueue(path_copy)

    return earliest_ancestor

