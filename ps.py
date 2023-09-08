from math import floor,ceil
def prs(num):
    space=floor(num/2)
    trail=1
    for i in range(num):
        if i < ceil(num/2):
            for j in range(space):
                print(" ", end='')
            for j in range(2*i+1):
                print('*', end='')
            print('')
            space-=1
        else:
            if i == ceil(num/2):
                space+=2
            else:
                space+=1
            for j in range(space):
                print(" ", end="")
            for j in range(num-2*trail):
                print("*", end='')
            print('')
            trail+=1