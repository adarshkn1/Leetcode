class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        sorted(nums)
        l = 0
        r = 1

        if(len(nums) < 2):
            return len(nums)

        while(r < len(nums)):
            if(nums[l] == nums[r]):
                r+=1
            else:
                if (nums[l]!=nums[r]):
                    nums[l+1], nums[r] = nums[r], nums[l+1]
                    l+=1
                    r+=1       
        
        return l+1
        