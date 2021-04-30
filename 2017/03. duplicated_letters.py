
def duplicate_letters(first_letter, second_letter):
    return first_letter == second_letter


def remove_duplicates_from_string(string):
    operations_count = 0
    moves_counter = 0

    while True:

        if moves_counter == len(string):
            break

        moves_counter = 0

        for i in range(len(string)):
            next_i = i + 1
            moves_counter += 1

            if next_i in range(len(string)):
                letter1 = string[i]
                letter2 = string[next_i]

                if duplicate_letters(letter1, letter2):
                    string = string.replace(letter1 + letter2, "", 1)
                    operations_count += 1
                    break

    return string, operations_count


def print_result(string, operations):

    if string:
        print(f"{string}\n{operations} operations")

    else:
        print(f"Empty String\n{operations} operations")


string = input()
new_string, operations_count = remove_duplicates_from_string(string)
print_result(new_string, operations_count)