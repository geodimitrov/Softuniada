def create_head_lines(n):
    n_lines = n // 2
    result = ""

    for _ in range(n_lines):
        result += n * " " + 3 * n * "#" + n * " " + "\n"

    return result


def create_bottom_lines(n):
    n_lines = n // 2
    result = ""

    for _ in range(n_lines):
        result += n * " " + 3 * n * "#" + n * " " + "\n"

    return result

def add_head_and_bottom_to_middle_lines(n, width, body):
    header = n * "#" + (width - n * 2) * " " + n * "#" + "\n"
    body = header + body + header

    return body

def add_middle_lines_to_body(n, width, middle_line):
    body = middle_line

    for i in range(n - 1):

        if i % 2 == 0:
            line = n * "#" + " " + (width - (n * 2 + 2)) // 2 * " #" + "  " + n * "#" + "\n"
        else:
            line = middle_line
        body = line + body + line

    body = add_head_and_bottom_to_middle_lines(n, width, body)

    return body

def add_bottom_to_body(n, width):
    result = ""

    for i in range(n + 2):
        if i % 2 == 0:
            line = width * "#" + "\n"
        else:
            line = n * "#" + " " + (width - (n * 2)) // 2 * "# " + n * "#" + "\n"

        result += line

    return result


def create_body(n, width):
    result = ""
    middle_line = n * "#" + " " + (width - (n * 2)) // 2 * "# " + n * "#" + "\n"
    result += add_middle_lines_to_body(n, width, middle_line)
    result += add_bottom_to_body(n, width)

    return result

def print_result(head, body, bottom):
    print(head + body + bottom)


n = int(input())
width = n * 5
height = n * 4 + 2
head_lines = create_head_lines(n)
body = create_body(n, width)
bottom_lines = create_bottom_lines(n)
print_result(head_lines, body, bottom_lines)