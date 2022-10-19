# Excercise 1 Write a script that would use Breadth first search (BFS) to allow for the students’ introductions to each
# other with the least number of intermediate students for the introduction, i.e. find the shortest path.

from students_list import graph, graph2


def bfs_garnett(graph_name, start, end):
    # mark all visited nodes in the graph
    visited = []

    # create a queue for bfs
    queue = []

    # mark the source node as visited and enqueue it
    queue.append(start)
    visited.append(start)

    while queue:
        # mark the frontier
        f = queue.pop(0)
        print(f, end=" ")

        if f is end:
            print('This is the end node')
            queue.clear()
        else:
            # Get all adjacent vertices
            # of the dequeued vertex s.
            # If an adjacent has not been visited,
            # then mark it visited and enqueue it
            for i in graph_name[f]:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)


bfs_garnett(graph2, 'Adam', 'Garnett')
