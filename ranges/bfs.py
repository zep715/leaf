import json


def bfsiter(nodes, links, start):
    q = [start]
    visited = set([start])
    while len(q) > 0:
        current = q.pop()
        for link in links[current]:
            if link not in visited:
                visited.add(link)
                q.append(link)
        yield nodes[current]


if __name__ == "__main__":
    with open("prova.json", "r") as fp:
        j = fp.read()
    graph = json.loads(j)
    hosts = graph["env"]["hosts"]
    links = graph["env"]["network"]["links"]
    for host in bfsiter(hosts, links, "main"):
        print (host)
