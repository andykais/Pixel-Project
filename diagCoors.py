#square of size 5
coor = [0,1,2,3,4]
for y in coor:
    for i in range(y+1):
        print y-i,i
print "second half"
y = 1
while y < len(coor):
    x = len(coor) - 1
    tempY = y
    while tempY < len(coor):
        print x, tempY
        tempY += 1
        x -= 1
    y += 1
