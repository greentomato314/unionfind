#unionfind経路圧縮あり
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = list(range(n))
        self.members = [set([i]) for i in range(n)]
        self.roots = set(range(n))

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if self.parents[x] > self.parents[y]:
            x, y = y, x
        if x == y:
            return
        for i in list(self.members[y]):
            self.members[x].add(i)
        self.members[y] = set()
        self.roots.remove(y)
        self.parents[y] = x

    def size(self, x):#O(1)xが含まれる集合の要素数
        return len(self.members[self.find(x)])

    def same(self, x, y):#O(1)
        return self.find(x) == self.find(y)

    def membersf(self, x):#取り出し部分はO(1)
        return self.members[self.find(x)]

    def rootsf(self):#根の要素、取り出し部分はO(1)
        return self.roots

    def group_count(self):#根の数O(1)
        return len(self.roots)

    def all_group_members(self):#O(N)
        return {r: self.members[r] for r in list(self.roots)}

l = ['A', 'B', 'C', 'D', 'E']#出現文字すべて
d = {x: i for i, x in enumerate(l)}
d_inv = {i: x for i, x in enumerate(l)}
uf_s = UnionFind(len(l))
uf_s.union(d['A'], d['D'])
uf_s.union(d['D'], d['C'])
uf_s.union(d['E'], d['B'])
print(d_inv[uf_s.find(d['D'])])