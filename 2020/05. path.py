
def find_ways(map):
    result = [""]

    for i in range(len(map)):
        el = map[i]

        if el == "*":
            end = len(result)

            for i in range(end):
                comb = result[i]
                result[i] += "R"

                for direction in directions:
                    comb += direction
                    result.append(comb)
                    comb = comb[:-1]

        else:
            for i in range(len(result)):
                result[i] += el

    return result


def print_result(possible_ways):
    sorted_possible_ways = sorted(possible_ways)
    print(f"{len(possible_ways)}")
    print("\n".join(sorted_possible_ways))


map = input()
directions = ["L", "S"]
possible_ways = find_ways(map)
print_result(possible_ways)