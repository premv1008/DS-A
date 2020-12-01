from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        countByKey = {}
        for n in nums:
            if n in countByKey:
                countByKey[n] += 1
                return True
            else:
                countByKey[n] = 1
        return False


solObj = Solution()
print(solObj.containsDuplicate([1, 2, 3, 1]))
print(solObj.containsDuplicate([1, 2, 3, 4]))
