import math
from typing import List


def chunkify(n: int, m: int) -> List[int]:
    """Divides n into uniform groups, the maximum number in the group is m"""
    k = math.ceil(n / m)
    ost = n - n // k * k
    groups = [n // k for _ in range(k)]
    for i in range(ost):
        groups[groups.index(min(groups))] += 1
    return groups
