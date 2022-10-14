lass Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge_sort(nums):
            
            if len(nums)<=1:
                return nums
            
            pivot = len(nums)//2
            left_list = merge_sort(nums[:pivot])
            right_list = merge_sort(nums[pivot:])
            return merge(left_list,right_list)
        
        def merge(left_list,right_list):
            
            
            ret = []
            left_ptr = right_ptr = 0
            while left_ptr < len(left_list) and right_ptr < len(right_list):
                
                if left_list[left_ptr] < right_list[right_ptr]:
                    ret.append(left_list[left_ptr])
                    left_ptr+=1
                elif left_list[left_ptr]>right_list[right_ptr]: 
                    ret.append(right_list[right_ptr])
                    right_ptr+=1
                else:
                    ret.append(left_list[left_ptr])
                    ret.append(right_list[right_ptr])
                    left_ptr+=1
                    right_ptr+=1
  
            ret = ret+left_list[left_ptr:]
            ret = ret+right_list[right_ptr:]
          
            return ret
        
        return(merge_sort(nums)) 
