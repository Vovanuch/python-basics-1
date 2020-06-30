''' Функция прохода по графу '''

def find_path(graph, start, end, path=[]):
    
    path = path + [start]

    if start == end:
        return path

    if not graph.__contains__(start):
        return None

    for node in graph[start]:

        if node not in path:

            newpath = find_path(graph, node, end, path)

            if newpath: return newpath

    return None
        

graph = {'A': ['B', 'C'], 'B': ['C', 'D'], 'C': ['D'], 'D': ['C'], 'E': ['F'], 'F': ['C']}

A = input('Enter start point (A as example):').strip()
B = input('Enter end point (D as example):').strip()
print(find_path(graph, A, B))
