def create_house_roof(n):
    top_line = (n - 1) * "." + "*" + (n - 1) * "." + "\n"
    bottom_line = "*" + (n - 1) * " *" + "\n"
    middle_lines = ""

    for i in range(0, n - 2):
        line = (n - i - 2) * "." + "*" + (2 * i + 1) * " " + "*" + (n - i - 2) * "." + "\n"
        middle_lines += line

    return top_line + middle_lines + bottom_line

def create_house_body(n, width):
    top_line = "+" + (width - 2) * "-" + "+"
    bottom_line = top_line
    middle_lines = ""

    for i in range(2, n):
        line = "|" + (width - 2) * " " + "|" + "\n"
        middle_lines += line

    return top_line + "\n" + middle_lines + bottom_line


def print_result(roof, body):
    print(roof + body)


n = int(input())
width = n * 2 - 1
roof = create_house_roof(n)
body = create_house_body(n, width)
print_result(roof, body)