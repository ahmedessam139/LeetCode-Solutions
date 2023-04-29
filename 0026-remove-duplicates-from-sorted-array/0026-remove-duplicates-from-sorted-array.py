class Solution(object):
    def removeDuplicates(self, nums):
       
        
        p_one, p_two = 0, 1
        new_nums = []
        while p_two < len(nums):
            if nums[p_one] == nums[p_two]:
                p_two += 1
            else:
                new_nums.append(nums[p_one])
                p_one = p_two
                p_two += 1
        
        new_nums.append(nums[p_one])
        nums[:] = new_nums
        return len(nums)
