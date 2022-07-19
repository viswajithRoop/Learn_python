cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
car_pool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven
print("there are", cars, "cars available")
print("there are only", drivers, "drivers available.")
print("there will be", cars_not_driven, "empty cars today.")
print("we can transport", car_pool_capacity, "people today")
print("we have", passengers, "to carpool today.")
print("we need to put about", average_passengers_per_car, "in each car")

print()

my_name = 'Viswajith'
my_age = 25
my_height = 160
my_weight = 55
print(f"lets talk about {my_name}.")
print(f"he is {my_age} years old")
print(f"he is {my_height} cm tall.")
print(f"he is {my_weight} kg heavy.")
total = my_age + my_height + my_weight
print(f"if i add {my_age}, {my_height}, {my_weight} i will get {total}")
