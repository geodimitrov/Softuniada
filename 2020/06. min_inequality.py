n_combs = int(input())
n_nums = int(input())
nums = [int(input()) for i in range(n_nums)]
min_value = 100000000
sorted_nums = sorted(nums)

for i in range(len(sorted_nums) - n_combs + 1):
    comb = sorted_nums[i:i + n_combs]
    difference = max(comb) - min(comb)

    if difference < min_value:
        min_value = difference

print(min_value)