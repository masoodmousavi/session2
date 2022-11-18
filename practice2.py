import random

robot_score = 0
user_score = 0

while True:
        
    a = random.randint(1, 3)


    if a == 1:
        pc_choice = "sang"

    elif a == 2:
        pc_choice = "kaqaz"

    else:
        pc_choice = "gheychi"   


    user_choice = input()
    print("___________")

    print("🤖:",pc_choice)
    print("👤:",user_choice)

    if pc_choice == "sang" and user_choice == "sang":
        print("equal")
        print("robot score:",robot_score)
        print("user score:",user_score)

    elif pc_choice == "sang" and user_choice == "kaqaz":
        print("user win")  
        user_score = user_score +1  
        print("robot score:",robot_score)
        print("user score:",user_score)
        
    elif pc_choice == "sang" and user_choice == "gheychi":
        print("robot win")    
        robot_score = robot_score +1
        print("robot score:",robot_score)
        print("user score:",user_score)

    elif pc_choice == "kaqaz" and user_choice == "sang":
        print("robot win")   
        robot_score = robot_score +1
        print("robot score:",robot_score)
        print("user score:",user_score)

    elif pc_choice == "kaqaz" and user_choice == "kaqaz":
        print("equal")    
        print("robot score:",robot_score)
        print("user score:",user_score)

    elif pc_choice == "kaqaz" and user_choice == "gheychi":
        print("user win")    
        user_score = user_score +1  
        print("robot score:",robot_score)
        print("user score:",user_score)

    elif pc_choice == "gheychi" and user_choice == "sang":
        print("user win") 
        user_score = user_score +1  
        print("robot score:",robot_score)
        print("user score:",user_score)

    elif pc_choice == "gheychi" and user_choice == "kaqaz":
        print("robot win")   
        robot_score = robot_score +1
        print("robot score:",robot_score)
        print("user score:",user_score)

    elif pc_choice == "gheychi" and user_choice == "gheychi":
        print("equal")    
        print("robot score:",robot_score)
        print("user score:",user_score)


    
