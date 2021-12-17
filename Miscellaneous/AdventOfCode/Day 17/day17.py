
'''
target area: x=236..262, y=-78..-58

'''
count = 0
for Vx in range(500):
    for Vy in range(-500, 500):
        dx, dy = Vx, Vy
        cur_x, cur_y = 0, 0
        good = False
        for _ in range(500):
            cur_x += dx
            cur_y += dy

            if dx > 0:
                dx -= 1
            elif dx < 0:
                dx += 1

            dy -= 1

            if 236 <= cur_x <= 262 and -78 <= cur_y <= -58:
                good = True
        if good:
            count += 1
                
print(count)

            

            