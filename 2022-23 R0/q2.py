mass_1 = int(input())
volume_1 = int(input())
mass_2 = int(input())
volume_2 = int(input())

density_1 = mass_1 / volume_1
density_2 = mass_2 / volume_2

if density_1 > density_2:
    print("1")
elif density_2 > density_1:
    print("2")
else:
    print("same")
