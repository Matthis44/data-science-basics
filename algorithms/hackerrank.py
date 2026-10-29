"""Solutions to HackerRank data structures and algorithms problems."""

import heapq


def pairs(k, arr):
    """Count the pairs of distinct values in ``arr`` whose difference is ``k``.

    Uses a hash set: O(n) time instead of O(n^2) for the naive double loop.
    """
    values = set(arr)
    return sum(1 for x in values if x + k in values)


class Queue:
    """FIFO queue built from two stacks (amortised O(1) per operation)."""

    def __init__(self):
        self._inbox = []
        self._outbox = []

    def enqueue(self, x):
        self._inbox.append(x)

    def _transfer(self):
        if not self._outbox:
            while self._inbox:
                self._outbox.append(self._inbox.pop())

    def dequeue(self):
        self._transfer()
        return self._outbox.pop() if self._outbox else None

    def front(self):
        self._transfer()
        return self._outbox[-1] if self._outbox else None


def is_balanced(s):
    """Return "YES" if every bracket in ``s`` is closed in the right order."""
    stack = []
    match = {")": "(", "]": "[", "}": "{"}
    for char in s:
        if char in match.values():
            stack.append(char)
        elif char in match:
            if not stack or stack.pop() != match[char]:
                return "NO"
    return "NO" if stack else "YES"


def super_digit(n, k):
    """Super digit of ``n`` repeated ``k`` times (digital root)."""
    total = sum(int(d) for d in n) * k
    while total >= 10:
        total = sum(int(d) for d in str(total))
    return total


def cookies(k, sweetness):
    """Minimum number of mix operations so that every cookie reaches ``k``.

    Mixing the two least sweet cookies gives ``least + 2 * second``.
    A min-heap gives O(n log n) overall. Returns -1 if it is impossible.
    """
    heap = list(sweetness)
    heapq.heapify(heap)
    operations = 0
    while len(heap) > 1 and heap[0] < k:
        least = heapq.heappop(heap)
        second = heapq.heappop(heap)
        heapq.heappush(heap, least + 2 * second)
        operations += 1
    return operations if heap and heap[0] >= k else -1


def lego_blocks(n, m, mod=10**9 + 7):
    """Count solid walls of height ``n`` and width ``m`` (dynamic programming).

    1. Ways to build one row of width w with blocks of width 1-4.
    2. All walls of height n: rows are independent, so ``row[w] ** n``.
    3. Subtract walls with a vertical crack: for each width, the leftmost
       crack splits the wall into a solid left part and any right part.
    """
    row = [1, 1, 2, 4]
    while len(row) <= m:
        row.append(sum(row[-4:]) % mod)
    total = [pow(r, n, mod) for r in row]

    solid = [0] * (m + 1)
    for width in range(1, m + 1):
        cracked = sum(solid[left] * total[width - left]
                      for left in range(1, width))
        solid[width] = (total[width] - cracked) % mod
    return solid[m]


class TextEditor:
    """Text editor with append, delete, print and undo."""

    def __init__(self):
        self.text = ""
        self._history = []

    def append(self, w):
        self._history.append(self.text)
        self.text += w

    def delete(self, k):
        self._history.append(self.text)
        self.text = self.text[:-k]

    def char_at(self, k):
        """Return the k-th character (1-indexed)."""
        return self.text[k - 1]

    def undo(self):
        if self._history:
            self.text = self._history.pop()
