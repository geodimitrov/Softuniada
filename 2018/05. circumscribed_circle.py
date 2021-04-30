from math import sqrt

def clean_data(circle_data, triangle_data):
    circle_data = [float(el.strip(",")) for el in circle_data[1:]]
    triangle_data = [float(el.strip(",")) for el in triangle_data[1:]]
    return circle_data, triangle_data

def read_input_data():
    circle_raw_data = input().split()
    triangle_raw_data = input().split()

    return clean_data(circle_raw_data, triangle_raw_data)

def get_circle_center_and_radius(data):
    center = data[:2]
    radius = data[2]
    return center, radius

def get_triangle_vertices(data):
    vertex_one = data[:2]
    vertex_two = data[2:4]
    vertex_three = data[4:]

    return vertex_one, vertex_two, vertex_three

def get_validity_range(value):
    return (round(value - 0.01, 2), round(value, 2), round(value + 0.01, 2))

def get_dist_between_points(point_one, point_two):
    x1, y1 = point_one
    x2, y2 = point_two
    distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return round(distance, 2)

def check_triangle_vertices(vertices, circle_center, validity_range):
    counter = 0

    for vertex in vertices:
        dist_from_vertex_to_circle_center = get_dist_between_points(vertex, circle_center)

        if dist_from_vertex_to_circle_center in validity_range:
            counter += 1

    return counter == 3

def calc_triangle_area(x1, x2, x3, y1, y2, y3):
    return round(abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2), 2)

def check_if_circle_center_inside_triangle(vertices, circle_center):
    x1, y1 = vertices[0]
    x2, y2 = vertices[1]
    x3, y3 = vertices[2]
    x4, y4 = circle_center
    triangleA_area = calc_triangle_area(x1, x2, x3, y1, y2, y3)
    triangleB_area = calc_triangle_area(x4, x1, x2, y4, y1, y2)
    triangleC_area = calc_triangle_area(x4, x2, x3, y4, y2, y3)
    triangleD_area = calc_triangle_area(x4, x1, x3, y4, y1, y3)
    area_validity_range = get_validity_range(triangleA_area)
    sum_areas = round(triangleB_area + triangleC_area + triangleD_area, 2)

    return sum_areas in area_validity_range

def print_result(is_circumscribed, center_is_inside):

    if is_circumscribed and center_is_inside:
        print(f"The circle is circumscribed and the center is inside.")
    elif is_circumscribed:
        print(f"The circle is circumscribed and the center is outside.")
    elif center_is_inside:
        print(f"The circle is not circumscribed and the center is inside.")
    else:
        print("The circle is not circumscribed and the center is outside.")

shape_pairs = int(input())

for pair in range(shape_pairs):
    data = read_input_data()
    circle_center, radius = get_circle_center_and_radius(data[0])
    triangle_vertices = get_triangle_vertices(data[1])
    radius_validity_range = get_validity_range(radius)
    is_circumscribed = check_triangle_vertices(triangle_vertices, circle_center, radius_validity_range)
    center_is_inside = check_if_circle_center_inside_triangle(triangle_vertices, circle_center)
    print_result(is_circumscribed, center_is_inside)