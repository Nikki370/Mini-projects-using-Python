import numpy as np
target = np.random.randint(1, 100)

while (target):
    user = input("User's choice: or Ouit{Q}: ")
    if user == "Q":
        break
    
    user = int(user)
    if user == target:
        print("HURRAH :) you won!")
        break
    elif user > target:
        print("Smaller number please...")
    else:
        print("Larger number Please...")

print("computer:", target)

print("GAME OVER!!!!")
