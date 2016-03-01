#assigning value 100 to the variable cars
cars = 100

#assigning value 4.0 to the variable space_in_a_car
space_in_a_car = 4.0

#assigning value 30 to the variable drivers
drivers = 30

#assigning value 90 to the variable passengers
passengers = 90

#calculate the no. of not driven cars as the difference between the cars and the no. of drivers
cars_not_driven = cars - drivers

#assigning value of the variable drivers to the variable cars_driven
cars_driven = drivers

#calculate the total capacity of the cars as the multiplication of the two variables cars_driven and space_in_a_car
carpool_capacity = cars_driven * space_in_a_car

#calculate the average no. of passengers that fit into one car as the division of the two varaibles passengers and cars_driven
average_passengers_per_car = passengers / cars_driven


print "There %s are", cars, "%scars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
