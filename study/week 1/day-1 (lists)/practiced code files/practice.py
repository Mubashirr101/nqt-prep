nums=[int(num) for num in input().split() ]

print(nums[0])   # first
print(nums[-1])  # last
print(nums[1:4]) # slicing 1 to 4
print(len(nums)) # length of list
print(9 in nums) # is 9 present in the list

###################

nums.append(7) # add 7 to the end
print(nums)

nums.remove(1) # delete the first instance of 1
print(nums)
 
nums.pop()     # delete the last element
print(nums)

nums.pop(0)    # deletes the first element
print(nums)

nums.sort()     # sorts in ascending
print(nums)

nums.reverse()  # reverses the list
print(nums)

print(nums.count(1)) # return the number of times '1' is in the list
print(nums.index(5)) # returnd the postion of '5'

print(nums)

"""
3 1 4 1 5 9 2 6
3
6
[1, 4, 1]
8
True
[3, 1, 4, 1, 5, 9, 2, 6, 7]
[3, 4, 1, 5, 9, 2, 6, 7]
[3, 4, 1, 5, 9, 2, 6]
[4, 1, 5, 9, 2, 6]
[1, 2, 4, 5, 6, 9]
[9, 6, 5, 4, 2, 1]
1
2
[9, 6, 5, 4, 2, 1]

"""