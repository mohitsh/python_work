
def solution(nums,target):
	nums.sort()
        for i in range(len(nums)):
            to_look = target-nums[i]
            
        second = nums.index(to_look)
        return [second,i]

print solution([1,2,3,4],5)
        
