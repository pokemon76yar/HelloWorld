import random

n = 10
arr = list()
for i in range(n):
    number = random.randint(1,100)
    arr.append(number)

print('Not sorted: ')
print(arr)
print('-----')

########################################################

left_index = 0
right_index = n-1
is_sorted = True

while left_index <= right_index:
    for i in range(left_index, right_index, +1):
        left = arr[i]
        right = arr[i+1]
        if left > right:
            is_sorted = False
            arr[i] = right
            arr[i+1] = left
    right_index -= 1
    print(arr)
    for i in range(right_index, left_index, -1):
        right = arr[i]
        left = arr[i-1]
        if left > right:
            is_sorted = False
            arr[i] = left
            arr[i-1] = right
    left_index += 1
    print(arr)
    if is_sorted is True:
        break
    else:
        is_sorted = True

########################################################

print('Sorted: ')
print(arr)