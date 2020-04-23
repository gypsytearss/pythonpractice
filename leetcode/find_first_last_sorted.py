from typing import List

class Solution(object):
    """
    https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
    Note: search must be O(log n) time
    Example:
        Input: nums = [5,7,7,8,8,10], target = 8
        Output: [3,4]
    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        else:
            return [self.searchLeft(nums, target, 0), self.searchRight(nums, target, 0)]


    def searchLeft(self, nums: List[int], target: int, carry: int) -> int:
        if not nums:
            return -1
        midpoint = len(nums) // 2
        this_num = nums[midpoint]
        if this_num == target:
            this_left = self.searchLeft(nums[:midpoint], target, carry)
            if this_left == -1:
                this_left_right = self.searchRight(nums[:midpoint], target, carry)
                if this_left_right == -1:
                    return midpoint + carry
                return this_left_right
            return this_left
        elif this_num < target:
            return self.searchLeft(nums[midpoint + 1:], target, carry + midpoint + 1)
        else:
            return self.searchLeft(nums[:midpoint], target, carry)


    def searchRight(self, nums: List[int], target: int, carry: int) -> int:
        if not nums:
            return -1
        midpoint = len(nums) // 2
        this_num = nums[midpoint]
        if this_num == target:
            this_right = self.searchRight(nums[midpoint + 1:], target, carry + midpoint + 1)
            if this_right == -1:
                this_right_left = self.searchLeft(nums[midpoint + 1:], target, carry + midpoint + 1)
                if this_right_left == -1:
                    return midpoint + carry
                return this_right_left
            return this_right
        elif this_num < target:
            return self.searchRight(nums[midpoint + 1:], target, carry + midpoint + 1)
        else:
            return self.searchRight(nums[:midpoint], target, carry)