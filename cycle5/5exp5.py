import graphics.rectangle as rect
import graphics.circle as circ
from graphics.graphics_3d.cuboid import *
from graphics.graphics_3d.sphere import *

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
length = int(input("enter the length of the cuboid: "))
width = int(input("enter the width of the cuboid: "))
height = int(input("enter the height of the cuboid: "))
print(f"Cuboid Volume: {volume(length,width,height)}")

# Sphere
sphere_radius = int(input("enter the radius of the sphere: "))
print(f"Sphere Volume: {volume1(radius)}")
