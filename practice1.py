import random

random_nubmer = random.randint(1, 100)
score = 0
while True:

    user_number = int(input())

    if random_nubmer == user_number:
        print("aqa awli 👌")
        score = score +1
        print("your score is: ",score)
        break

    elif user_number < random_nubmer:
        score = score +1
        print("boro bala pesar jan ⬆⬆⬆⬆")

    else:
        score = score +1
        print("biya payin ⬇⬇⬇⬇")    