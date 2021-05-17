def read_input():
    return [int(el) for el in input().split()]


def calculate_sum_nums(nums, n, index=0, comb=[], result=[]):

    if n == 0:
        result.append(sum(comb))
        return

    num = nums[index]

    for el in (num, -num):
        comb.append(el)
        calculate_sum_nums(nums, n - 1, index + 1, comb, result)
        comb.pop()

    return result


def print_result(result):

    if result:
        print("Yes")
    else:
        print("No")


n = 3
nums = read_input()
sums = calculate_sum_nums(nums, n)
result = [sum for sum in sums if sum == 13]
print_result(result)