PI = 3.14
# input_radius is going to be in string 
input_radius = input("Please enter the radius : \n ")
radius = float(input_radius)
surface_area = 4*PI*radius**2
volume = (4/3)*PI*radius**3

print(f'Surface are of sphere is : {surface_area}')
print(f'Volume of Sphere is : {volume}')
