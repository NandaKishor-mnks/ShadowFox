#1.Function using format() to a format number
def convert_number(number,format_type):
  return format(number,format_type)
result=format(145,'o')
print("Formatted result:",result)

# 2. Area of a circular pond and total water in the pond
radius = 84
pi = 3.14
pond_area = pi * radius * radius
print("Area of the pond:", pond_area)
water_per_sqm = 1.4
total_water = pond_area * water_per_sqm
print("Total water in the pond:", int(total_water))

# 3. Speed calculation
distance = 490          # meters
time_minutes = 7
time_seconds = time_minutes * 60
speed = distance / time_seconds
print("Speed in meters per second:", int(speed))
