unit_choice = input()

if unit_choice == "metric":
    mass_kg = int(input())
    formatted_mass = '{} kg'.format(mass_kg)
elif unit_choice == "imperial":
    mass_st = int(input())
    mass_lbs = int(input())
    formatted_mass = '{} st {} lbs'.format(mass_st, mass_lbs)
else:
    formatted_mass = "Invalid unit choice"

# main
print(formatted_mass)
