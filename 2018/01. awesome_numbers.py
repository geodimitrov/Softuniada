def classify_number(num, fav_num):
    result = 0

    if not num % 2 == 0:
        result += 1
    if num < 0:
        result += 1
    if num % fav_num == 0:
        result += 1

    return result

def print_result(result):
    if not result:
        print("boring")
    elif result == 1:
        print("awesome")
    elif result == 2:
        print("super awesome")
    else:
        print("super special awesome")

number = int(input())
fav_number = int(input())
result = classify_number(number, fav_number)
print_result(result)