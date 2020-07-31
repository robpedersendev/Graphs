import random
from random import randint

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
        # Used as a unique ID
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

        # Add users

        # Create friendships
        for i in range(0, num_users):
            self.add_user(f"User {i + 1}")

        # Generate All Friendship combinations
        possible_friendships = []

        # Avoid dupes by makings ure first number is smaller than second
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # Shuffle all possible avg_friendships
        random.shuffle(possible_friendships)

        # Create for first x pairs. X is total //2
        # Creates a friendship from B to A and A to B
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):

        visited = {}  # Note that this is a dictionary, not a set
        # Create a Queue
        queue = Queue()
        # Add the user_id to the queue as a list
        queue.enqueue([user_id])

        # Loop through the queue
        while queue.size() > 0:
            # Set last item in list equal to path
            friends_list = queue.dequeue()
            # Set unique_id to the last item in friends_list
            unique_id = friends_list[-1]

            # Now we are going to check if the unique_id was visited
            if unique_id not in visited:
                # Add to the path
                visited[unique_id] = friends_list
                print(friends_list)
                # For each neighboor
                for neighbor in self.friendships[unique_id]:
                    # copy the path and enqueue
                    new_friends_list= friends_list.copy()
                    new_friends_list.append(neighbor)
                    print(friends_list)
                    friends_list.append(new_friends_list)


        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print("friendships")
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print("connections")
    print(connections)
