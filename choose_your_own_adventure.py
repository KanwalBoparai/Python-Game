name = input("Enter your name: ")

print("Welcome " + name + " to this game")

answer = input("You are on a gravel road and it has come to a dead end. you can turn either left or right. Would you go left or right?").lower()

if answer == "left":
    answer = input("You have come to river. You can either walk around it or swim cross the river. If you choose to walk around it, type walk and if you choose to swim, type swim. What would you like to do?").lower()
    if answer == "walk":
        print("You have walked a few miles, ran out of water, and lost the game.")
    elif answer == "swim":
        print("You swam across the river and found a bag of diamonds. YOU WIN THE GAME!")
    else:
        print("THIS IS AN INVALID ANSWER AND THE GAME HAS ENDED") 

elif answer == "right":
    answer = input("The sun has set and you have reached the forest. You can choose to pick some berries in the forest for some food, start a warm fire a sleep next to it, or continue through the forest without food or sleep. Please enter food, fire or walk for each of the choices respectively. You can only choose one: ").lower()
    if answer == "food":
        answer = input("You have been walking and haven't eaten in a few days now, but you have berries with you. However, you come across a random man that shouts that the berries are poisonous. You can choose to either eat the berries or throw them away. To eat the berries, type eat, and to ditch the berries, type throw: ").lower()
        if answer == "eat":
            print("You eat the berries and it turns out they were not poisonous. YOU WON THE GAME!")
        elif answer == "throw":
            print("You thew the berries away but they were never poisonous. YOU LOSE.")
        else:
            print("THIS IS AN INVALID ANSWER AND THE GAME HAS ENDED")
    elif answer == "fire":
        print("You choose to start a fire and fall asleep, but the fire spread around and you lost the game")
    elif answer == "walk":
        print("You walked to the end of forest and found home. YOU WIN THE GAME!") 
    else: 
        print("This answer is invalid and the game has ended.")
else:
    print("This answer is invalid either enter 'left' or 'right'. Please restart the game to try again")
