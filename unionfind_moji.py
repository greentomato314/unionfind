import collections
class UnionFind():
    def __init__(self):
        '''
        unionfind経路圧縮あり,要素にtupleや文字列可,始めに要素数指定なし
        '''
        self.parents = dict()                                      # {子要素:親ID,}
        self.members_set = collections.defaultdict(lambda : set()) # keyが根でvalueが根に属する要素要素(tupleや文字列可)
        self.roots_set = set()                                     # 根の集合(tupleや文字列可)
        self.key_ID = dict()                                       # 各要素にIDを割り振る
        self.ID_key = dict()                                       # IDから要素名を復元する
        self.cnt = 0                                               # IDのカウンター
    
    def dictf(self,x): # 要素名とIDをやり取りするところ
        if x in self.key_ID:
            return self.key_ID[x]
        else:
            self.cnt += 1
            self.key_ID[x] = self.cnt
            self.parents[x] = self.cnt
            self.ID_key[self.cnt] = x
            self.members_set[x].add(x)
            self.roots_set.add(x)
            return self.key_ID[x]

    def find(self, x):
        ID_x = self.dictf(x)
        if self.parents[x] == ID_x:
            return x
        else:
            self.parents[x] = self.key_ID[self.find(self.ID_key[self.parents[x]])]
            return self.ID_key[self.parents[x]]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        if x == y:
            return
        for i in self.members_set[y]:
            self.members_set[x].add(i)
        self.members_set[y] = set()
        self.roots_set.remove(y)
        self.parents[y] = self.key_ID[x]

    def size(self, x):#xが含まれる集合の要素数
        return len(self.members_set[self.find(x)])

    def same(self, x, y):#同じ集合に属するかの判定
        return self.find(x) == self.find(y)

    def members(self, x):#xを含む集合の要素
        return self.members_set[self.find(x)]

    def roots(self):#根の要素
        return self.roots_set

    def group_count(self):#根の数
        return len(self.roots_set)

    def all_group_members(self):#根とその要素
        return {r: self.members_set[r] for r in self.roots_set}

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