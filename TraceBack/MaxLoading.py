from functools import total_ordering
import heapq


class BBNode:
    parent = None
    left_child = True

    def __init__(self, p, lc):
        self.parent = p
        self.left_child = lc


@total_ordering
class HeapNode:
    live_node = None
    uweight = None
    level = 0

    def __init__(self, node, up, lev):
        self.live_node = node
        self.uweight = up
        self.level = lev

    def __le__(self, other):
        return self.uweight < other.uweight

    def __eq__(self, other):
        return self.uweight == other.uweight


def add_live_node(up, lev, par, ch, heap):
    heap.append(HeapNode(BBNode(par, ch), up, lev))
    heapq._heapify_max(heap)


def max_loading(w, c, bestx):
    heap = []
    n = len(w) - 1
    e = BBNode
    i = 1
    ew = 0
    r = [0] * (n + 1)
    for j in range(n - 1, 0, -1):
        r[j] = r[j + 1] + w[j + 1]

    while i != n + 1:
        if ew + w[i] <= c:
            add_live_node(ew + w[i] + r[i], i + 1, e, True, heap)
        add_live_node(ew + r[i], i + 1, e, False, heap)
        node = heapq._heappop_max(heap)
        i = node.level
        e = node.live_node
        ew = node.uweight - r[i - 1]

    for j in range(n, 0, -1):
        if e.left_child:
            bestx[j] = 1
        else:
            bestx[j] = 0
        e = e.parent
    return ew


bestx = [0] * 5
ew = max_loading([2, 2, 6, 5, 4], 16, bestx)
print(bestx)
