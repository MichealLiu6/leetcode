def twoSum(nums,target):
	i = 0;j = 0
	while i<len(nums):
		a = target - nums[i]
		for j in range(i+1,len(nums)) :
			if a==nums[j]:
				print([i,j])
		i+=1






