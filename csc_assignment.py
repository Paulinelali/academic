import math
done = ""
donemean = ""
con = []
initvalue = 1
averageinit = 0

while donemean != "yes":
    x = int(input("Enter value for x: "))
    con.append(x)
    donemean = input(" Are you done? ")
    if x < 0:
        print("Y")
    for x in con:
        initvalue = initvalue * x
        averageinit = averageinit + x
    Arithmetric = averageinit/(len(con))
    geomean = initvalue**(1/(len(con)))
print("The geometric mean is: ",geomean)
print("The arithmetic mean is: ",Arithmetric)
print("   ")
print("   ")
print("   ")
print("Start second question ")
#------------2-----------------
while done !="yes":
    x = int(input("Enter value for x: "))
    y = math.log(1/(1-x))
    if x > 0:
        print(x, "is not an illegal value!")
        break
    print('y(x) = ', y)
    done = input("are you done? ")
