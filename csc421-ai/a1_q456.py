import random
import heapq
import math
import matplotlib.pyplot as plt
import sys
from collections import defaultdict, deque, Counter
from itertools import combinations
import numpy as np 

# initialize random number generator for consistency 
rng = np.random.default_rng(seed=3)

class Problem(object):
    """The abstract class for a formal problem. A new domain subclasses this,
    overriding `actions` and `results`, and perhaps other methods.
    The default heuristic is 0 and the default action cost is 1 for all states.
    When yiou create an instance of a subclass, specify `initial`, and `goal` states 
    (or give an `is_goal` method) and perhaps other keyword args for the subclass."""

    def __init__(self, initial=None, goal=None, **kwds): 
        self.__dict__.update(initial=initial, goal=goal, **kwds) 
        
    def actions(self, state):        raise NotImplementedError
    def result(self, state, action): raise NotImplementedError
    def is_goal(self, state):        return state == self.goal
    def action_cost(self, s, a, s1): return 1
    def h(self, node):               return 0
    
    def __str__(self):
        return '{}({!r}, {!r})'.format(
            type(self).__name__, self.initial, self.goal)

class Node:
    "A Node in a search tree."
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.__dict__.update(state=state, parent=parent, action=action, path_cost=path_cost)

    def __repr__(self): return '<{}>'.format(self.state)
    def __len__(self): return 0 if self.parent is None else (1 + len(self.parent))
    def __lt__(self, other): return self.path_cost < other.path_cost
    
failure = Node('failure', path_cost=math.inf) # Indicates an algorithm couldn't find a solution.
cutoff  = Node('cutoff',  path_cost=math.inf) # Indicates iterative deepening search was cut off.
       
def expand(problem, node):
    "Expand a node, generating the children nodes."
    s = node.state
    for action in problem.actions(s):
        s1 = problem.result(s, action)
        cost = node.path_cost + problem.action_cost(s, action, s1)
        yield Node(s1, node, action, cost)
        
def path_actions(node):
    "The sequence of actions to get to this node."
    if node.parent is None:
        return []  
    return path_actions(node.parent) + [node.action]

def path_states(node):
    "The sequence of states to get to this node."
    if node in (cutoff, failure, None): 
        return []
    return path_states(node.parent) + [node.state]


# PriorityQueue - note 
# there is a small difference from the 
# book implementation in order to ensure 
# sorting stability 

class PriorityQueue:
    """A queue in which the item with minimum f(item) is always popped first."""

    def __init__(self, items=(), key=lambda x: x): 
        self.key = key
        self.items = [] # a heap of (score, item) pairs
        self.item_count = 0 
        for item in items:
            self.add(item)
         
    def add(self, item):
        """Add item to the queuez."""
        pair = ((self.key(item),self.item_count), item)
        heapq.heappush(self.items, pair)
        self.item_count+=1  

    def pop(self):
        """Pop and return the item with min f(item) value."""
        return heapq.heappop(self.items)[1]
    
    def top(self): return self.items[0][1]

    def get_items(self): 
        return self.items.copy() 

    def __len__(self): return len(self.items)


# Different search algorithms 
# defined by appropriate definition of priorities 


def best_first_search(problem, f):
    "Search nodes with minimum f(node) value first."
    node = Node(problem.initial)
    frontier = PriorityQueue([node], key=f)
    reached = {problem.initial: node}
    frontiers = [] 
    while frontier:
        node = frontier.pop()
        
        if problem.is_goal(node.state):
            return (node,reached,frontiers)
        for child in expand(problem, node):
            s = child.state
            if s not in reached or child.path_cost < reached[s].path_cost:
                reached[s] = child
                frontier.add(child)
        
    return (failure, reached, frontiers)

def g(n): return n.path_cost

def astar_search(problem, h=None):
    """Search nodes with minimum f(n) = g(n) + h(n)."""
    h = h or problem.h
    return best_first_search(problem, f=lambda n: g(n) + h(n))
        
def greedy_bfs(problem, h=None):
    """Search nodes with minimum h(n)."""
    h = h or problem.h
    return best_first_search(problem, f=h)

def uniform_cost_search(problem):
    "Search nodes with minimum path cost first."
    return best_first_search(problem, f=g)

