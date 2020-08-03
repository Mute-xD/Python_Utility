"""
狄克斯特拉
加权图
只适用于有向无环图
无负权边（如有负权边考虑 贝尔曼-福德算法）
属于贪婪算法
时间复杂度：⚪(n^2)
"""
graphs = dict(host={})
graphs['host']['a'] = 6
graphs['host']['b'] = 2
graphs['a'] = {}
graphs['a']['target'] = 1
graphs['b'] = {}
graphs['b']['a'] = 3
graphs['b']['target'] = 5
graphs['target'] = {}
print(graphs)

infinity = float('inf')
costs = {'a': 6,
         'b': 2,
         'target': infinity}

parents = {'a': 'host',
           'b': 'host',
           'target': None}

processed = []


def findLowestCost(costs_):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs_:
        cost = costs_[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost_node = node
            lowest_cost = cost
    return lowest_cost_node


def costToTarget():
    node = findLowestCost(costs)
    while node is not None:
        cost = costs[node]
        neighbour = graphs[node]

        for i in neighbour.keys():
            new_cost = cost + neighbour[i]
            if costs[i] > new_cost:
                costs[i] = new_cost
                parents[i] = node
        processed.append(node)
        node = findLowestCost(costs)
    print(costs['target'])


costToTarget()
