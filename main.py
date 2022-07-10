import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print("Comp Turn: Snake(s), Water(w) or Gun(g)?")
randNo = random.randint(1, 3)
if(randNo == 1):
    comp = 's'
elif(randNo == 2):
    comp = 'w'
elif(randNo == 3):
    comp = 'g'

you = input("Your Turn: Snake(s), Water(w) or Gun(g)?")
g = gameWin(comp, you)
if g == None:
    print("Game Tied!")
elif g:
    print("You Win!")
else:
    print("You Lost.")

print(f"Comp chose {comp}")
print(f"You chose {you}")