def breadth_first_bfs(problem):
    "Search shallowest nodes in the search tree first; using best-first."
    return best_first_search(problem, f=len)
    


class Map:
    """A map of places in a 2D world: a graph with vertexes and links between them. 
    In `Map(links, locations)`, `links` can be either [(v1, v2)...] pairs, 
    or a {(v1, v2): distance...} dict. Optional `locations` can be {v1: (x, y)} 
    If `directed=False` then for every (v1, v2) link, we add a (v2, v1) link."""

    def __init__(self, links, locations=None, directed=False):
        if not hasattr(links, 'items'): # Distances are 1 by default
            links = {link: 1 for link in links}
        if not directed:
            for (v1, v2) in list(links):
                links[v2, v1] = links[v1, v2]
        self.distances = links
        self.neighbors = multimap(links)
        self.locations = locations or defaultdict(lambda: (0, 0))

        
def multimap(pairs) -> dict:
    "Given (key, val) pairs, make a dict of {key: [val,...]}."
    result = defaultdict(list)
    for key, val in pairs:
        result[key].append(val)
    return result


class RouteProblem(Problem):
    """A problem to find a route between locations on a `Map`.
    Create a problem with RouteProblem(start, goal, map=Map(...)}).
    States are the vertexes in the Map graph; actions are destination states."""
    
    def actions(self, state): 
        """The places neighboring `state`."""
        return self.map.neighbors[state]
    
    def result(self, state, action):
        """Go to the `action` place, if the map says that is possible."""
        return action if action in self.map.neighbors[state] else state
    
    def action_cost(self, s, action, s1):
        """The distance (cost) to go from s to s1."""
        return self.map.distances[s, s1]
    
    def h(self, node):
        "Straight-line distance between state and the goal."
        locs = self.map.locations
        return straight_line_distance(locs[node.state], locs[self.goal])
    
    
def straight_line_distance(A, B):
    "Straight-line distance between two points."
    return sum(abs(a - b)**2 for (a, b) in zip(A, B)) ** 0.5
    
    
class GridProblem(Problem):
    """Finding a path on a 2D grid with obstacles. Obstacles are (x, y) cells."""

    def __init__(self, initial=(15, 30), goal=(130, 30), obstacles=(), **kwds):
        Problem.__init__(self, initial=initial, goal=goal, 
                         obstacles=set(obstacles) - {initial, goal}, **kwds)

    directions = [(-1, -1), (0, -1), (1, -1),
                  (-1, 0),           (1,  0),
                  (-1, +1), (0, +1), (1, +1)]
    
    def action_cost(self, s, action, s1): return straight_line_distance(s, s1)
    
    def h(self, node): return straight_line_distance(node.state, self.goal)
                  
    def result(self, state, action): 
        "Both states and actions are represented by (x, y) pairs."
        return action if action not in self.obstacles else state
    
    def actions(self, state):
        """You can move one cell in any of `directions` to a non-obstacle cell."""
        x, y = state
        return {(x + dx, y + dy) for (dx, dy) in self.directions} - self.obstacles

def straight_line_distance(A, B):
    "Straight-line distance between two points."
    return sum(abs(a - b)**2 for (a, b) in zip(A, B)) ** 0.5

def transpose(matrix): return list(zip(*matrix))

land_grid1 = [[1,1,2,3,3],[1,2,1,3,1],[1,1,3,1,1],[2,2,2,3,3],[3,1,1,1,1]]
land_grid2 = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]

def create_uniform_land_grid(n): 
    column = [1] * n
    grid = [column] * n 
    return grid 

def create_random_land_grid(n): 
    matrix = [] 
    random.seed(30)
    for i in range(0,n): 
        row = [] 
        for i in range(0,n): 
            row.append(random.randint(1, 3))
        matrix.append(row)
    return matrix 
    
land_grid3 = create_uniform_land_grid(10) 
land_grid4 = create_random_land_grid(10)


# TODO: complete the code as described in the notebook 

# ANSWER TO QUESTION 4 GOES HERE 
# question 4 ANSWER GOES HERE 
# add your GridProblemMod class 
# and then check that the code provided works 
# and produces the desired output 
# you can add some check of your own to 
# see how things work 

