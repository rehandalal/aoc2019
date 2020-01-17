from utils import get_input_data


data = get_input_data('1.txt')


def calculate_fuel_requirement(mass):
    fuel = (mass // 3) - 2
    return fuel


def calculate_true_fuel_requirement(mass):
    fuel = calculate_fuel_requirement(mass)
    if fuel > 0:
        fuel += calculate_true_fuel_requirement(fuel)
    else:
        return 0
    return fuel


sum_of_fuel = 0
sum_of_true_fuel = 0
for d in data:
    sum_of_fuel += calculate_fuel_requirement(int(d))
    sum_of_true_fuel += calculate_true_fuel_requirement(int(d))

print(f'Sum of fuel required for all modules: {sum_of_fuel}')
print(f'Sum of fuel required for all modules and fuel: {sum_of_true_fuel}')
