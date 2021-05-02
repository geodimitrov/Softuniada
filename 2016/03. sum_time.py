def read_input():
    result = []

    for i in range(2):
        line = input().split("::")
        if len(line) > 1:
            days = int(line[0])
            hours, minutes = line[1].split(":")
        else:
            days = 0
            hours, minutes = line[0].split(":")
        result.append((days, int(hours), int(minutes)))
    return result

def sum_times_intervals(time_one, time_two):
    minutes = time_one[2] + time_two[2]
    hours = time_one[1] + time_two[1]
    days = time_one[0] + time_two[0]

    if minutes >= 60:
        minutes -= 60
        hours += 1

    if hours >= 24:
        hours -= 24
        days += 1

    return days, hours, minutes

def add_leading_zeroes_to_minutes_if_applicable(minutes):

    if minutes < 10:
        minutes = str(minutes).zfill(1 + len(str(minutes)))

    return minutes

def print_result(time):
    days, hours, minutes = time

    minutes = add_leading_zeroes_to_minutes_if_applicable(minutes)

    if days:
        print(f"{days}::{hours}:{minutes}")
    else:
        print(f"{hours}:{minutes}")

time_one, time_two = read_input()
total_time = sum_times_intervals(time_one, time_two)
print_result(total_time)