DIV_BY_12 = "Divisible by 12"
DIV_BY_15 = "Divisible by 15"

def create_two_digit_nums_from_num(number):
    num1 = number[0] + number[2]
    num2 = number[1] + number[3]

    return num1, num2


def calc_ceiling(num1, num2):
    return int(num1) + int(num2)


def generate_numbers(num1, num2, ceiling):
    result = {
        DIV_BY_12: [],
        DIV_BY_15: []
    }
    first_number_range = range(int(num1), ceiling + 1)
    second_number_range = range(int(num2), ceiling + 1)

    for x in first_number_range:

        for y in second_number_range:
            number = int(str(x) + str(y))

            if number % 12 == 0:
                result[DIV_BY_12].append(str(number))

            if number % 15 == 0:
                result[DIV_BY_15].append(str(number))

    return result


def print_result(result):
    divisible_by_12 = f"Dividing on 12: {' '.join(result[DIV_BY_12])}\n"
    divisible_by_15 = f"Dividing on 15: {' '.join(result[DIV_BY_15])}\n"

    if len(result[DIV_BY_12]) == len(result[DIV_BY_15]):
        bingo = "!!!BINGO!!!"
    else:
        bingo = "NO BINGO!"

    print(divisible_by_12 + divisible_by_15 + bingo)

input_number = input()
first_num, second_num = create_two_digit_nums_from_num(input_number)
ceiling = calc_ceiling(first_num, second_num)
bingo_numbers = generate_numbers(first_num, second_num, ceiling)
print_result(bingo_numbers)