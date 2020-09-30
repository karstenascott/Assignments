dis1 = int(input('Enter first distance:'))
dis2 = int(input('Enter second distance:'))
#This is where users can input any number.

product1 = dis1 * 2
product2 = dis2 * 2
#These are the variables for calculating the distance to and from.
print(' ')
print(product1)
print(product2)
print(' ') 
#These represent the operations carried out based on user input.

if dis1 < dis2:
    print('YES')
if dis2 > dis1:
    print('NO')
#These are my if statements.

print(' ')

if dis1 > dis2:
    print('Distance 1 is farther.')
elif dis1 < dis2:
    print('Distance 2 is farther.')
else:
    print("Distance 1 is farther.")

if dis2 < dis1:
    print('Distance 2 is closer.')
elif dis2 > dis1:
    print('Distance 2 is farther.')
else:
    print('Distance 2 is closer.')
#These are my if-else statements. 

print(' ')

while dis1 <=10000:
    print(dis1)
    dis1 = dis1 * 2
print(' ')
while dis2 <=10000:
    print(dis2)
    dis2 = dis2 * 3
#These are my while loops.

print(' ')

for y in "CONCLUSION":
    print(y)
#This is my for loop.  
    

