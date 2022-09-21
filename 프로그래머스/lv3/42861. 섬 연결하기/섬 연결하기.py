from collections import defaultdict
from itertools import combinations

class DisjointSet():
    def __init__(self, node):
        self.data = set([node])
        self.root = self
        self.node = node
        
    def compareset(self, ds):
        if len(self.data) > len(ds.data):
            return self, ds
        else:
            return ds, self
    
    def findroot(self):
        cur = self
        while cur.root != cur:
            cur =  cur.root
        return cur

def solution(n, costs):
    answer, cnt = 0, 0
    costs = sorted(costs, key = lambda x: x[-1])
    dj = [DisjointSet(i) for i in range(n)]
    for a, b, c in costs:
        djset1, djset2 = dj[a], dj[b]
        r1, r2 = djset1.findroot(), djset2.findroot()
        if r1.node != r2.node:
            p, ch = r1.compareset(r2)
            p.data = p.data.union(ch.data)
            ch.root = p.root
            cnt += 1
            answer += c
        if cnt == n - 1:
            break
    return answer
    
    
                  
