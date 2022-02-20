"""
If statemants

goodCredit = False
price = 1000000

if goodCredit:
    down_pay = (price * 0.1)

else:
    down_pay = (price * 0.2)

print (f"Down payment is: ${down_pay}" )
"""
'''
weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted.__round__(2)} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted.__round__(2)} lbs")
'''
#KURS SKONCZONY NA 1H:20MIN - WHILE LOOPS

i = 1
while i <= 7:
    print('*' * i)
    i = i + 1
print("Done")