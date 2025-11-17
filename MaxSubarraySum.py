n = int(input())
arr = list(map(int, input().split()))

max_sum = cur_sum = arr[0]
for i in arr[1:]:
    cur_sum = max(i, cur_sum + i)
    max_sum = max(max_sum, cur_sum)
print(max_sum)