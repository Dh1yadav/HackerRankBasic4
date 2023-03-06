thickness = int(input())
K = 'H'

#T_spike
for i in range(thickness):
    print((K*i).rjust(thickness-1)+K+(K*i).ljust(thickness-1))

#T_side
for i in range(thickness+1):
    print((K*thickness).center(thickness*2)+(K*thickness).center(thickness*6))

#Middle
for i in range((thickness+1)//2):
    print((K*thickness*5).center(thickness*6))    

#B_side
for i in range(thickness+1):
    print((K*thickness).center(thickness*2)+(K*thickness).center(thickness*6))    

#B_spike
for i in range(thickness):
    print(((K*(thickness-i-1)).rjust(thickness)+K+(K*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
