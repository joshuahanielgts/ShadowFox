print("\nNumbers Section")
def format_example(num, fmt):
    return format(num, fmt)
formatted = format_example(145, 'o')
print("Formatted 145 with 'o':", formatted)  
radius = 84
area = 3.14 * radius ** 2
total_water = int(area * 1.4)
print("Area of the pond:", area)
print("Total water in the pond (litres):", total_water)
distance = 490
time_sec = 7 * 60
speed = int(distance / time_sec)
print("Speed (m/s):", speed)