class GridProblemMod(Problem):
    """Finding a path on a 2D grid with obstacles. Obstacles are (x, y) cells."""

    def __init__(self, initial=(15, 30), goal=(130, 30), size = 10, obstacles=(), **kwds):
        self.size = size
        Problem.__init__(self, initial=initial, goal=goal, 
                         obstacles=set(obstacles) - {initial, goal}, **kwds)

    #directions = [(0, -1),(1, 0),(0, +1),(-1, 0)]
    directions = [(0,+1),(1,0),(0,-1),(-1,0)]
    #directions =[(1,0), (0,+1), (0,-1),(-1,0)]
    
    def action_cost(self, s, action, s1): return straight_line_distance(s, s1)
    
    def h(self, node): return straight_line_distance(node.state, self.goal)
                  
    def result(self, state, action): 
        "Both states and actions are represented by (x, y) pairs."
        return action if action not in self.obstacles else state
    
    def actions(self, state):
        """You can move one cell in any of `directions` to a non-obstacle cell."""       
        x, y = state
        #print({((x + dx)%self.size, (y + dy)%self.size) for (dx, dy) in self.directions} - self.obstacles
        return {((x + dx)%self.size, (y + dy)%self.size) for (dx, dy) in self.directions} - self.obstacles
        #(y + dy)%self.size

def straight_line_distance(A, B):
    "Straight-line distance between two points."
    return sum(abs(a - b)**2 for (a, b) in zip(A, B)) ** 0.5

def transpose(matrix): return list(zip(*matrix))


g1 = GridProblemMod(initial = (2,2), goal = (7,6), size=10)
(bfs_g1, reached, frontiers) = breadth_first_bfs(g1)
print(path_states(bfs_g1))
(ucs_g1, reached, frontiers) = uniform_cost_search(g1)
print(path_states(ucs_g1))

g2 = GridProblemMod(initial = (2,2), goal = (8,8), size=10)
(ucs_g2, reached, frontiers) = uniform_cost_search(g2)
print(path_states(bfs_g1))

g3 = GridProblemMod(initial = (2,2), goal = (4,4), size=5)
(ucs_g3, reached, frontiers) = uniform_cost_search(g3)
print(path_states(ucs_g3))



# desired answer 
# [(2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (1, 6), (0, 6), (9, 6), (8, 6), (7, 6)]
# [(2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
# [(2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (1, 6), (0, 6), (9, 6), (8, 6), (7, 6)]
# [(2, 2), (2, 3), (2, 4), (3, 4), (4, 4)]

# EXAMPLE client code 
g1 = GridProblemMod(initial = (2,2), goal = (7,6), size=10)
(bfs_g1, reached, frontiers) = breadth_first_bfs(g1)
print(path_states(bfs_g1))
(ucs_g1, reached, frontiers) = uniform_cost_search(g1)
print(path_states(ucs_g1))

g2 = GridProblemMod(initial = (2,2), goal = (8,8), size=10)
(ucs_g2, reached, frontiers) = uniform_cost_search(g2)
print(path_states(bfs_g1))

g3 = GridProblemMod(initial = (2,2), goal = (4,4), size=5)
(ucs_g3, reached, frontiers) = uniform_cost_search(g3)
print(path_states(ucs_g3))



# QUESTION 5 and 6 ANSWER GOES HERE 



# This code will not work until you have implemented LandGridProblem 

# QUESTION 5 ANSWER GOES HERE 
#there may not be any obstacles in this question, but ill keep them just in case
class LandgridProblem(Problem):
    """Finding a path on a 2D grid with obstacles. Obstacles are (x, y) cells."""

    def __init__(self, initial=(2, 2), goal=(4, 4), land_grid=[],  obstacles=(), **kwds):
        size = len(land_grid)
        Problem.__init__(self, initial=initial, goal=goal,land_grid = land_grid, size = size, obstacles=set(obstacles) - {initial, goal}, **kwds)

    #directions = [(0, -1),(1, 0),(0, +1),(-1, 0)]
    directions = [(0,+1),(1,0),(0,-1),(-1,0)]
    #directions =[(1,0), (0,+1), (0,-1),(-1,0)]
    
    def action_cost(self, s, action, s1): 
       # print(action)
       # self.land_grid[i][j] *
        x,y = action
       # print(self.land_grid[x][y])
        return self.land_grid[x][y] * straight_line_distance(s, s1)
       # x,y = action
        #print(s1)
        
    
    def h(self, node): return straight_line_distance(node.state, self.goal)
                  
    def result(self, state, action): 
        "Both states and actions are represented by (x, y) pairs."
        return action if action not in self.obstacles else state
    
    def actions(self, state):
        """You can move one cell in any of `directions` to a non-obstacle cell."""       
        x, y = state
        #print({((x + dx)%self.size, (y + dy)%self.size) for (dx, dy) in self.directions} - self.obstacles
        return {((x + dx)%self.size, (y + dy)%self.size) for (dx, dy) in self.directions} - self.obstacles
        #(y + dy)%self.size

