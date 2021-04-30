HAPPY_EASTER = "HAPPY EASTER"

def calc_width_and_height(n):
    width = 5 * n
    height = 2 * n + 3
    return width, height

def calc_num_tildes(n, egg_width):
    asterisks = 4
    dots = n
    length_without_tilde = asterisks + dots + len(HAPPY_EASTER)
    num_tildes = egg_width - length_without_tilde

    return num_tildes // 2

def create_middle_line(n, width, dots):
    num_tildes = calc_num_tildes(n, width)
    first_half = dots + 2 * "*" + num_tildes * "~"
    result = first_half + HAPPY_EASTER + first_half[::-1]

    return result

def create_egg(n, egg_width, egg_height):
    result = ""
    dots = n // 2 * "."
    middle_line = create_middle_line(n, egg_width, dots)
    result += middle_line

    for i in range(n + 1):

        if i < n // 2:
            asteriks = 2 * "*"
            eq_signs = (egg_width // 2 - (len(dots) + len(asteriks))) * "="
            first_half = dots + asteriks + eq_signs
            line = first_half + first_half[::-1]
            dots += "."

        elif i < n:
            asteriks = (n - i) * "*"
            plus_signs = (egg_width // 2 - (len(dots) + len(asteriks))) * "+"
            first_half = dots + asteriks + plus_signs
            line = first_half + first_half[::-1]
            dots += 2 * "."

        else:
            asteriks = n * "*"
            line = dots + asteriks + dots


        result = line + "\n" + result + "\n" + line

    return result

def print_result(egg):
    print(egg)

n = int(input())
egg_width, egg_height = calc_width_and_height(n)
egg = create_egg(n, egg_width, egg_height)
print_result(egg)