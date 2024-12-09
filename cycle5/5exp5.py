import graphics.rectangle as rect
import graphics.circle as circ
from graphics.volumes import cuboid
from graphics.volumes import sphere

# Rectangle
length = int(input("enter the length of the rectangle: "))
width = int(input("enter the width of the rectangle: "))
print(f"Rectangle Area: {rect.area(length, width)}")
print(f"Rectangle Perimeter: {rect.perimeter(length, width)}")

# Circle
radius = int(input("enter the radius of the circle: "))
print(f"Circle Area: {circ.area(radius)}")
print(f"Circle Perimeter (Circumference): {circ.perimeter(radius)}")

# Cuboid
cuboid_length = int(input("enter the length of the cuboid: "))
cuboid_width = int(input("enter the width of the cuboid: "))
cuboid_height = int(input("enter the height of the cuboid: "))
print(f"Cuboid Surface Area: {cuboid.area(cuboid_length, cuboid_width, cuboid_height)}")
print(f"Cuboid Volume: {cuboid.volume(cuboid_length, cuboid_width, cuboid_height)}")

# Sphere
sphere_radius = int(input("enter the radius of the sphere: "))
print(f"Sphere Surface Area: {sphere.area(sphere_radius)}")
print(f"Sphere Volume: {sphere.volume(sphere_radius)}")
