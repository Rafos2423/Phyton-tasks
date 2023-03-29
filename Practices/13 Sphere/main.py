from Practices.Sphere.Sphere import Sphere

s = Sphere(2.5, 1.0, 2.0, 3.0)

print(s.get_radius())
print(s.get_center())
print(s.get_volume())
print(s.get_square())

s.set_radius(3.0)
s.set_center(0.0, 0.0, 0.0)

print(s.is_point_inside(1.0, 2.0, 3.0))
print(s.is_point_inside(0.0, 0.0, 2.5))
