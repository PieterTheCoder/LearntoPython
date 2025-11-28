weight = int(input('Enter your weight: '))
unit = input('(K)g or (L)bs: ')
if unit.upper() == 'K':
    converted_weight = weight / 0.45
    print("Your weight in Lbs: " + str(converted_weight))
else:
    converted_weight = weight * 0.45
    print("Your weight in Kg: " + str(converted_weight))