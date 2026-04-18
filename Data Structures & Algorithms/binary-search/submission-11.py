class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_index = 0
        right_index = len(nums) - 1

        while (left_index <= right_index):
            midpoint = left_index + ((right_index - left_index) // 2)

            if nums[midpoint] < target:
                left_index = midpoint + 1
            elif nums[midpoint] > target:
                right_index = midpoint - 1
            else:
                return midpoint
        return -1


