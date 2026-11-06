
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        D = {}
        L = []

        for num in nums:
            if num in D:
                D[num] = D[num] + 1
            else:
                D[num] = 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in D.items():
            buckets[count].append(num)

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                L.append(num)

                if len(L) == k:
                    return L

        return L
