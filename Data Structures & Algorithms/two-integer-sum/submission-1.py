class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_values = {}

        for i, num in enumerate(nums):
            needed_value = target - num
            
            if(needed_value in seen_values):
                return [seen_values[needed_value], i]

            seen_values[num] = i