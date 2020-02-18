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

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        hash = {}
        s = Stack()
        s.push(starting_vertex)
        path = ""
        while s.size() > 0:
            current_value = s.pop()

            #add to hash
            if str(current_value) not in hash:
                path += f"{current_value}, "
                hash[str(current_value)] = True

                #Add neighbors
                for neighbor in self.get_neighbors(current_value):
                    s.push(neighbor)
        print(path[:-2])

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
