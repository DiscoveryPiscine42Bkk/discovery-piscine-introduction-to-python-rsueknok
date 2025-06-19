array = [2, 8, 9, 48, 8, 22, -12, 2]
new_arrayEx02 = [value + 2 for value in array if value >5]
new_arrayEx03 = {value + 2 for value in array if value >5}

print(array)
print(new_arrayEx03)