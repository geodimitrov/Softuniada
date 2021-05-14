# SOLUTION 1 - using sets and intersection

def get_connection_range(x, y):
    if x < y:
        return {i for i in range(x, y + 1)}
    else:
        return {i for i in range(y, x + 1)}


def get_nexus_value(first_array, second_array, x, x1, y, y1):
    return first_array[x] + first_array[x1] + second_array[y] + second_array[y1]


def remove_nexus_elements_from_arrays(first_array, second_array, x, x1, y, y1):
    if x < x1:
        first_array = first_array[:x] + first_array[x1 + 1:]
    else:
        first_array = first_array[:x1] + first_array[x + 1:]

    if y < y1:
        second_array = second_array[:y] + second_array[y1 + 1:]
    else:
        second_array = second_array[:y1] + second_array[y + 1:]

    return first_array, second_array


def add_nexus_value_to_elements(nexus_value, first_array, second_array):
    if first_array:
        first_array = [el + nexus_value for el in first_array]

    if second_array:
        second_array = [el + nexus_value for el in second_array]

    return first_array, second_array


def print_result(first_array, second_array):
    print(", ".join(map(str, first_array)))
    print(", ".join(map(str, second_array)))


first_array = [int(el) for el in input().split()]
second_array = [int(el) for el in input().split()]


while True:
    command = input()

    if command == "nexus":
        print_result(first_array, second_array)
        break

    is_nexus = False
    connection_one, connection_two = command.split("|")
    x, y = [int(el) for el in connection_one.split(":")]
    x1, y1 = [int(el) for el in connection_two.split(":")]
    connection_one_range = get_connection_range(x, y)
    connection_two_range = get_connection_range(x1, y1)
    intersection = connection_one_range.intersection(connection_two_range)

    if intersection:
        nexus_value = get_nexus_value(first_array, second_array, x, x1, y, y1)
        first_array, second_array = remove_nexus_elements_from_arrays(first_array, second_array, x, x1, y, y1)
        first_array, second_array = add_nexus_value_to_elements(nexus_value, first_array, second_array)


# SOLUTION 2 - compare connection elements to determine whether there is nexus

def get_nexus_value(first_array, second_array, x, x1, y, y1):
    return first_array[x] + first_array[x1] + second_array[y] + second_array[y1]

def remove_nexus_elements_from_arrays(first_array, second_array, x, x1, y, y1):
    if x < x1:
        first_array = first_array[:x] + first_array[x1 + 1:]
    else:
        first_array = first_array[:x1] + first_array[x + 1:]

    if y < y1:
        second_array = second_array[:y] + second_array[y1 + 1:]
    else:
        second_array = second_array[:y1] + second_array[y + 1:]

    return first_array, second_array

def add_nexus_value_to_elements(nexus_value, first_array, second_array):
    if first_array:
        first_array = [el + nexus_value for el in first_array]

    if second_array:
        second_array = [el + nexus_value for el in second_array]

    return first_array, second_array

def print_result(first_array, second_array):
    print(", ".join(map(str, first_array)))
    print(", ".join(map(str, second_array)))


first_array = [int(el) for el in input().split()]
second_array = [int(el) for el in input().split()]


while True:
    command = input()

    if command == "nexus":
        break

    is_nexus = False
    connection_one, connection_two = command.split("|")
    x, y = (int(el) for el in connection_one.split(":"))
    x1, y1 = (int(el) for el in connection_two.split(":"))

    if x < y and (x < x1 and y > y1):
        is_nexus = True
    elif x > y and (x1 < x and y < y1):
        is_nexus = True
    elif x == y and ((x < x1 and y > y1) or (x1 < x and y < y1)):
        is_nexus = True

    if is_nexus:
        nexus_value = get_nexus_value(first_array, second_array, x, x1, y, y1)
        first_array, second_array = remove_nexus_elements_from_arrays(first_array, second_array, x, x1, y, y1)
        first_array, second_array = add_nexus_value_to_elements(nexus_value, first_array, second_array)

    if not first_array or not second_array:
        break

print_result(first_array, second_array)