def straight_line_distance(A, B):
    "Straight-line distance between two points."
    return sum(abs(a - b)**2 for (a, b) in zip(A, B)) ** 0.5

def transpose(matrix): return list(zip(*matrix))


# QUESTION 6 ANSWER GOES HERE 

class LandgridProblem(Problem):
    """Finding a path on a 2D grid with obstacles. Obstacles are (x, y) cells."""

    def __init__(self, initial=(2, 2), goal=(4, 4), land_grid=[],heuristic = '',obstacles=(), **kwds):
        size = len(land_grid)
        Problem.__init__(self, initial=initial, goal=goal,land_grid = land_grid, size = size, heuristic = heuristic, obstacles=set(obstacles) - {initial, goal}, **kwds)

    #directions = [(0, -1),(1, 0),(0, +1),(-1, 0)]
    directions = [(0,+1),(1,0),(0,-1),(-1,0)]
    #directions =[(1,0), (0,+1), (0,-1),(-1,0)]
    
    def action_cost(self, s, action, s1): 
        x,y = action
        if self.heuristic == 'straight':
            return self.land_grid[x][y] * straight_line_distance(s, s1)
        else:
            #print("pls print")
            return self.land_grid[x][y] * manhattan_distance(s, s1)
        
    
    def h(self, node): return straight_line_distance(node.state, self.goal)
                  
    def result(self, state, action): 
        "Both states and actions are represented by (x, y) pairs."
        return action if action not in self.obstacles else state
    
    def actions(self, state):
        """You can move one cell in any of `directions` to a non-obstacle cell."""       
        x, y = state
        #print({((x + dx)%self.size, (y + dy)%self.size) for (dx, dy) in self.directions} - self.obstacles
        return {((x + dx)%self.size, (y + dy)%self.size) for (dx, dy) in self.directions} - self.obstacles
        #(y + dy)%self.size

def straight_line_distance(A, B):
    "Straight-line distance between two points."
    
    return sum(abs(a - b)**2 for (a, b) in zip(A, B)) ** 0.5

def manhattan_distance(A, B):
    return sum(abs(a - b) for (a, b) in zip(A, B))

def transpose(matrix): return list(zip(*matrix))





# This code will not work until you have implemented appropriately the LandGridProblem class 


land_grid1 = [[1,1,2,3,3],[1,2,1,3,1],[1,1,3,1,1],[2,2,2,3,3],[3,1,1,1,1]]
land_grid2 = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]

def create_uniform_land_grid(n): 
    column = [1] * n
    grid = [column] * n 
    return grid 

def create_random_land_grid(n): 
    matrix = [] 
    random.seed(30)
    for i in range(0,n): 
        row = [] 
        for i in range(0,n): 
            row.append(random.randint(1, 3))
        matrix.append(row)
    return matrix 
    
land_grid3 = create_uniform_land_grid(10) 
land_grid4 = create_random_land_grid(10)

#print(land_grid4)
print(land_grid1)


