def is_inside(point,rectangle):
    if (rectangle[0] <= point[0] <= rectangle[0]+rectangle[2]) and (rectangle[1] <= point[1] <= rectangle[1]+rectangle[3]):
        return True
    else:
        return False
check = is_inside([200, 120], [140, 60, 100, 200])
if check == True:
    print("Your function is correct")
else:
    print("Ooops, bugs detected")