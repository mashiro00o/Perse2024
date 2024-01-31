first = input()
second = input()
third = input()

if first == second and first == third:
  print('OK')
elif first != second and first != third:
  print('BOTH MISMATCH')
elif first != second:
  print('ENTRY 2 MISMATCH')
else:
  print('ENTRY 3 MISMATCH')
