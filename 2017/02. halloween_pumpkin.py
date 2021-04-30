def get_line_length(n):
    return n * 2 + 1


def create_middle_lines(n, line_len):
    result = ""
    for _ in range(n - 3):
        result += f"|{(line_len - 2) * '.'}|\n"

    return result


def create_head(n):
    top_line = (n - 1) * "." + "_/_" + (n - 1) * "." + "\n"
    second_line = "/" + (n - 2) * "." + "^,^" + (n - 2) * "." + "\\" + "\n"

    return top_line + second_line


def create_bottom(n):
    bottom_line = "\\" + (n - 2) * "." + "\_/" + (n - 2) * "." + "/"
    return bottom_line


def print_pumpkin(head, middle_lines, bottom):
    print(head + middle_lines + bottom)


n = int(input())
line_len = get_line_length(n)
pumpkin_head = create_head(n)
middle_lines = create_middle_lines(n, line_len)
pumpkin_bottom = create_bottom(n)
print_pumpkin(pumpkin_head, middle_lines, pumpkin_bottom)