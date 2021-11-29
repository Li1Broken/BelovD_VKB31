class DSU:

    def __init__(self, k):
        self.parent = list(range(k))
        self.rank = [0] * k  

    def make_set(self):
        self.parent.append(len(self.parent))
        self.rank.append(0)

    def find_set(self, v):
        if v == self.parent[v]:
            return v
        self.parent[v] = self.find_set(self.parent[v])
        return self.parent[v]

    def union_sets(self, a_, b_):
        a = self.find_set(a_)
        b = self.find_set(b_)
        if a != b:
            if self.rank[a] < self.rank[b]:
                a, b = b, a
            self.parent[b] = a
            if self.rank[a] == self.rank[b]:
                self.rank[a] += 1


if __name__ == '__main__':
    n, m = map(int, input().split())
    dsu = DSU(n)
    ribs = []
    for _ in range(m):
        req = list(map(int, input().split()))
        req.reverse()
        ribs.append(req)
    ribs.sort()   
    ff = 0
    for i in ribs:
        if dsu.find_set(i[1] - 1) != dsu.find_set(i[2] - 1):
            dsu.union_sets(i[1] - 1, i[2] - 1)
            
            ff += i[0]
    print(ff)
