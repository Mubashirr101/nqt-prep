nums = [int(num) for num in input().split()]
num_2 = nums.copy()
num_3 = nums.copy()
num_4 = nums.copy()

# list of num and find max and min without using max n min func
min_val = nums[0]
max_val = nums[0]
for num in nums:
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num
print('min:', min_val)
print('max:', max_val)


# reverse a list without using .reverse() or slicing
reversed_list = []
for i in range(len(num_2)):
    last_element = num_2.pop()
    reversed_list.append(last_element)
    
print(reversed_list)
    
## remove all duplicates without changing order
result = []
for item in num_3:
    if item not in result:
        result.append(item)
print(result)


## count how many even numbers are in a list
count = 0
for num in num_4:
    if num % 2 == 0:
        count += 1
print(count)
        