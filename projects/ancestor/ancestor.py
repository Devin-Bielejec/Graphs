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

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if str(vertex_id) not in self.vertices:
            self.vertices[f"{vertex_id}"] = set()
        else:
            print("Vertex already in there!")

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if str(v1) not in self.vertices:
            print("Vertex does not exist")
        else:
            self.vertices[str(v1)].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        neighbors = []
        if str(vertex_id) in self.vertices:
            for node in self.vertices[str(vertex_id)]:
                neighbors.append(node)
            return neighbors
        else:
            return []

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        hash = {}
        q = Queue()
        q.enqueue(starting_vertex)
        path = ""
        while q.size() > 0:
            current_value = q.dequeue()

            #add to hash
            if str(current_value) not in hash:
                path += f"{current_value}, "
                hash[str(current_value)] = True

                #Add neighbors
                for neighbor in self.get_neighbors(current_value):
                    q.enqueue(neighbor)
        print(path[:-2])

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push({"value": starting_vertex, "depth": 0})
        max_depth = 1
        max_depth_item = float("Infinity")
        while s.size() > 0:
            current = s.pop()

            if current["depth"] > max_depth:
                max_depth = current["depth"]
                max_depth_item = current["value"]
            elif current["depth"] == max_depth and current["value"] < max_depth_item:
                max_depth_item = current["value"]
            
            #Add neighbors
            for neighbor in self.get_neighbors(current["value"]):
                s.push({"value": neighbor, "depth": current["depth"] + 1})

        return max_depth_item
    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        hash = {}
        path = ""
        def helper(self, current_vertex):
            nonlocal path
            hash[f"{current_vertex}"] = True
            path += f"{current_vertex}, "
            #for both cases, find neighbors
            #Find all unvisited neighbors
            unvisited_neighbors = [neighbor for neighbor in self.get_neighbors(current_vertex) if str(neighbor) not in hash]
            
            #Base Case - no unvisited neighbors
            if len(unvisited_neighbors) == 0:
                return
            else:
                #loop through unvisited neighbors and call helper
                for uvn in unvisited_neighbors:
                    helper(self, uvn)
            
        helper(self, starting_vertex)
        print(path[:-2])
        
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        hash = {}
        q = Queue()
        q.enqueue({"value": starting_vertex, "previous_items": []})
        while q.size() > 0:
            current_item = q.dequeue()
            current_value = current_item["value"]
            current_previous_items = current_item["previous_items"]
            
            #if current value is destination vertex, print out all previous items and current, then break
            if current_value == destination_vertex:
                return current_previous_items + [current_value]
            #add to hash
            if str(current_value) not in hash:
                hash[str(current_value)] = True

                #Add neighbors
                for neighbor in self.get_neighbors(current_value):
                    q.enqueue({"value": neighbor, "previous_items": current_previous_items + [current_value]})

        return []

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        hash = {}
        s = Stack()
        s.push({"value": starting_vertex, "previous_items": []})
        while s.size() > 0:
            current_item = s.pop()
            current_value = current_item["value"]
            current_previous_items = current_item["previous_items"]
            
            #if current value is destination vertex, print out all previous items and current, then break
            if current_value == destination_vertex:
                return current_previous_items + [current_value]
            #add to hash
            if str(current_value) not in hash:
                hash[str(current_value)] = True

                #Add neighbors
                for neighbor in self.get_neighbors(current_value):
                    s.push({"value": neighbor, "previous_items": current_previous_items + [current_value]})

        return []

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        hash = {}
        results = None
        def helper(self, current_vertex, destination_vertex):
            nonlocal results
            if current_vertex["value"] == destination_vertex:
                results = current_vertex["previous_items"] + [current_vertex["value"]]
            
            hash[f"{current_vertex['value']}"] = True

            #Find all unvisited neighbors
            unvisited_neighbors = [neighbor for neighbor in self.get_neighbors(current_vertex["value"]) if str(neighbor) not in hash]
            
            #Base Case - no unvisited neighbors
            if len(unvisited_neighbors) == 0:
                return
            else:
                #loop through unvisited neighbors and call helper
                for uvn in unvisited_neighbors:
                    helper(self, {'value': uvn, 'previous_items': current_vertex['previous_items'] + [current_vertex['value']]}, destination_vertex)
            
        helper(self, {"value": starting_vertex, "previous_items": []}, destination_vertex)
        return results


def earliest_ancestor(ancestors, starting_node):
    #Make graph
    g = Graph()

    #For each ancestor in acesctors, add the vertex then add the edge
    for parent, child in ancestors:
        #make edge go from child to parent, so we can do searches later
        g.add_vertex(child)
        g.add_edge(child, parent)

    #Easiest case is starting_node doesn't have neighbords, return -1
    neighbors = g.get_neighbors(starting_node)
    print(neighbors)
    if len(neighbors) == 0:
        return -1
    else:
        return g.dft(starting_node)


