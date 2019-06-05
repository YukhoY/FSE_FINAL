walls = eval(input())
num_of_walls = walls.__len__()
min = num_of_walls
width = sum(walls[0])
while width-1:
    penatrate = num_of_walls
    width = width -1
    for wall in walls:
        wall[0] = wall[0]-1
        if not wall[0]:
            penatrate = penatrate -1
            wall.remove(0)
    if penatrate < min:
        min = penatrate
print(min)
