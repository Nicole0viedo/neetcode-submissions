class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        for i, j in enumerate(nums):
            if (target-j) not in seen:
                seen[j] = i
            else:
                return [seen[target-j], i]
        