class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}

        for num in nums:
            countMap[num] = 1 + countMap.get(num, 0)

        # {1: 1, 2: 3, 5: 1}

        arr = []
        for num, cnt in countMap.items():
            arr.append([cnt, num])
        arr.sort()

        # [[1,1], [1,5], [3,2]]

        res = []
        
        while len(res) < k:
            res.append(arr.pop()[1])
        
        # [2]
        
        return res
        