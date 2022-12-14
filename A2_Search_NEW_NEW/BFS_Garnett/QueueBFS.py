'''
@author: Devangini Patel
'''

from Node import Node
from State import State
from collections import deque


def performQueueBFS(initial_state):
    """
    This function performs BFS search using a queue
    """
    # create queue
    queue = deque([])
    # since it is a graph, we create visited list
    visited = []
    # create root node
    initialState = State().getInitialState(initial_state)
    root = Node(initialState)
    # add to queue and visited list
    queue.append(root)
    visited.append(root.state.name)
    # check if there is something in queue to dequeue
    while len(queue) > 0:

        # get first item in queue
        currentNode = queue.popleft()

        print(("-- dequeue --"), currentNode.state.name)

        # check if this is goal state
        if currentNode.state.checkGoalState():
            print("reached goal state")
            # print the path
            print("----------------------")
            print("Path")
            currentNode.printPath()
            break
            # get the child nodes
        childStates = currentNode.state.successorFunction()
        for childState in childStates:

            childNode = Node(State(childState))

            # check if node is not visited
            if childNode.state.name not in visited:
                # add this node to visited nodes
                visited.append(childNode.state.name)

                # add to tree and queue
                currentNode.addChild(childNode)
                queue.append(childNode)
                # print tree
    print("----------------------")
    print("Tree")
    root.printTree()


performQueueBFS("Garnett")
