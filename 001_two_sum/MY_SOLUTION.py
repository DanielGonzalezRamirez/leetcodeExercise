def twoSum(nums=[], target=0):
	n = len(nums)
	i = 0
	j = 0
	found = False
	answer = []

	while i < n and not found:
		j = 0
		lookingfor = target - nums[i]
		while j < n and not found:
			if j != i:
				if nums[j] == lookingfor:
					found = True
					answer = [i, j]
			j += 1
		i += 1
	return answer

def main():
	nums = [-5,-8,11,15,-1,-3,0]
	target = -5
	print(twoSum(nums=nums, target=target))

if __name__ == '__main__':
	main()