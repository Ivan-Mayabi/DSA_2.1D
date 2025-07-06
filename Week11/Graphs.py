class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = dict()

    def __repr__(self):
        str_graph = ""

        for key, values in self.adj_list.items():
            str_graph += f"{key} -> {values}"

        return str_graph

    def breadth_first_search(self):
        visited = set()

    def depth_first_search(self):
        pass

    def add_node(self, node):
        if node not in self.adj_list.keys():
            self.adj_list[node] = set()
        else:
            raise ValueError("Node Exists!!")

    def add_edge(self, source_node, destination_node, weighted = None):
        if source_node not in self.adj_list.keys():
            self.add_node(source_node)

        if destination_node not in self.adj_list.keys():
            self.add_node(destination_node)

        if weighted is None:
            self.adj_list[source_node].add(destination_node)

            #*(This is bi-directional by default
            if self.directed:
                self.adj_list[destination_node].add(source_node)
            #if it is not directed, then you are done, you don't need to repeat anything

        else:
            self.adj_list[source_node].add((destination_node,weighted))

            if self.directed:
                self.adj_list[destination_node].add((source_node,weighted))

    def obtain_neighbours(self,key_node):
        return self.adj_list.get(key_node,set())

    def adj_matrix(self):
        pass

    def bfs(self, start):
        """"We use QUEUES(fifo) IN BFS,  AND STACK(lifo) FOR DFS, as helping data structures"""""

    visited = set()  # set of visited nodes
    #    queue = [start] #nodes to be processed, so have a starting node
    #    order = [] #Our result in order, which is traversal order
    #    while queue:
    # while we still have elements to process,
    # """"get the elements to process in fifo way"""
    # node = queue.pop(0) #first element added        #
    # print(f"Exploring room: {node}, Path so far: {path}")
    # if node == goal:        #     print("\n🎯 Theseus found the Minotaur!")
    #     return path
    #     if node not in visited: #if node is not visited
    #     visited.add(node) #first add it to the visited nodes
    #     order.append(node) #append it to our resulting list
    #     #Then get all the neighbours of this node, use our available function
    #     neighbours = self.get_neighbours(node)
    # then iterate through them
    # for neighbour in neighbours:
    # #means we have a weighted connection not just individual value
    # if isinstance(neighbour, tuple):
    # neighbour = neighbour[0]
    # #just take the value and leave the weight,
    # Sometimes neighbors might come as (value, weight), so we only take the value
    # if neighbour is not visited, append it to queue
    # if neighbour not in visited:
    # queue.append(neighbour)
    # return orderdef dfs(self, start):
    # """"We use STACK(lifo) FOR DFS, as helping data structures"""""
    # visited = set()  # set of visited nodes
    # stack = [start]  # nodes to be processed, so have a starting node
    # order = []  # Our result in order, which is traversal order
    # while stack:
    # while we still have elements to process,
    # """"get the elements to process in fifo way"""
    # node = stack.pop()  # first element added
    # if node not in visited:
    # if node is not visited
    # visited.add(node)  # first add it to the visited nodes
    # order.append(node)  # append it to our resulting list
    # Then get all the neighbours of this node, use our available function
    # neighbours = self.get_neighbours(node)
    # then iterate through them
    # for neighbour in sorted(neighbours, reverse=True):
    # means we have a weighted connection not just individual value
    # if isinstance(neighbour, tuple):
    # neighbour = neighbour[0]  # just take the value and leave the weight
    # if neighbour is not visited, append it to queue
    # if neighbour not in visited:                    s
    # tack.append(neighbour)
    # return order

if __name__=="__main__":
    graph_obj = Graph()

    print(graph_obj)