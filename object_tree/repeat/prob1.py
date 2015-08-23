



def twoSum(nums, target):
	length = len(nums)
        nums.sort()
        for i in range(length):
            lookup = target-nums[i]
            index = binary_search(lookup,nums)
            if index == True:
		return 
            
                
            
def binary_search(lookup,nums):
        length = len(nums)
        mid = nums[length//2]
        if lookup > mid:
            #print nums
	    #print nums[length//2]
            return binary_search(lookup,nums[(length//2)+1:])
        elif lookup < mid:
            #print nums
	    #print nums[length//2]
            return binary_search(lookup,nums[:length//2])
        elif lookup == mid:
	    #print nums
  	    #print nums[length//2]
            return True
	else:
	    return False


print twoSum([4,3,2,1],5)
#print binary_search(5,[1,2,3,4,5,6,7,8,9,10])
