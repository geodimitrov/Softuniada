from itertools import permutations

def read_input():
    result = []
    for i in range(3):
        result.append(input())

    return result


def check_permutations_for_possible_division(permutations, digits_sum):
    result = False

    if digits_sum == 0:
        return result

    for p in permutations:
        number = int("".join(p))

        if number % digits_sum == 0:
            result = True
            break

    return result


def print_result(successful_digitivision):

    if not successful_digitivision:
        print("No digitivision possible.")

    else:
        print("Digitivision successful!")


digits = read_input()
digits_sum = sum(list(map(int, digits)))
perm = permutations(digits)
result = check_permutations_for_possible_division(perm, digits_sum)
print_result(result)