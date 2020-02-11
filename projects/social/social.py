import random
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
class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        
        #Average number of friends to add
        total_friends = avg_friendships * num_users

        #Add users
        for user_id in range(1, num_users+1):
            self.add_user(user_id)

        #make friends ship pairs
        friendship_pairs = []
        for i in range(1,num_users+1):
            for j in range(i+1, num_users+1):
                friendship_pairs.append((i,j))

        random.shuffle(friendship_pairs)
        #we need 10 pairs, ie 20 relationships
        count = 10
        for friendship_pair in friendship_pairs:
            if count == 0:
                break
            if len(self.friendships[friendship_pair[0]]) < 4 and len(self.friendships[friendship_pair[1]]) < 4:
                self.add_friendship(friendship_pair[0], friendship_pair[1])
                count -= 1

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        neighbors = []
        if vertex_id in self.friendships:
            for node in self.friendships[vertex_id]:
                neighbors.append(node)
            return neighbors
        else:
            return []

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
            if current_value not in hash:
                hash[current_value] = True

                #Add neighbors
                for neighbor in self.get_neighbors(current_value):
                    q.enqueue({"value": neighbor, "previous_items": current_previous_items + [current_value]})

        return []

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.

        {1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {8, 1, 2}, 6: {10}, 7: {2}, 8: {1, 5}, 9: {4}, 10: {1, 2, 6}}

        {1: [1], 8: [1, 8], 10: [1, 10], 5: [1, 5], 2: [1, 10, 2], 6: [1, 10, 6], 7: [1, 10, 2, 7]}
        """
        social_paths = {}

        for num in range(1, len(self.users)+1):
            if len(self.bfs(user_id, num)) > 0:
                social_paths[num] = self.bfs(user_id, num)
        return social_paths

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
