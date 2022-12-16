class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        ###########This is O(2N) solution
        
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
    ####################This is more efficent solution with O(N) complexity
        p0 = curr = 0
        p2 = len(nums)-1

        while curr<=p2:
            if nums[curr]==0:
                nums[curr], nums[p0] = nums[p0],nums[curr]
                p0+=1
                curr+=1
            elif nums[curr] ==2:
                nums[curr], nums[p2] = nums[p2],nums[curr]
                p2-=1
            else:
                curr+=1

        return nums       


