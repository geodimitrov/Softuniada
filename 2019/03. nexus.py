def read_input():
    result = []
    while True:

        command = input()

        if command == "nexus":
            break

        result.append(command)

    return result


def get_nexus_value(first_array, second_array, x, x1, y, y1):
    return first_array[x] + first_array[x1] + second_array[y] + second_array[y1]

def remove_nexus_elements_from_arrays(first_array, second_array, x, x1, y, y1):
    first_array = first_array[:x] + first_array[x1 + 1:]
    second_array = second_array[:y1] + second_array[y + 1:]

    return first_array, second_array


def add_nexus_value_to_elements(nexus_value, first_array, second_array):
    first_array = [el + nexus_value for el in first_array]
    second_array = [el + nexus_value for el in second_array]

    return first_array, second_array


def print_result(first_array, second_array):
    print(", ".join(map(str, first_array)))
    print(", ".join(map(str, second_array)))

first_array = list(map(int, input().split()))
second_array = list(map(int, input().split()))
commands = read_input()


for command in commands:
    is_nexus = False
    connection_one, connection_two = command.split("|")
    x, y = map(int, connection_one.split(":"))
    x1, y1 = map(int, connection_two.split(":"))

    if x <= y:
        if x < x1 and y > y1:
            is_nexus = True
    elif x >= y:
        if x1 < x and y < y1:
            is_nexus = True

    if is_nexus:
        nexus_value = get_nexus_value(first_array, second_array, x, x1, y, y1)
        first_array, second_array = remove_nexus_elements_from_arrays(first_array, second_array, x, x1, y, y1)
        first_array, second_array = add_nexus_value_to_elements(nexus_value, first_array, second_array)

    if not first_array or not second_array:
        break

print_result(first_array, second_array)
