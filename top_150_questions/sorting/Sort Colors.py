class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red_count = 0
        white_count = 0
        blue_count = 0
        for i in nums:
            if i == 0:
                red_count+=1
            elif i==1:
                white_count+=1
            elif i ==2:
                blue_count+=1

        for i in range(len(nums)):
            if red_count!=0:
                nums[i]=0
                red_count-=1
            elif white_count!=0:
                nums[i]=1
                white_count-=1
            else:
                nums[i]=2
                blue_count-=1

        return(nums)                


