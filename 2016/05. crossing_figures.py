from math import sqrt


def read_input_data():

    for _ in range(2):
        line = input()

        if line.startswith("circle"):
            circle = eval(line.replace("circle", ""))

        else:
            rect = eval(line.replace("rectangle", ""))

    return list(map(float, circle)), list(map(float, rect))


def get_rect_vertices(rect):
    A = rect[:2]
    D = rect[2:]
    B = D[0], A[1]
    C = A[0], D[1]

    return A, B, C, D

def get_dist_between_points(point_one, point_two):
    x1, y1 = point_one
    x2, y2 = point_two
    distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return distance

def get_dist_between_vertices_and_center(vertices, center):
    result = []

    for vertex in vertices:
        distance = get_dist_between_points(vertex, center)
        result.append(distance)

    return result

def circle_is_inside_rect(center, radius, rect):
    Ax, Ay = rect[:2]
    Dx, Dy = rect[2:]
    Ox, Oy = center

    return Ax <= Ox - radius and Dx >= Ox + radius \
        and Ay >= Oy + radius and Dy <= Oy - radius

def circle_and_rect_cross(center, radius, rect):
    Ax, Ay = map(float, rect[:2])
    Dx, Dy = map(float, rect[2:])
    Ox, Oy = center

    return Ax < Ox - radius < Dx \
            or Ax < Ox + radius < Dx \
            or Ay > Oy - radius > Dy \
            or Ay > Oy + radius > Dy

def check_if_figures_cross(distances, center, radius, rect):

    if max(distances) <= radius:
        print("Rectangle inside circle")

    elif circle_is_inside_rect(center, radius, rect):
        print("Circle inside rectangle")

    elif circle_and_rect_cross(center, radius, rect):
        print("Rectangle and circle cross")

    else:
        print("Rectangle and circle do not cross")


n_cases = int(input())

for i in range(n_cases):
    circle, rect = read_input_data()
    circle_center = circle[:2]
    radius = circle[-1]
    rect_vertices = get_rect_vertices(rect)
    distances_between_vertices_and_center = get_dist_between_vertices_and_center(rect_vertices, circle_center)
    check_if_figures_cross(distances_between_vertices_and_center, circle_center, radius, rect)
