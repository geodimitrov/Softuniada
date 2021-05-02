from itertools import permutations

def read_input(n):
    result = []

    for _ in range(n):
        result.append(int(input()))

    return result


def print_result(equal_sums, group_sum):

    if equal_sums:
        print(f"Yes\n{group_sum}")
    else:
        print("No")

n = 4
nums = read_input(n)
perms = permutations(nums)
equal_sums = False
group_sum = None

for p in perms:

    if equal_sums:
        break

    for i in range(1, n):
        group_one = p[:i]
        group_two = p[i:]

        if sum(group_one) == sum(group_two):
            equal_sums = True
            group_sum = sum(group_one)

print_result(equal_sums, group_sum)