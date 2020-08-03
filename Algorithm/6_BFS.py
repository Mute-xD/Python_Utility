"""
广度优先算法
非加权图
指出是否有A到B的路径
多层网络（人际关系网）
时间复杂度：⚪(V + E)  -> V:顶点  E:边数
"""
from collections import deque

graphs = dict()  # 构建一个图
graphs["host"] = ["alice", "bob", "charlie"]
graphs["alice"] = ["peggy"]
graphs["bob"] = ["anuj", "peggy"]
graphs["charlie"] = ["thom", "jonny"]
graphs["anuj"] = []
graphs["peggy"] = []
graphs["thom"] = []
graphs["jonny"] = []
print(graphs)
thePerson = "peggy"


def search(graphs_):
    search_queue = deque()  # 双端队列
    search_queue += graphs_["host"]
    searched = []
    while search_queue:  # 当序列非空
        person = search_queue.popleft()
        if person not in searched:
            if person == thePerson:
                return person
            else:
                search_queue += graphs_[person]
                searched.append(person)
    return 'NotFound'


print(search(graphs))