def plot_grid_problem(grid, solution, reached=(), title='Search', show=True):
    "Use matplotlib to plot the grid, obstacles, solution, and reached."
    grass_points = [] 
    hill_points = [] 
    mountain_points = [] 
    for i in range(0,grid.size): 
        for j in range(0,grid.size): 
            if (grid.land_grid[i][j] == 1): 
                grass_points.append((i,j))
            elif (grid.land_grid[i][j] == 2): 
                hill_points.append((i,j))
            elif (grid.land_grid[i][j] == 3): 
                mountain_points.append((i,j))
    
    nlocations =  grid.size
    plt.figure(figsize=(5, 5))
    plt.axis('on'); 
    plt.xlim((-0.5,nlocations-0.5))
    plt.ylim((-0.5,nlocations-0.5))
    if (grass_points):
        plt.scatter(*transpose(grass_points), (250 / nlocations) **2, marker='s', c='green')
    if (hill_points): 
        plt.scatter(*transpose(hill_points), (250 / nlocations) **2, marker='s', c='yellow')
    if (mountain_points): 
        plt.scatter(*transpose(mountain_points), (250 / nlocations) **2, marker='s', c='black')
    plt.scatter(*transpose(reached), (50/nlocations)**2, marker='o', c='blue')
    plt.scatter(*transpose(path_states(solution)), (100 / nlocations) **2,marker='s', c='red')
    plt.scatter(*transpose([grid.initial]), (125/nlocations)**2, marker='8', c='orange')
    plt.scatter(*transpose([grid.goal]), (125/nlocations)**2, marker='*', c='orange')
    if show: plt.show()
    print('{} {} search: {:.1f} path cost, {:,d} states reached'
          .format(' ' * 10, title, solution.path_cost, len(reached)))

# This code will not work until you have implemented appropriately the LandGridProblem class 

d1 = LandgridProblem(initial = (2,2), land_grid = land_grid1)
(bfs_d1, reached, frontiers) = breadth_first_bfs(d1)
print(path_states(bfs_d1))
print(path_states(bfs_d1))

plot_grid_problem(d1, bfs_d1, reached, title='BFS', show=True)
(ucs_d1, reached, frontiers) = uniform_cost_search(d1) 
plot_grid_problem(d1, ucs_d1, reached, title='UniformCost', show=True)
(ass_d1, reached, frontiers) = astar_search(d1)
plot_grid_problem(d1, ass_d1, reached, title='A* search', show=True)


d3 = LandgridProblem(initial = (2,2), goal=(7,6), land_grid = land_grid3)
(bfs_d3, reached, frontiers)= breadth_first_bfs(d3)
print(path_states(bfs_d3))
plot_grid_problem(d3, bfs_d3, reached, title='BFS', show=True)


d4 = LandgridProblem(initial = (2,2), goal=(7,6), land_grid = land_grid4)
(bfs_d4, reached, frontiers) = breadth_first_bfs(d4)
plot_grid_problem(d4, bfs_d4, reached, title='BFS', show=True)
(ucs_d4, reached, frontiers) = uniform_cost_search(d4)
plot_grid_problem(d4, ucs_d4, reached, title='UCF', show=True)
(ass_d4, reached, frontiers) = astar_search(d4)
plot_grid_problem(d4, ass_d4, reached, title='A*', show=True)
(grs_d4, reached, frontiers) = greedy_bfs(d4)
plot_grid_problem(d4, grs_d4, reached, title='Greedy', show=True)
        

# Test code below will only work with appropriate LandgridProblem defined 
d4_h2 = LandgridProblem(initial = (2,2), goal=(7,6), land_grid = land_grid4, heuristic='manhattan')
(bfs_d4, reached, frontiers) = breadth_first_bfs(d4_h2)
plot_grid_problem(d4_h2, bfs_d4, reached, title='BFS', show=True)
(ucs_d4, reached, frontiers) = uniform_cost_search(d4_h2)
plot_grid_problem(d4_h2, ucs_d4, reached, title='UCF', show=True)
(ass_d4, reached, frontiers) = astar_search(d4_h2)
plot_grid_problem(d4_h2, ass_d4, reached, title='A*', show=True)
(grs_d4, reached, frontiers) = greedy_bfs(d4_h2)
plot_grid_problem(d4_h2, grs_d4, reached, title='Greedy', show=True)


d2 = LandgridProblem(initial = (2,2), goal=(7,6), land_grid = land_grid4)
(bfs_d2, reached, frontiers) = breadth_first_bfs(d2)
plot_grid_problem(d2, bfs_d2, reached, title='BFS', show=True)
(ucs_d2, reached, frontiers) = uniform_cost_search(d2)
plot_grid_problem(d2, ucs_d2, reached, title='UCF', show=True)
(ass_d2, reached, frontiers) = astar_search(d2)
plot_grid_problem(d2, ass_d2, reached, title='A*', show=True)
(grs_d2, reached, frontiers) = greedy_bfs(d2)
plot_grid_problem(d2, grs_d2, reached, title='Greedy', show=True)

