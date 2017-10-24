# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return[s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    border = util.Stack()
    visited = []
    startNode = (problem.getStartState(), None, [])
    border.push(startNode)

    while not border.isEmpty():
        curr = border.pop()
        currLoc = curr[0]
        currDir = curr[1]
        currPath = curr[2]

        if(currLoc not in visited):
            visited.append(currLoc)

            if(problem.isGoalState(currLoc)):
                return currPath

        successors = problem.getSuccessors(currLoc)
        successorsList = list(successors)

        for i in successorsList:
            if i[0] not in visited:
                border.push((i[0], i[1], currPath + [i[1]]))

    return[]


def breadthFirstSearch(problem):
    border = util.Queue()
    visited = []
    startNode = (problem.getStartState(), None, [])
    border.push(startNode)

    while not border.isEmpty():
        curr = border.pop()
        currLoc = curr[0]
        currDir = curr[1]
        currPath = curr[2]

        if (currLoc not in visited):
            visited.append(currLoc)

            if (problem.isGoalState(currLoc)):
                return currPath

            successors = problem.getSuccessors(currLoc)
            successorsList = list(successors)

            for i in successorsList:
                if i[0] not in visited:
                    border.push((i[0], i[1], currPath + [i[1]]))
    return []


def uniformCostSearch(problem):
    border = util.PriorityQueue()
    visited = []
    startNode = ((problem.getStartState(), None, 0), [], 0)
    border.push(startNode, None)
    while not border.isEmpty():
        curr = border.pop()
        currLoc = curr[0][0]
        currDir = curr[0][1]
        currPath = curr[1]
        currCost = curr[2]
        if currLoc not in visited:
            visited.append(currLoc)
            if (problem.isGoalState(currLoc)):
                return currPath
            successors = problem.getSuccessors(currLoc)
            successorsList = list(successors)
            for i in successorsList:
                if i[0] not in visited:
                    if (problem.isGoalState(i[0])):
                        return currPath + [i[1]]
                    newNode = (i, currPath + [i[1]], currCost + i[2])
                    border.push(newNode, currCost + i[2])
    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    border = util.PriorityQueue()
    visited = []
    h = heuristic(problem.getStartState(), problem)
    g = 0
    f = g + h
    startingNode = (problem.getStartState(), None, g, []);
    border.push(startingNode, f)
    while not border.isEmpty():
        curr = border.pop()
        currLoc = curr[0]
        currDir = curr[1]
        currCost = curr[2]
        if currLoc not in visited:
            currPath = curr[3]
            visited.append(currLoc)
            successors = problem.getSuccessors(currLoc)
            successorsList = list(successors)
            for i in successorsList:
                if i[0] not in visited:
                    if (problem.isGoalState(i[0])):
                        return currPath + [i[1]]
                    h = heuristic(i[0], problem)
                    g = currCost + i[2]
                    f = g + h
                    newNode = (i[0], i[1], g, currPath + [i[1]])
                    border.push(newNode, f)
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
