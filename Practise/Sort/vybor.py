import random

n = 5
arr = list()
for i in range(n):
    number = random.randint(1,100)
    arr.append(number)

print('Not sorted: ')
print(arr)
print('-----')

########################################################

for i in range(n-1):
    min_max = i
    for j in range(i+1, n, 1):
        if arr[j] < arr[min_max]:
            min_max = j
    temp = arr[i]
    arr[i] = arr[min_max]
    arr[min_max] = temp

########################################################

print('Sorted: ')
print(arr)