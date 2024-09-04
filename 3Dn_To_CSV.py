#! python3
import tree2python as tp
import Rhino
import csv


# Assuming 'x' is the tree you get from somewhere
points_list = tp.manually_convert_tree_to_list(x)  # ignore the error, it's just a warning

surfaces = []
# Iterate through the nested lists to extract the X, Y, and Z coordinates
for sublist in points_list:fefefsfwwgf
    surface_points = []
    for inner_list in sublist:
        for point in inner_list:
            if isinstance(point, Rhino.Geometry.Point3d):
                surface_points.append((point.X, point.Y, point.Z))
            else:
                print("Error: point is not a Point3d object")
    surfaces.append(surface_points)

print(surfaces)

# write a csv file from the surfaces list
with open("surfaces.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Surface"])
    for i, surface in enumerate(surfaces):
        surface_str = "[" + ", ".join([f"({point[0]:.2f}, {point[1]:.2f}, {point[2]:.2f})" for point in surface]) + "]"
        writer.writerow([i, surface_str])


