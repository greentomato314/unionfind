import collections
class UnionFind():
    def __init__(self):
        '''
        unionfind経路圧縮あり,要素にtupleや文字列可,始めに要素数指定なし
        '''
        self.parents = dict()                                   #{要素:番号,}
        self.membersf = collections.defaultdict(lambda : set()) #setの中はtupleや文字列可
        self.rootsf = set()                                     #tupleや文字列可
        self.d = dict()
        self.d_inv = dict()
        self.cnt = 0
    
    def dictf(self,x):
        if x in self.d:
            return self.d[x]
        else:
            self.cnt += 1
            self.d[x] = self.cnt
            self.parents[x] = self.cnt
            self.d_inv[self.cnt] = x
            self.membersf[x].add(x)
            self.rootsf.add(x)
            return self.d[x]

    def find(self, x):
        self.dictf(x)
        if self.parents[x] == self.dictf(x):
            return x
        else:
            self.parents[x] = self.d[self.find(self.d_inv[self.parents[x]])]
            return self.d_inv[self.parents[x]]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        if x == y:
            return
        for i in list(self.membersf[y]):
            self.membersf[x].add(i)
        self.membersf[y] = set()
        self.rootsf.remove(y)
        self.parents[y] = self.d[x]

    def size(self, x):#xが含まれる集合の要素数
        return len(self.membersf[self.find(x)])

    def same(self, x, y):#同じ集合に属するかの判定
        return self.find(x) == self.find(y)

    def members(self, x):#xを含む集合の要素
        return self.membersf[self.find(x)]

    def roots(self):#根の要素
        return self.rootsf

    def group_count(self):#根の数
        return len(self.rootsf)

    def all_group_members(self):#根とその要素
        return {r: self.membersf[r] for r in list(self.rootsf)}

if __name__=="__main__":
    uf_s = UnionFind()
    uf_s.union('A', 'D')
    uf_s.union('D', 'C')
    uf_s.union('E', 'B')
    print(uf_s.members('D'))
    print(uf_s.members('E'))
    uf_s.union('A', 'B')
    print(uf_s.members('E'))
    print(uf_s.same('A','F'))
    print(uf_s.members('F'))
    print(uf_s.members('G'))

    print()
    uf_t = UnionFind()
    uf_t.union((2,3),(3,4))
    uf_t.union((4,3),(5,4))
    uf_t.union((1,3),(3,4))
    print(uf_t.members((2,3)))
    print(uf_t.roots())
    print(uf_t.group_count())
    print(uf_t.all_group_members())

    print()
    uf_ts = UnionFind()
    uf_ts.union((2,3),1)
    uf_ts.union((4,3),'A')
    uf_ts.union((1,3),(3,4))
    uf_ts.union((1,3),'A')
    print(uf_ts.members((2,3)))
    print(uf_ts.roots())
    print(uf_ts.all_group_members())
    print(uf_ts.size('A'))